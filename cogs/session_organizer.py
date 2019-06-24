import discord
import os
from discord.ext import tasks, commands
from datetime import datetime, timedelta
from utils.message_helper import has_bot_sent_this_message

FRIDAY = 4
SATURDAY = 5
SUNDAY = 6


class SessionOrganizer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.main_channel = None
        self.last_session = ''
        self.dnd_config = self.bot.config["dnd"]["session"]
        self.announcement_channel = self.bot.config["server"]["channels"]["announcement"]
        self.dnd_server = self.bot.config["test_server"]["name"]
        location = './session_history/'
        file_name = 'last_session.md'
        self.file_name = f'{location}{file_name}'

    @commands.Cog.listener()
    async def on_ready(self):
        for server in self.bot.guilds:
            if server.name.lower() == self.dnd_server.lower():
                self.main_channel = discord.utils.get(server.channels, name=self.announcement_channel)
        #
        # message = 'I live again!'
        # if not await has_bot_sent_this_message(self.client, self.main_channel, message, timedelta(minutes=10)):
        #     await self.main_channel.send(message)
        print('Session Organizer *cog* is loaded')
        await self.post_last_session()
        self.group_reminder.start()

    @tasks.loop(minutes=30)
    async def group_reminder(self):
        await self.bot.wait_until_ready()
        START_TIME = self.dnd_config["start_time"]
        HOUR_BEFORE_EVENT = self.dnd_config["hour_before_session"]
        if datetime.now().weekday() == FRIDAY:
            message = f'**Reminder:** {self.dnd_config["reminderTwoDaysBefore"]}'
            if not await has_bot_sent_this_message(self.bot, self.main_channel, message):
                await self.main_channel.send(message)
        elif datetime.now().weekday() == SATURDAY:
            message = f'**Reminder:** {self.dnd_config["reminderOneDayBefore"]}'.format(
                self.dnd_config["start_time"])
            if not await has_bot_sent_this_message(self.bot, self.main_channel, message):
                await self.main_channel.send(message)
        elif datetime.now().weekday() == SUNDAY and datetime.now().hour == HOUR_BEFORE_EVENT:
            message = f'---\n*Next session starts at {START_TIME}.*\n---'
            if not await has_bot_sent_this_message(self.bot, self.main_channel, message):
                await self.main_channel.send(message)
                await self.post_last_session()

    async def post_last_session(self):
        await self.bot.wait_until_ready()
        if not self.open_last_session():
            return
        await self.send_session_chunks()
        self.archive_last_session()

    def archive_last_session(self):
        last_session_file_name = self.file_name
        location = self.dnd_config["recentSessionFileLocation"]
        last_session_timestamp = datetime.now() + timedelta(weeks=-1)
        # ':' are reserved key words
        os.rename(last_session_file_name, f'{location}{str(last_session_timestamp).replace(":", "-")}.md')

    async def send_session_chunks(self):
        content = self.last_session
        if not content:
            return
        await self.main_channel.send('---')
        if len(content) < 2000:
            await self.main_channel.send(content)
        else:
            try:
                for message_chunk in [content[i:i+2000] for i in range(0, len(content), 2000)]:
                    if message_chunk:
                        await self.main_channel.send(message_chunk)
            except discord.errors.HTTPException as e:
                print('Could not output last session')
                print(e)
        await self.main_channel.send('---')

    def open_last_session(self):
        last_session_file_name = self.file_name
        if os.path.isfile(last_session_file_name):
            self.last_session = open(last_session_file_name, 'r').read()
            return True
        else:
            print('No new session file')
            return False


def setup(client):
    client.add_cog(SessionOrganizer(client))
