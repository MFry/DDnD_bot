import discord
import os
from discord.ext import commands

TOKEN = open('token', 'r').read()


bot = commands.Bot(command_prefix='!')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if not filename.startswith('_') and filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[-2]}')

bot.run(TOKEN)
