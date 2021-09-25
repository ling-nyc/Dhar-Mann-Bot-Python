import discord
import random
import time
import config
import re
from discord.ext import commands
from pretty_help import PrettyHelp
from insultgenerator import phrases
import requests
from faker import Faker
faker = Faker()

import json

with open('words.json') as f:words = json.load(f)

class Wisdom(commands.Cog, description='Receive wisdom from Dhar Mann himself.'):
    def __init__(self, bot):
        self.bot = bot
        self.bot.snipedMessage = ''

    @commands.Cog.listener()
    async def on_message(self, msg):
        if any(trigger in msg.content for trigger in config.triggers):
            roast = random.choice(open('insults.txt').readlines())
            await msg.channel.send(roast)

        if msg.content.startswith(f'<@!{self.bot.user.id}>'):
            await msg.channel.send(f'Use {config.prefix}help for a list of commands')

    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        self.bot.snipedMessage = msg
    
    @commands.command(help='Absolutely roasts someone. (Don\'t use if easily offended!!!)', pass_context=True)
    async def roast(self, ctx, args=None):
        if args == None:
            args = ctx.author.mention
        roastEmbed = discord.Embed(
            description=phrases.get_so_insult_with_action_and_target(
                args, 'they'),
            color=discord.Color.red()
        )
        roastEmbed.set_footer(text=f'Roast from {ctx.author.name}')
        await ctx.send(embed=roastEmbed)

    @commands.command(help='Reveals someone\'s totally real personal info!!!', pass_context=True)
    async def dox(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        doxEmbed = discord.Embed(
            title=f'{user.name}\'s Personal Info:',
            color=0x7289da
        )
        doxEmbed.add_field(name='Address', value=faker.address(), inline=False)
        doxEmbed.add_field(name='IP', value=faker.ipv4(), inline=True)
        doxEmbed.set_thumbnail(url=user.avatar_url)

        await ctx.send(embed=doxEmbed)
    @commands.command(help='Gets a random cat picture')
    async def cat(self, ctx):
        req = requests.get(
            f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key={config.cat_key}")
        r = req.json()
        em = discord.Embed(title='Cat 🐱')
        em.set_author(
            name=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        em.set_image(url=str(r[0]["url"]))
        await ctx.send(embed=em)
    @commands.command(help='Gets a random dog picture')
    async def dog(self, ctx):
        req = requests.get(
            f"https://api.thedogapi.com/v1/images/search?format=json&x-api-key={config.dog_key}")
        r = req.json()
        em = discord.Embed(title='Good Boi')
        em.set_author(
            name=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        em.set_image(url=str(r[0]["url"]))
        await ctx.send(embed=em)
    @commands.command(help='Get a random Dhar Mann title', aliases=['man', 'mann'])
    async def title(self, ctx):
        title = f"{random.choice(words['people'])} {random.choice(words['actions'])} {random.choice(words['people'])}, {random.choice(words['endings'])}!"
        await ctx.reply(title)
    @commands.command(help='Snipe the last deleted message')
    async def snipe(self, ctx):
        if self.bot.snipedMessage:
            content = self.bot.snipedMessage.content
            content = content if content else '** **'
            author = self.bot.snipedMessage.author
            timestamp = str(self.bot.snipedMessage.created_at
                            ).split('.')[0] + ' UTC'

            em = discord.Embed(
                color=discord.Color.random()
            )
            em.set_author(
                name=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
            em.add_field(name='Sniped Message', value=f'{content}')
            em.set_footer(text=f'{author}, at {timestamp}',
                          icon_url=author.avatar_url)

            await ctx.send(embed=em)
        else:
            await ctx.send('No message to snipe!')




def setup(bot):
    bot.add_cog(Wisdom(bot))
