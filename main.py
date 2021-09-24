import os
import discord
import requests
import json
import random
from discord.ext import commands

activity = discord.Activity(name=f' Dhar Man', type=3)
# Set this to any status the bot should have on start
# Types:
#   1 - Playing ...
#   2 - Listening to ...
#   3 - Watching ...
#   4 - Streaming (you can set url='') ...
#   5 - Competing in ...
client = discord.Client()

token = os.getenv['BOT_TOKEN']


with open('words.json') as f:
  words = json.load(f)

# words['people'], words['actions'], words['endings']

@client.event
async def on_ready():
    await client.change_presence(activity=(activity))
    print('Bot is ready.')

@client.event 
async def on_message(message):

  if not message.author.bot:

    if message.content.startswith('dhar man'):
    
      title = f"{random.choice(words['people'])} {random.choice(words['actions'])} {random.choice(words['people'])}, {random.choice(words['endings'])}!"
      
      await message.reply(title)
    if message.content.startswith('dhar ping'):

      await message.reply('Pong! %0.2fms' % client.latency)

client.run(token)
