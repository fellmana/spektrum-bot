import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random

class Sing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = 'https://support.discordapp.com/hc/en-us/articles/212517297-Text-to-Speech-101'

    @commands.command(name='tts', help='Hjälp med att aktivera text-to-speech')
    async def _svammel(self, ctx):
        await message.channel.send(f'Hjälp med tts: {url}', tts=True)


def setup(bot):
    bot.add_cog(Sing(bot))