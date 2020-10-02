import time
import discord
from discord.ext import commands, tasks
import Constants as consts

class Moderation(commands.Cog, commands.MemberConverter):
    def __init__(self, client):
        self.client = client
        self.muted_members = []
        #self.server = self.client.get_guild(consts.SERVER_ID)
        self.mute_role = None
        self.main_moderation_loop.start()


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

            if member:
                try:
                    await member.kick(reason=_reason)
                    await ctx.send(f"Kicked **{member}**.\nReason : **{_reason}**")
                    return True

                except:
                    await ctx.send(f"Failed to kick {member}.")
                    return False

            await ctx.send(f"Member as **'{_member}'** was not found.")
            return False

        except:
            await ctx.send("Please give a valid member.")
            return False


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, _member=None, *, _reason="No reason specified."):
        '''Bans the specified user'''

        if _member == None:
            await ctx.send("Please provide a user as well.")
            return False

        try:
            member_id = int(_member[:-1][2:])
            member = ctx.guild.get_member(member_id)

            if member:
                try:
                    await member.ban(reason=_reason)
                    await ctx.send(f"Banned **{member}**.\nReason : **{_reason}**")
                    return True

                except:
                    await ctx.send(f"Failed to ban {member}.")
                    return False

            await ctx.send(f"Member as **'{_member}'**' was not found.")
            return False

        except:
            await ctx.send("Please give a valid member.")
            return False


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


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, _member=None, _hours=None, *, _reason="No reason specified."):
        '''Mute Members'''

        # Getting Mute Role
        if self.mute_role == None:
            self.mute_role = discord.utils.get(ctx.guild.roles, id=consts.ROLE_IDS["MUTE_ROLE_ID"])

        if _member == None:
            await ctx.send("Please provide a member as well.")
            return False

        # Getting Member
        member = None
        try:
            member_id = int(_member[:-1][2:])
            member = ctx.guild.get_member(member_id)
            if member == None:
                await ctx.send(f"No member as **'{_member}'** was found.")
                return False

        except:
            await ctx.send("Please provide a valid member.")
            return False

        # Converting to Hours
        if _hours == None:
            _hours = -1

        else:
            try:
                _hours = int(_hours)
            except:
                await ctx.send("Please provide time in numbers (hours)")
                return False

        try:
            await member.add_roles(self.mute_role)
        except:
            await ctx.send(f"Failed to mute {member.mention}")
            return False

        if _hours <= 0:
            await ctx.send(f"Muted {member.mention} indefinitely.\nReason : **{_reason}**")

        else:
            await ctx.send(f"Muted {member.mention} for {_hours} hours.\nReason : **{_reason}**")
            self.muted_members.append({"member" : member, "time" : time.perf_counter(), "for" : _hours*3600})
            (self.muted_members)

        return True


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, _member=None, *, _reason="No reason specified."):
        '''Unute Members'''

        # Getting Mute Role
        if self.mute_role == None:
            self.mute_role = discord.utils.get(ctx.guild.roles, id=consts.ROLE_IDS["MUTE_ROLE_ID"])

        if _member == None:
            await ctx.send("Please provide a member as well.")
            return False

        # Getting Member
        member = None
        try:
            member_id = int(_member[:-1][2:])
            member = ctx.guild.get_member(member_id)
            if member == None:
                await ctx.send(f"No member as **'{_member}'** was found.")
                return False

        except:
            await ctx.send("Please provide a valid member.")
            return False

        try:
            await member.remove_roles(self.mute_role)
            await ctx.send(f"Unmuted {member} successfully.")
            return True
        except:
            await ctx.send(f"Failed to unmute {member}.")
            return False


    @tasks.loop(seconds=10.0)
    async def main_moderation_loop(self):
        # Getting Mute Role
        if self.mute_role == None:
            self.mute_role = discord.utils.get(self.client.get_guild(consts.SERVER_ID).roles, id=consts.ROLE_IDS["MUTE_ROLE_ID"])

        for muted_member in self.muted_members:
            if time.perf_counter() - muted_member["time"] >= muted_member["for"]:
                await muted_member["member"].remove_roles(self.mute_role)
                self.muted_members.remove(muted_member)


    @main_moderation_loop.before_loop
    async def before_main_moderation_loop(self):
        await self.client.wait_until_ready()



def setup(client):
    client.add_cog(Moderation(client))
