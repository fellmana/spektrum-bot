"""
bot.py
========================
Spektrum Bot core module
"""

import discord
from discord.ext import commands
from utils.environment import get_token

def get_prefix(bot, message):
    """
    A callable prefix for the bot separeted into guilds and DM's

    Parameters
    ----------
    bot
        commands.Bot
    message
        discord message
    """

    prefixes = ['spektrumiter ', '!']

    if not message.guild:
        return '!'

    return commands.when_mentioned_or(*prefixes)(bot, message)


extensions = ['cogs.events',
              'cogs.commands',
              'cogs.svammel',
              'cogs.music',
              'cogs.wolfram']

bot = commands.Bot(command_prefix=get_prefix,
                   description='Spektrum Discord Bot 🤖')

def get_embed(title, description, url):
    embed = (discord.Embed(title=title,
                           description=description,
                           color=discord.Color.blurple())
                    .add_field(name='url', value=url))
    return embed

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

    @bot.command(name='contribute', help='Add new parts to me')
    async def _contribute(ctx):
        title = 'Contribute'
        description = 'Fork me here 🍴'
        url = 'https://github.com/hd4niel/spektrum-bot'
        await ctx.send(embed=get_embed(title, description, url))

    @bot.command(name='documentation', help='Bot is feeling well documented')
    async def _documentation(ctx):
        title = 'Documentation'
        description = 'Read about me here 📖'
        url = 'https://hd4niel.github.io/spektrum-bot'
        await ctx.send(embed=get_embed(title, description, url))

    @bot.command(name='text-to-speech', help='I sometimes speak ;)')
    async def _documentation(ctx):
        title = 'Text to speech'
        description = 'Activate tts on Discord 🗣️'
        url = 'https://support.discordapp.com/hc/en-us/articles/212517297-Text-to-Speech-101'
        await ctx.send(embed=get_embed(title, description, url))        

    bot.run(get_token(), bot=True, reconnect=True)
