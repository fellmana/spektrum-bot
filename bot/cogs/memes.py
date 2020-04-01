import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import json


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='meme', help='Random')
    async def _meme(self, ctx):
        await ctx.message.add_reaction('🐸')
        url = 'https://meme-api.herokuapp.com/gimme'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        site_json=json.loads(soup.text)
        e = discord.Embed()
        e.set_image(url=site_json['url'])
        await ctx.send(embed=e)

    @commands.command(name='fyssa', help='pi=3')
    async def _physics(self, ctx):
        await ctx.message.add_reaction('🖖')
        url = 'https://meme-api.herokuapp.com/gimme/physicsmemes'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        site_json=json.loads(soup.text)
        e = discord.Embed()
        e.set_image(url=site_json['url'])
        await ctx.send(embed=e)

    @commands.command(name='mafs', help='1+2+3+...=-1/12')
    async def _maths(self, ctx):
        await ctx.message.add_reaction('➗')
        url = 'https://meme-api.herokuapp.com/gimme/mathmemes'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        site_json=json.loads(soup.text)
        e = discord.Embed()
        e.set_image(url=site_json['url'])
        await ctx.send(embed=e)

    @commands.command(name='dank', help='420')
    async def _dank(self, ctx):
        await ctx.message.add_reaction('🆘')
        url = 'https://meme-api.herokuapp.com/gimme/dankmemes'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        site_json=json.loads(soup.text)
        e = discord.Embed()
        e.set_image(url=site_json['url'])
        await ctx.send(embed=e)

    @commands.command(name='gegga', help='60°10\'15.2\"N 24°57\'22.6\"E')
    async def _geography(self, ctx):
        await ctx.message.add_reaction('🌍')
        url = 'https://meme-api.herokuapp.com/gimme/geographymemes'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        site_json=json.loads(soup.text)
        e = discord.Embed()
        e.set_image(url=site_json['url'])
        await ctx.send(embed=e)

    @commands.command(name='cs', help='01100011 01110011')
    async def _cs(self, ctx):
        await ctx.message.add_reaction('👩‍💻')
        url = 'https://meme-api.herokuapp.com/gimme/ProgrammerHumor'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        site_json=json.loads(soup.text)
        e = discord.Embed()
        e.set_image(url=site_json['url'])
        await ctx.send(embed=e)

    @commands.command(name='kemist', help='H2O + H2O = H4O')
    async def _chemistry(self, ctx):
        await ctx.message.add_reaction('🧪')
        url = 'https://meme-api.herokuapp.com/gimme/chemistrymemes'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        site_json=json.loads(soup.text)
        e = discord.Embed()
        e.set_image(url=site_json['url'])
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Memes(bot))
