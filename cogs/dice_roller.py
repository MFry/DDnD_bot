import discord
from discord.ext import commands
import random


class DiceRoller(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Dice rolling cog is loaded')

    @commands.command()
    async def roll(self, ctx, dice: str):
        cleaned_dice = dice.lower()
        dice_list = dice.split('d')
        dice_number = int(dice_list[0])
        dice_type = int(dice_list[1])
        if dice_number == 1:
            dice_total = random.randint(1, dice_type)
            await ctx.send(
                f'*{ctx.message.author} rolls {dice} for {dice_total}*'
            )
        elif dice_number > 1
            result = []
            dice_total = 0
            ii = 0
            while ii < dice_number:
                result.append(random.randint(1, dice_type))
                dice_total += result[ii]
                ii += 1

            rolls = ", ".join(map(str, result))
            await ctx.send(
                f'*{ctx.message.author} rolls {dice} for: {rolls}; a total of {dice_total}*'
            )
        else:
            await ctx.send(
                f'*{ctx.message.author} rolls a non-physical number of dice and takes 5 damage*'
            )

def setup(client):
    client.add_cog(DiceRoller(client))
