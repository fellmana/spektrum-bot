from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random


class Svammel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = 'https://spektrum.fi/spektraklet/svammel/'

    @commands.command(name='svammel', help='Hmm ...')
    async def _svammel(self, ctx):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        content = soup.find(class_='entry-content')
        paragraphs = content.find_all('p')
        svammel = [p.get_text() for p in paragraphs]

        response = random.choice(svammel)
        await ctx.send(response)


def setup(bot):
    bot.add_cog(Svammel(bot))
