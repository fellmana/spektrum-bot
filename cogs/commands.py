import discord
from discord.ext import commands
import random

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Hello', help='Testing testing')
    async def _hello_world(self, ctx):
        response = "World!"
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

    @commands.command(name='dice', help='Kasta tärning')
    async def _roll(self, ctx, number_of_dice: int):
        dice = [
            str(random.choice(range(1, 7)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))

def setup(bot):
    bot.add_cog(Commands(bot))