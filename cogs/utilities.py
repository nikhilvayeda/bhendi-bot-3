import discord
from discord.ext import commands

class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    #ping
        
    @commands.command()
    async def ping(self, ctx):
        '''Shows the latency.'''
        await ctx.send(f'Latency: {round(self.client.latency * 1000)} ms')  
         
def setup(client):
    client.add_cog(Utilities(client))
