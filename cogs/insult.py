import json
import requests
import discord
from discord.ext import commands

class Fun_insult(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def insult(self, ctx):
        '''insult command'''

        _res = requests.get(url='https://evilinsult.com/generate_insult.php?lang=en&type=json')

        if _res.status_code == 200:
            try:
                _data = _res.json()
                _insult = _data['insult']

            except:
                return False

            _embed = discord.Embed(color=0x42c42b, title=_insult)
            _embed.set_author(name='Bhendi Bot')
            _embed.set_thumbnail(url='https://media.giphy.com/media/2pjspMQCi70k/giphy.gif')

            await ctx.send(ctx.author.mention, embed=_embed)


def setup(client):
    client.add_cog(Fun_insult(client))

