import discord
from discord.ext import commands
import time
import platform

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

    @commands.command()
    async def ping(self, ctx):
        '''Shows the latency.'''
        await ctx.send(f'Latency: **{round(self.client.latency * 1000)}** ms')

    @commands.command()
    async def stats(self, ctx):
        '''System Stats'''

        _live_stats = f"**__Stats__**\n\nUptime : **{round(time.perf_counter() - self.started)}s**\nLatency: {round(self.client.latency * 1000)} ms\n"
        await ctx.send(_live_stats + self.stats)


def setup(client):
    client.add_cog(Utilities(client))
