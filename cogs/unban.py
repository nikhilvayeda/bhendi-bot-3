import discord
from discord.ext import commands

class Moderation_unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, _member=None, *, _reason="No reason specified."):
        '''Unbans the specified user'''

        if _member == None:
            await ctx.send("Please provide a user as well.")
            return False

        _banned_users = await ctx.guild.bans()
        _member_name = _member.split('#')[0]
        _member_no = _member.split('#')[-1]

        for ban_member in _banned_users:
            user = ban_member.user
            if user.name == _member_name and user.discriminator == _member_no:
                try:
                    await ctx.guild.unban(user, reason=_reason)
                    await ctx.send(f"Unbanned **{user.name}#{user.discriminator}**\nReason : **{_reason}**")
                    return True

                except Exception as e:
                    await ctx.send(f"Failed to unban **'{user.name}#{user.discriminator}.'**")
                    return False

        await ctx.send(f"No banned user found as **'{_member}'**")
        return False


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.CommandNotFound):
            return None
        print(f"Error in unban. {error}")



def setup(client):
    client.add_cog(Moderation_unban(client))
