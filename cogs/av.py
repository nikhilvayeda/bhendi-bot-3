import discord
from discord.ext import commands

class Utility_av(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def av(self, ctx, user : discord.Member=None):
        '''avatar command'''

        if user == None:
            _embed = discord.Embed(title=f"{ctx.author}", color=discord.Colour.blue())
            _embed.set_image(url=ctx.author.avatar_url)

            await ctx.send(ctx.author.mention, embed=_embed)
            return True

        else:
            if isinstance(user, discord.member.Member):
                _embed = discord.Embed(title=f"{user}", color=discord.Colour.blue())
                _embed.set_image(url=user.avatar_url)

                await ctx.send(ctx.author.mention, embed=_embed)
                return True

            await ctx.send(f"Couldn't find the user as **{user}**")


def setup(client):
    client.add_cog(Utility_av(client))