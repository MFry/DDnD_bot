import discord, os
from discord.ext import tasks, commands
from datetime import datetime, timedelta
from utils.message_helper import has_bot_sent_this_message

FRIDAY = 4
SATURDAY = 5
SUNDAY = 6
HOUR_BEFORE_EVENT = 13


class SessionOrganizer(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.main_channel = None
        self.last_session = ''
        self.announcement_channel = 'general'

    @commands.Cog.listener()
    async def on_ready(self):
        print('Session Organizer *cog* is loaded')
        for server in self.client.guilds:
            if server.name.lower() == "lambda legends":
                self.main_channel = discord.utils.get(server.channels, name=self.announcement_channel)
        message = 'I live again!'
        if not await has_bot_sent_this_message(self.client, self.main_channel, message, timedelta(minutes=10)):
            await self.main_channel.send(message)
        self.group_reminder.start()

    @tasks.loop(minutes=30)
    async def group_reminder(self):
        await self.client.wait_until_ready()
        if datetime.now().weekday() == FRIDAY:
            message = '**Reminder:** DnD session this weekend.'
            if not await has_bot_sent_this_message(self.client, self.main_channel, message):
                await self.main_channel.send(message)
        elif datetime.now().weekday() == SATURDAY:
            message = '**Reminder:** DnD session starts tomorrow at 14:00'
            if not await has_bot_sent_this_message(self.client, self.main_channel, message):
                await self.main_channel.send(message)
        elif datetime.now().weekday() == SUNDAY and datetime.now().hour == HOUR_BEFORE_EVENT:
            message = '---\n*Next session starts within the hour.*\n---'
            if not await has_bot_sent_this_message(self.client, self.main_channel, message):
                await self.main_channel.send(message)
                await self.send_last_session()

    async def send_last_session(self):
        await self.client.wait_until_ready()
        self.read_and_archive_last_session()
        await self.main_channel.send(f'---\n{self.last_session}\n---')

    def read_and_archive_last_session(self):
        location = './session_history/'
        file_name = 'last_session.md'
        last_session_file_name = f'{location}{file_name}'
        if os.path.isfile(last_session_file_name):
            self.last_session = open(last_session_file_name, 'r').read()
            last_session_timestamp = datetime.now() + timedelta(weeks=-1)
            os.rename(last_session_file_name, f'{location}{str(last_session_timestamp).replace(":","-")}.md')
        else:
            print('No new session file')


def setup(client):
    client.add_cog(SessionOrganizer(client))
