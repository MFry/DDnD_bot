import discord
from discord.ext import commands


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Main *cog* is loaded')
        await self.bot_status()

    async def bot_status(self):
        await self.bot.wait_until_ready()
        await self.bot.change_presence(activity=discord.Game(name="Dungeons and Robots"))


def setup(bot):
    bot.add_cog(MainCog(bot))
