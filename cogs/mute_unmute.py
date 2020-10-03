import time
import discord
from discord.ext import commands, tasks
import Constants as consts

class Moderation_mute_unmute(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.muted_members = []
        self.mute_role = None
        self.unmute_loop.start()


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

        return True


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, _member=None, *, _reason="No reason specified."):
        '''Unmute Members'''

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
    async def unmute_loop(self):
        # Getting Mute Role
        if self.mute_role == None:
            self.mute_role = discord.utils.get(self.client.get_guild(consts.SERVER_ID).roles, id=consts.ROLE_IDS["MUTE_ROLE_ID"])

        # Unmuting muted members if the time has arrived.
        for muted_member in self.muted_members:
            if time.perf_counter() - muted_member["time"] >= muted_member["for"]:
                await muted_member["member"].remove_roles(self.mute_role)
                self.muted_members.remove(muted_member)


    @unmute_loop.before_loop
    async def before_unmute_loop(self):
        await self.client.wait_until_ready()



def setup(client):
    client.add_cog(Moderation_mute_unmute(client))
