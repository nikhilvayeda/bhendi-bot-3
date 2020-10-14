import discord
from discord.ext import commands

class Moderation_ban(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, _member : discord.Member=None, *, _reason="No reason specified."):
        '''Bans the specified user'''

        if _member == None:
            await ctx.send("Please provide a user as well.")
            return False

        elif isinstance(_member, discord.member.Member):
            await _member.send(f"You have been banned from the server **{ctx.guild}**\nReason : **{_reason}**")
            #await _member.ban(reason=_reason)
            await ctx.send(f"Banned **{_member}**.\nReason : **{_reason}**")
            return True

        await ctx.send("Couldn't find the member.")
        return False


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.CommandNotFound):
            return None
        print(f"Error in BAN. {error}")


def setup(client):
    client.add_cog(Moderation_ban(client))