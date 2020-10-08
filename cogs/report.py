import discord
from discord.ext import commands
import Constants as consts

class Utility_report(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.reports_channel = None
        self.green_tick_reaction = "\u2705"


    @commands.command()
    async def report(self, ctx, *, context=None):

        if context == None:
            await ctx.send("Please provide a context as well.")
            return False

        if self.reports_channel == None:
            self.reports_channel = ctx.guild.get_channel(consts.CHANNEL_IDS["REPORTS"])

        _embed = discord.Embed(title="New Report", color=discord.Colour.red())
        _embed.add_field(name="**Report :**", value=context, inline=False)
        _additonal_info = f"Channel : <#{ctx.channel.id}>\nMessage : [jump to context]({ctx.message.jump_url})"
        _embed.add_field(name="**Additonal info :**", value=_additonal_info, inline=False)
        _embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

        await self.reports_channel.send(embed=_embed)
        await ctx.message.add_reaction(self.green_tick_reaction)


def setup(client):
    client.add_cog(Utility_report(client))
