import discord
import json
from discord.ext import commands
from dotenv import load_dotenv


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        load_dotenv()
        with open("config.json") as config:
            self.bot.config = json.load(config)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Main *cog* is loaded')
        await self.bot_status()

    async def bot_status(self):
        await self.bot.wait_until_ready()
        activity = self.bot.config['bot']['activities']
        await self.bot.change_presence(activity=discord.Game(name=activity))


def setup(bot):
    bot.add_cog(MainCog(bot))
