import discord

token = 'die'
# Your bot token from https://discord.com/developers/applications

prefix = ['dhar ', 'Dhar ', 'DHAR ']
# Bot will listen for commands starting with this prefix

activity = discord.Activity(name=f'{prefix}help', type=2)
# Set this to any status the bot should have on start
# Types:
#   1 - Playing ...
#   2 - Listening to ...
#   3 - Watching ...
#   4 - Streaming (you can set url='') ...
#   5 - Competing in ...

triggers = ['@here', '@everyone']
# The bot will respond to any message containing these

ownerID = 822679038434213908
# Put your user id here, lets you reload the bot

cat_key = ''
# Get an api key from https://thecatapi.com/

dog_key = ''
# Get an api key from https://thedogapi.com/