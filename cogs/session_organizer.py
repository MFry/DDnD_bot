import discord
from discord.ext import tasks, commands
from datetime import datetime

SATURDAY = 5
SUNDAY = 6
HOUR_BEFORE_EVENT = 13


class SessionOrganizer(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.main_channel = None

    @commands.Cog.listener()
    async def on_ready(self):
        print('Session Organizer *cog* is loaded')
        for server in self.client.guilds:
            if server.name.lower() == "lambda legends":
                self.main_channel = discord.utils.get(server.channels, name='general')
        await self.main_channel.send('I live again!')
        self.group_reminder.start()

    @tasks.loop(minutes=30)
    async def group_reminder(self):
        await self.client.wait_until_ready()

        if datetime.now().weekday() == SATURDAY:
            await self.main_channel.send('**Reminder:** DnD session starts tomorrow at 14:00')
        elif datetime.now().weekday() == SUNDAY and datetime.now().hour == HOUR_BEFORE_EVENT:
            await self.main_channel.send('*Next session starts within the hour.*')
        elif datetime.now().weekday() == 2:
            await self.main_channel.send('It\'s Wednesday my Dudes!')


def setup(client):
    client.add_cog(SessionOrganizer(client))
