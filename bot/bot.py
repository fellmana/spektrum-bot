"""
bot.py
====================================
The core module of my example project
"""

from discord.ext import commands
from utils.environment import TOKEN

def get_prefix(bot, message):
    """
    A callable prefix for the bot separeted into guilds and DM's

    Parameters
    ----------
    your_name
        A string indicating the name of the person.
    """

    prefixes = ['spektrumiter ', '!']

    if not message.guild:
        return '!'

    return commands.when_mentioned_or(*prefixes)(bot, message)

extensions = ['cogs.events',
              'cogs.commands',
              'cogs.greetings',
              'cogs.svammel',
              'cogs.music',
              'cogs.wolfram']

bot = commands.Bot(command_prefix=get_prefix, description='Spektrum Discord Bot 🤖')

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

bot.run(TOKEN, bot=True, reconnect=True)
