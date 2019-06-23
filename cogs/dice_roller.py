import discord
from discord.ext import commands
import random

#Accepts an arbitrary number and type of dice as input of the form xdy, where 'x'
#is the integer number of dice and 'y' is the integer number of faces on each die.
#d is a delimiter.

class DiceRoller(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Dice Roller *cog* is loaded')

    @commands.command()
    async def roll(self, ctx, dice: str):
        """
        Rolls an arbitrary number of dice with an arbitrary number of sides
        :param dice: String of the form xdy, where x is the integer number of dice, and y is the integer number of sides per dice.
        """
        cleaned_dice = dice.lower()
        dice_list = cleaned_dice.split('d')
        if not dice_list[0]:                                                    #handle inputs of the type 'dy', with implied dice number equal to 1
            dice_number = 1
        else:
            dice_number = int(dice_list[0])
        dice_type = int(dice_list[1])
        if dice_number == 1:                                                    #generate a single dice roll and send
            dice_total = random.randint(1, dice_type)
            await ctx.send(
                f'*{ctx.message.author} rolls {dice} for {dice_total}*'
            )
        elif dice_number > 1:                                                   #generate x number of dice rolls, send the individual rolls and sum
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
        else:                                                                   #handle invalid inputs
            await ctx.send(
                f'*{ctx.message.author} rolls a non-physical number of dice and takes 5 damage*'
            )

def setup(client):
    client.add_cog(DiceRoller(client))
