import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Välkommen {member.mention} 🤙')

    @commands.command(name='hej', help='Hej på dej.')
    async def _hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hej {member.name} 👋')
        else:
            await ctx.send(f'Hej {member.name}... hmm känns bekant.')
        self._last_member = member


def setup(bot):
    bot.add_cog(Greetings(bot))