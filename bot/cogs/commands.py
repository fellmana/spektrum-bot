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
            "Voflor",
            "Glassepaus",
            "Glaffepaus",
            "God morgon",
            "Tundercash",
            "Kuuleppa poka",
            "ouptutten"
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
        pair =  False
        three = False
        won = False
        for die in dice:
            n = dice.count(die)
            if n > 5 and not won:
                won = True
                await ctx.message.add_reaction('🔥')
            elif n == 5 and len(dice) == 5 and not won:
                won = True
                await ctx.message.add_reaction('🏆')
                y = ':regional_indicator_y:'
                a = ':regional_indicator_a:'
                t = ':regional_indicator_t:'
                z = ':regional_indicator_z:'
                await ctx.send(f'{y} {a} {t} {z} {y}', tts=True)
            elif n == 4:
                await ctx.message.add_reaction('🎀')
            if n == 3:
                three = True
                await ctx.message.add_reaction('👏')
            if n == 2:
                pair = True
        if pair and three:
            await ctx.message.add_reaction('🏠')

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
