from discord.ext import commands
from utils.censoring import get_bad_words, get_sketchy_words

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print(f'user:\t{self.bot.user}')
        print(f'id:\t{self.bot.user.id}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        msg = message.content.lower()

        for word in get_sketchy_words():
            if word in msg:
                await message.add_reaction('👀')
        
        for word in get_bad_words():
            if word in msg:
                await message.delete()

        if 'grattis' in msg:
            await message.channel.send('Grattis! 🎈🎉', tts=True)

        if 'eif' in msg:
            await message.add_reaction('🏆')
    

def setup(bot):
    bot.add_cog(Events(bot))