import discord
import random
import time
import config
import re
from discord.ext import commands
from pretty_help import PrettyHelp
from insultgenerator import phrases
from faker import Faker
faker = Faker()

class Wisdom(commands.Cog):
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



def setup(bot):
    bot.add_cog(Wisdom(bot))
