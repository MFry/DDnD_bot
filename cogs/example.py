import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Example *cog* is loaded')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def info(self, ctx):
        """
         Returns bot info as an embedded message
        :param ctx: discord.py given context
        """
        description = self.bot.config["bot"]["description"]
        author = self.bot.config["bot"]["author"]
        embed = discord.Embed(title="DnD bot", description=description, color=0xeee657)
        # give info about you here
        embed.add_field(name="Author", value=author)
        # Shows the number of servers the bot is member of.
        embed.add_field(name="Server count", value=f"{len(self.bot.guilds)}")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Example(client))
