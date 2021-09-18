import discord
import asyncio
import dataBase

client = discord.Client()

async def send(message,text):
    await message.channel.send(text)

async def inputHandler(message):
    if "%getStats" in message.content and (len(message.content) >= 9):
        a1,a2,name = dataBase.getStats(message.content)
        if name ==None:
            await message.channel.send(a1)
        else:
            embedVar = discord.Embed(title=name, colour=discord.Colour(0xFF015B))
            embedVar.add_field(name="Name:", value=a1, inline = True)
            embedVar.add_field(name=name, value=a2, inline = True)
            embedVar.set_footer(text= client.user.name, icon_url = client.user.avatar_url)
            await message.channel.send(embed=embedVar)

    elif '%compare' in message.content and (len(message.content) >= 10 and "|" in message.content):
        a1,a2,a3,pos,name1,name2 = dataBase.compare(message.content)
        if a2 == None:
            await send(message,a1)
        elif(pos != None):
            embedVar = discord.Embed(title=pos + " Comparison", colour=discord.Colour(0xFF015B))
            embedVar.add_field(name="Names:", value=a1, inline = True)
            embedVar.add_field(name=name1, value=a2, inline = True)
            embedVar.add_field(name=name2, value=a3, inline = True)
            embedVar.set_footer(text= client.user.name, icon_url = client.user.avatar_url)
            await message.channel.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title = "Comparison", colour=discord.Colour(0xFF015B))
            embedVar.add_field(name="Names:", value=a1, inline = True)
            embedVar.add_field(name=name1, value=a2, inline = True)
            embedVar.add_field(name=name2, value=a3, inline = True)
            embedVar.set_footer(text= client.user.name, icon_url = client.user.avatar_url)
            await message.channel.send(embed=embedVar)
    elif "hello" in message.content:
        await send(message,"```diff\n -" + "hello" + "\n```" + "```css\n" + "[world]" + "\n```")
    elif "%getStats" in message.content or "%comparison" in message.content:
        await message.channel.send("Request format is %Command then args sepreated by spaces")
    
@client.event
async def on_ready():
    print("Bot Running")

@client.event
async def on_message(message):
    if message.author != client.user:
        await inputHandler(message)

client.run("ODg4ODA2MDU0ODE1NzMxNzMz.YUYDJA.-peMP7SORqlIhQVj2D4QcDkXvBU")