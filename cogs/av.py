import discord
from discord.ext import commands

class Utility_av(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def av(self, ctx, user=None):
        '''avatar command'''

        if user == None:
            _embed = discord.Embed(title=f"{ctx.author}", color=discord.Colour.blue())
            _embed.set_image(url=ctx.author.avatar_url)

            await ctx.send(ctx.author.mention, embed=_embed)
            return True

        else:
            member_id = int(user[:-1][2:])
            member = ctx.guild.get_member(member_id)

            if member:
                _embed = discord.Embed(title=f"{member}", color=discord.Colour.blue())
                _embed.set_image(url=member.avatar_url)

                await ctx.send(ctx.author.mention, embed=_embed)
                return True

            else:
                member = ctx.guild.get_member(int(user))
                if member:
                    _embed = discord.Embed(title=f"{member}", color=discord.Colour.blue())
                    _embed.set_image(url=member.avatar_url)

                    await ctx.send(ctx.author.mention, embed=_embed)
                    return True

            await ctx.send(f"Couldn't find the user as **{user}**")


def setup(client):
    client.add_cog(Utility_av(client))