import discord
from discord.ext import commands
from bisect import bisect_left


class Initiative(commands.Cog):
    initiatives = []
    temp_initiatives = []
    current_initiative = 0
    current_round = 1

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Initiative *cog* is loaded')

    @staticmethod
    def _sort_initiatives(to_sort):
        return sorted(to_sort, key=lambda x: x[1], reverse=True)

    @commands.command(name="setInitiative", aliases=["si"])
    async def set_initiative(self, ctx, *args):
        """
         Sets initial combat initiative
        :param args: space separated tuples of {name} {initiative_value}...
        :aliases: si
        ::
            # example
            !si me 20 you 1
        """
        it = iter(args)
        self.initiatives.extend(self._sort_initiatives(zip(it, it)))
        await ctx.send('Set initiative')

    @commands.command(name="addInitiative", aliases=["ai"])
    async def add_initiative(self, ctx, *args):
        """
         Add additional entities to the current combat round
        :param args: space separated tuples of {name} {initiative_value}...
        :aliases: ai
        """
        it = iter(args)
        self.temp_initiatives = self._sort_initiatives(zip(it, it))

    @commands.command(name="nextInitiative", aliases=["ni"])
    async def next_initiative(self, ctx):
        """
         Moves to the next entities turn
        :aliases: ni
        :returns the name of the next entity and its initiative
        """
        NAME = 0
        INIT = 1
        i = self.current_initiative
        if i > len(self.initiatives):
            entity = self.initiatives[-1]
        else:
            entity = self.initiatives[i]
        if self.temp_initiatives:
            if entity[INIT] < self.temp_initiatives[0][INIT]:
                new_entity = self.temp_initiatives.pop(0)
                self.initiatives.append(new_entity)
                self.initiatives = self._sort_initiatives(self.initiatives)
                i = bisect_left(self.initiatives, entity) - 1
                entity = new_entity
        if i >= len(self.initiatives):
            await ctx.send('-'*10)
            await ctx.send(' Round is over')
            await ctx.send('-' * 10)
            self.current_round += 1
            i = 0
            entity = self.initiatives[i]
        self.current_initiative = i + 1
        await ctx.send(f'{entity[NAME]} is up. Initiative: {entity[INIT]}')

    @commands.command(name="endInitiative", aliases=["ei"])
    async def end_initiative(self, ctx):
        """
         Ends initiative
        :aliases: ei
        """
        self.initiatives = []
        self.current_initiative = 0
        await ctx.send('Combat is over. Is Thorgal dead?')


def setup(client):
    client.add_cog(Initiative(client))
