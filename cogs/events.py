from discord.ext import commands
from utils.censoring import BAD, SKETCHY

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
        
        for word in SKETCHY:
            if word in message.content.lower():
                await message.add_reaction('👀')
        
        for word in BAD:
            if word in message.content.lower():
                await message.delete()

        if 'grattis' in message.content.lower():
            await message.channel.send('Grattis! 🎈🎉')

    

def setup(bot):
    bot.add_cog(Events(bot))