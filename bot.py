import discord
from discord.ext import commands
import random

p = "r!"
client = commands.Bot(command_prefix=p)

f = open('token.txt', 'r')
token = f.read()
f.seek(0)
f.close()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send('wow, just wow, you want the ping? well ok fine here i guess. {0}'.format(round(client.latency, 4)*1000) + ' ms')

@client.command()
async def what(ctx):
    await ctx.send('i want to know the same thing myself tbh')

@client.command()
async def kill(ctx, arg):
    line = random.choice(open('kill.txt').readlines())
    await ctx.send('**' + arg + '**' + line)

client.run(token)