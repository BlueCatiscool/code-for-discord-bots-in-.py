# NOTE: you need to install discord.py before doing any of this.
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!') # Change this one to the one you want to use.

@client.event
async def on_ready():
  print(f'Logged in as {client.user.name}#{bot.user.discriminator}')

@bot.commands(name='echo')
async def echo(ctx, *, message):
  await ctx.send(message)
  
 client.run(token-goes-here)
