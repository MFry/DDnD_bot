import discord, random

client = discord.Client()
TOKEN = open('token', 'r').read()


@client.event
async def on_ready():
    print("Thorgal the sad and unfortunate \"dragon\"-born has fainted. Again...")
    await client.change_presence(activity=discord.Game(name="Dungeons and Robots"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = message.channel
    cleaned_text = message.content.lower()
    if cleaned_text == "hello warforged":
        await channel.send("sup")
    if cleaned_text == "how is thorgal?":
        await channel.send("Thorgal the sad and unfortunate \"dragon\"-born has fainted. Again...")
    if cleaned_text == "roll":
        if message.author.name == 'codefry':
            await channel.send('The dm rolls a nat 20.')
        else:
            result = random.randint(1, 20)
            await channel.send(f'*D20 rolls across the table and lands on {result}*')


client.run(TOKEN)
