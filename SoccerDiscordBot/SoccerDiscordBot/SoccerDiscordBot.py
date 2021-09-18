import discord
import asyncio
import dataBase

client = discord.Client()

async def send(message,text):
    await message.channel.send(text)

async def inputHandler(message):
    if "%getStats" in message.content and (len(message.content) >= 9):
        print("this")
        await send(message,dataBase.getStats(message.content))
    elif '%compare' in message.content and (len(message.content) >= 10 and "|" in message.content):
        await send(message,dataBase.compare(message.content))
    else:
        await message.channel.send("Request format is %Command then args sepreated by spaces")
    
@client.event
async def on_ready():
    print("Bot Running")

@client.event
async def on_message(message):
    if message.author != client.user:
        await inputHandler(message)

client.run("ODg4ODA2MDU0ODE1NzMxNzMz.YUYDJA.-peMP7SORqlIhQVj2D4QcDkXvBU")