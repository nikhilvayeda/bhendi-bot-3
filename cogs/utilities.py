import discord
from discord.ext import commands

class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    #ping
        
    @commands.command()
    async def ping(self, ctx):
      ```Shows the latency.```
      
        try:
            await ctx.send(f'Latency: {round(self.client.latency * 1000)} ms')
            
        except Exception as e:
            print(e)
            await ctx.send("An Error has been logged.")


def setup(client):
    client.add_cog(Utilities(client))
