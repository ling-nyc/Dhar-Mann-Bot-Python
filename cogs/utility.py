import discord
import time
import psutil
import main
from datetime import datetime
from discord.ext import commands


class Utility(commands.Cog, description='Somewhat useful commands'):
    def __init__(self, bot):
        self.bot = bot

    def getUptime(self):
        seconds = time.time()-main.startTime
        min, sec = divmod(seconds, 60)
        hour, min = divmod(min, 60)
        return f'{hour:0.0F} hours, {min:0.0F} minutes and {sec:0.0F} seconds'

    def getStartTime(self):
        value = datetime.fromtimestamp(main.startTime)
        return value.strftime('%Y-%m-%d %H:%M:%S')

    def check_author(self, author):
        def inner_check(message):
            return message.author == author
        return inner_check

    @commands.command(help='Show information about the bot', aliases=['info', 'bot'])
    async def botinfo(self, ctx):
        em = discord.Embed(
            title='Bot Info',
            color=discord.Color.random()
        )
        em.add_field(name='Uptime', value=self.getUptime(), inline=False)
        em.add_field(name='Since', value=self.getStartTime(), inline=False)
        em.add_field(name='System Stats',
                     value=f'{psutil.cpu_percent()}% CPU usage\n{psutil.virtual_memory().percent}% memory usage', inline=False)

        await ctx.send(embed=em)

    @commands.command(help="Show current member count", aliases=["membercount"])
    async def members(self, ctx):
        em = discord.Embed(
            title=f"Members in {ctx.guild}",
            description=f"```{ctx.guild.member_count}```",
            color=discord.Color.blurple()
        )

        await ctx.send(embed=em)

    @commands.command(help='Gets bot latency', aliases=['latency', 'pong'])
    async def ping(self, ctx):
        em = discord.Embed(
            title='Pinging. . .',
            description=f'{round(self.bot.latency, 3)}ms',
            color=discord.Color.gold()
        )
        await ctx.send(embed=em)

    @commands.command(help='Gets a user\'s profile picture', aliases=['av', 'avatar'])
    async def pfp(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        em = discord.Embed(
            title=f'{user}\'s avatar'
        )
        em.set_footer(text=f'Requested by {ctx.author}')
        em.set_image(url=user.avatar_url)
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Utility(bot))
