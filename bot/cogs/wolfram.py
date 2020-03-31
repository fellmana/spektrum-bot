from discord.ext import commands
import wolframalpha
from utils.environment import get_app_id


class Ruben(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='ruben', aliases=['wolfram'], help='Sök fakta eller lös svåra matteproblem')
    async def _wolfram_alpha(self, ctx, *, query: str):
        client = wolframalpha.Client(get_app_id())

        res = client.query(query)

        if res['@success'] == 'true':
            response = next(res.results).text
        else:
            response = f'Inga resultat för {query}'
        await ctx.send(response)


def setup(bot):
    bot.add_cog(Ruben(bot))
