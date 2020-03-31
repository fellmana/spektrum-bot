from discord.ext import commands
import json

class Sitz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hitta', help='Hitta en sång i sångboken')
    async def _find(self, ctx, *, song: str):
        with open('utils/index.json') as f:
            index = json.load(f)
        if song in index.keys():
            await ctx.send(f'{song} är på sida: {index[song]}', tts=True)
        else:
            await ctx.send(f'Hittade inte sången ...', tts=True)

    @commands.command(name='lista', help='Lista alla sånger som börjar på en bokstav')
    async def _songs(self, ctx, *, letter: str):
        with open('utils/index.json') as f:
            index = json.load(f)
        songs = []
        for song in index.keys():
            if letter.lower().strip() in song[0].lower():
                songs.append(song)   
        if songs:     
            await ctx.send('\n'.join(songs))
        else:
            await ctx.send('Märklig bokstav 🤔', tts=True)

    @commands.command(name='text', help='Få texten till en sång (BETA)')
    async def _lyrics(self, ctx, *, song: str):
        with open('utils/index.json') as f:
            index = json.load(f)

        found = False
        lyrics = []
        with open('utils/sangbok.txt') as f:
            for line in f:
                if song in line:
                    found = True
                if found:
                    if line.strip() in index.keys() and line.strip() != song:
                        break
                    lyrics.append(line)
        if lyrics:
            await ctx.send(' '.join(lyrics), tts=True)
        else:
            await ctx.send(f'Hittade inte sången ...', tts=True)

def setup(bot):
    bot.add_cog(Sitz(bot))
