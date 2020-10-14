import discord
from discord.ext import commands, tasks

class Moderation_kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, _member : discord.Member=None, *, _reason="No reason specified."):
        '''kicks the specified user'''

        if _member == None:
            await ctx.send("Please provide a user as well.")
            return False

        elif isinstance(_member, discord.member.Member):
            await _member.send(f"You have been kicked from the server **{ctx.guild}**\nReason : **{_reason}**")
            await _member.kick(reason=_reason)
            await ctx.send(f"Kicked **{_member}**.\nReason : **{_reason}**")
            return True

        await ctx.send("Couldn't find the member.")
        return False


def setup(client):
    client.add_cog(Moderation_kick(client))