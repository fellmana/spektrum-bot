from discord.ext import commands


class Sitz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = 'https://support.discordapp.com/hc/en-us/articles/212517297-Text-to-Speech-101'

    @commands.command(name='tts', help='Hjälp med att aktivera text-to-speech')
    async def _svammel(self, ctx):
        await ctx.send(f'Hjälp med tts: {self.url}', tts=True)


def setup(bot):
    bot.add_cog(Sitz(bot))
