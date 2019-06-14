from discord.ext import commands

class MainCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_role("Mod")
    async def acommand(self, ctx, argument):
       await self.bot.say("Stuff")

    async def on_message(self, message):
        print(message.content)

def setup(bot):
    bot.add_cog(MainCog(bot))