import discord
from discord.ext import commands
import time
import platform
import requests

class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.started = time.perf_counter()
        self.stats = f"Discordpy : **{discord.__version__}**\n"\
                    f"Python Version : **3.7.2**\n"\
                    f"Platform : **{platform.platform()}**\n"\
                    f"System : **{platform.system()}**\n"\
                    f"Processor : **{platform.processor()}**\n"\
                    f"Architecture : **{platform.architecture()}**\n"\
                    f"Machine : **{platform.machine()}**\n"\

        self.api_url = "https://api.github.com/repos/nikhilvayeda/bhendi-bot-3"

    @commands.command()
    async def ping(self, ctx):
        '''Shows the latency.'''
        await ctx.send(f'Latency: **{round(self.client.latency * 1000)}** ms')

    @commands.command()
    async def stats(self, ctx):
        '''System Stats'''

        _live_stats = f"**__Stats__**\n\nUptime : **{round(time.perf_counter() - self.started)}s**\nLatency: {round(self.client.latency * 1000)} ms\n"
        await ctx.send(_live_stats + self.stats)


    @commands.command()
    async def github(self, ctx):
        '''Guthub status'''

        _res = requests.get(self.api_url)

        if _res.status_code == 200:
            _json_data = _res.json()
            _main_str = f"**Url** : {_json_data['html_url']}\n**Size** : {_json_data['size']}\n**Stars** : {_json_data['stargazers_count']}\n"\
                    f"**Watchers** : {_json_data['watchers_count']}\n**Forks** : {_json_data['forks_count']}"

            await ctx.send(_main_str)
            return True

        await ctx.send("Failed to retrieve data from github.")


def setup(client):
    client.add_cog(Utilities(client))
