import discord, random, datetime
from datetime import datetime
import asyncio


TOKEN = open('token', 'r').read()


class DiscordDnDBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_channel = None
        self.schedule_reminder.start()

    async def on_ready(self):
        random.seed(datetime.now())
        print("Thorgal the sad and unfortunate \"dragon\"-born has fainted. Again...")
        await client.change_presence(activity=discord.Game(name="Dungeons and Robots"))
        await self.waking_up()

    async def on_message(self, message):
        if message.author == client.user:
            return
        channel = message.channel
        cleaned_text = message.content.lower()
        if cleaned_text == "hello warforged":
            await channel.send("sup")
        if cleaned_text == "how is thorgal?":
            await channel.send("*Thorgal the sad and unfortunate \"dragon\"-born has fainted.* **Again...**")
        if cleaned_text == "simulate thorgal rolling":
            await channel.send(f'natural 1, natural 1, *next 5 rolls* '
                               f'{random.randint(1, 3)}, {random.randint(1, 3)}, {random.randint(1, 3)},'
                               f' {random.randint(1, 3)}, {random.randint(1, 8)}\n'
                               f'*Oh look an event that doesn\'t matter!*     **natural 20**')
        if cleaned_text == "simulate thorgal in combat":
            await channel.send(
                f'Initiative: Thorgal rolls a **nat20**!\n [Round 2 in combat]\t\t *Thorgal has fainted in combat*\n [Round 3 in combat]\t\t **Thorgal has failed his second death savings throw**\n')
        if cleaned_text == "roll":
            if message.author.name == 'codefry':
                await channel.send('The dm rolls a nat 20.')
            else:
                result = random.randint(1, 20)
                if result == 1:
                    await channel.send(
                        f'*{message.author.name}\'s palms are sweaty, luck weak, dice are heavy*\n **{message.author.name} rolls a natural 1***')
                elif result == 20:
                    await channel.send(f'*Using Jedi Fucking Magic, {message.author.name} rolls a **natural 20***')
                else:
                    await channel.send(f'*{message.author.name} rolls a d20 across the table and lands on {result}*')

    async def schedule_reminder(self):
        await self.main_channel.send('Lets run this!')
        # Saturday
        if datetime.now().weekday() == 5:
            await self.main_channel.send('**Reminder:** DnD session starts tomorrow at 14:00')
        if datetime.now().weekday() == 2:
            await self.main_channel.send('It\'s Wednesday my Dudes!')
        await asyncio.sleep(60)

    async def waking_up(self):
        await self.wait_until_ready()
        for server in self.guilds:
            if server.name.lower() == "lambda legends":
                self.main_channel = discord.utils.get(server.channels, name='general')
        await self.main_channel.send('I live again!')


client = DiscordDnDBot()
client.run(TOKEN)
