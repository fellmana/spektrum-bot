import discord
from discord.ext import commands
import random

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', help='Testing testing')
    async def _hello_world(self, ctx):
        response = "world!"
        await ctx.send(response)

    @commands.command(name='aslak', help='Lappländsk svenska')
    async def _say_mys(self, ctx):
        quotes = [
            "Mys mys säger filten",
            "Prassel säger pressun",
            "Voflor"
        ]
        response = random.choice(quotes)
        await ctx.send(response)

    @commands.command(name='kasta', help='Kasta ett specifierat antal tärningar')
    async def _roll(self, ctx, number_of_dice: int):
        dice = [
            str(random.choice(range(1, 7)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))

    @commands.command(name='inbjudan', help='Skapa en tillfällig inbjudan')
    async def _create_invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=300)
        await ctx.send(f'Här är en inbjudan till servern: {link}"')

def setup(bot):
    bot.add_cog(Commands(bot))