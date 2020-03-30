import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def get_prefix(bot, message):
    """A callable prefix for the bot separeted into guilds and DM's"""

    prefixes = ['spektrumiter ', '!']

    if not message.guild:
        return '!'

    return commands.when_mentioned_or(*prefixes)(bot, message)

extensions = ['cogs.events',
              'cogs.commands',
              'cogs.greetings',
              'cogs.svammel']

bot = commands.Bot(command_prefix=get_prefix, description='Spektrum Discord Bot 🤖')

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

bot.run(TOKEN, bot=True, reconnect=True)
