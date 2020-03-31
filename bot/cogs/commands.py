import discord
from discord.ext import commands
import random

class Kommandon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='aslak', help='Lappländsk svenska')
    async def _say_mys(self, ctx):
        quotes = [
            "Mys mys säger filten",
            "Prassel prassel säger pressun",
            "Voflor"
        ]
        response = random.choice(quotes)
        await ctx.send(response, tts=True)

    @commands.command(name='kasta', help='Kasta ett specifierat antal tärningar')
    async def _roll(self, ctx, number_of_dice: int):
        dice = [
            str(random.choice(range(1, 7)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice), tts=True)

    @commands.command(name='inbjudan', help='Skapa en tillfällig inbjudan')
    async def _create_invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=300)
        await ctx.send(f'Här är en inbjudan till servern: {link}')

    @commands.command(name='hej', help='Hej på dej')
    async def _hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hej {member.name} 👋', tts=True)
        else:
            await ctx.send(f'Hej {member.name}... hmm känns bekant.', tts=True)
        self._last_member = member

def setup(bot):
    bot.add_cog(Kommandon(bot))
