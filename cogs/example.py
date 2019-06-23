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

        :param ctx:
        :return:
        """
        embed = discord.Embed(title="DnD bot", description="Nicest bot there is ever.", color=0xeee657)

        # give info about you here
        embed.add_field(name="Author", value="Michal Frystacky")

        # Shows the number of servers the bot is member of.
        embed.add_field(name="Server count", value=f"{len(self.bot.guilds)}")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Example(client))
