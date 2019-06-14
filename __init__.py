from discord.ext import commands

TOKEN = open('token', 'r').read()


bot = commands.Bot(command_prefix='!')

bot.load_extension("maincog")

bot.run(TOKEN)
