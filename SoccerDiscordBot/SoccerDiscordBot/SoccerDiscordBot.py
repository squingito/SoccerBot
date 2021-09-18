import discord
import asyncio



client = discord.Client()

async def InputHandler():
    def check(message):
        return message.author != client.user
    try:
        message = await client.wait_for('message', check=check,timeout = 300)
    except asyncio.TimeoutError:
        return None, 'noResponce'
    else:
        print(message.author.nick)
        print(message)
        if "" in message.content:
            return message, ""

@client.event
async def on_ready():
    print("Bot Running")

@client.event
async def on_message(message):
    if message.author != client.user:
        await message.channel.send(message.content);

client.run("ODg4ODA2MDU0ODE1NzMxNzMz.YUYDJA.-peMP7SORqlIhQVj2D4QcDkXvBU")