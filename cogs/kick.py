import discord
from discord.ext import commands, tasks

class Moderation_kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, _member=None, *, _reason="No reason specified."):
        '''kicks the specified user'''

        if _member == None:
            await ctx.send("Please provide a user as well.")
            return False

        try:
            member_id = int(_member[:-1][2:])
            member = ctx.guild.get_member(member_id)

            if member == None:
                try:
                    member = ctx.guild.get_member(int(_member))
                except:
                    await ctx.send("Please provide a valid member")
                    return False

            if member:
                try:
                    await member.send(f"You have been kicked from the server **{ctx.guild}**\nReason : **{_reason}**")
                    await member.kick(reason=_reason)
                    await ctx.send(f"Kicked **{member}**.\nReason : **{_reason}**")
                    return True

                except :
                    await ctx.send(f"Failed to kick {member}.")
                    return False

            await ctx.send(f"Member as **'{_member}'** was not found.")
            return False

        except:
            await ctx.send("Please give a valid member.")
            return False


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(f"Failed. {error}")



def setup(client):
    client.add_cog(Moderation_kick(client))