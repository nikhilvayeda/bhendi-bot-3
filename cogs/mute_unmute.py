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
    async def mute(self, ctx, _member : discord.Member=None, _hours=None, *, _reason="No reason specified."):
        '''Mute Members'''

        # Getting Mute Role
        if self.mute_role == None:
            self.mute_role = discord.utils.get(ctx.guild.roles, id=consts.ROLE_IDS["MUTE_ROLE_ID"])

        if _member == None:
            await ctx.send("Please provide a member as well.")
            return False

        # Getting Member
        if not isinstance(_member, discord.member.Member):
            await ctx.send("Couldn't find the member")
            return False


        # Converting to Hours
        if _hours == None:
            _hours = -1

        else:
            try:
                _hours = float(_hours)
            except:
                await ctx.send("Please provide time in numbers (hours)")
                return False

        await _member.add_roles(self.mute_role)


        if _hours <= 0:
            await ctx.send(f"Muted {_member.mention} indefinitely.\nReason : **{_reason}**")

        else:
            await ctx.send(f"Muted {_member.mention} for {_hours} hours.\nReason : **{_reason}**")
            self.muted_members.append({"member" : _member, "time" : time.perf_counter(), "for" : _hours*3600})

        return True


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, _member : discord.Member=None, *, _reason="No reason specified."):
        '''Unmute Members'''

        # Getting Mute Role
        if self.mute_role == None:
            self.mute_role = discord.utils.get(ctx.guild.roles, id=consts.ROLE_IDS["MUTE_ROLE_ID"])

        if _member == None:
            await ctx.send("Please provide a member as well.")
            return False

        # Getting Member
        if not isinstance(_member, discord.member.Member):
            await ctx.send("Couldn't find the member")
            return False


        await _member.remove_roles(self.mute_role)
        await ctx.send(f"Unmuted {_member} successfully.")

        for i in self.muted_members:
            if i["member"].id == _member.id:
                self.muted_members.remove(i)
                break;

        return True



    @tasks.loop(seconds=10.0)
    async def unmute_loop(self):
        # Getting Mute Role
        if self.mute_role == None:
            self.mute_role = discord.utils.get(self.client.get_guild(consts.SERVER_ID).roles, id=consts.ROLE_IDS["MUTE_ROLE_ID"])

        # Unmuting muted members if the time has arrived.
        for muted_member in self.muted_members:
            if time.perf_counter() - muted_member["time"] >= muted_member["for"]:
                try:
                    await muted_member["member"].remove_roles(self.mute_role)
                except:
                    pass
                self.muted_members.remove(muted_member)


    @unmute_loop.before_loop
    async def before_unmute_loop(self):
        await self.client.wait_until_ready()


    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        '''This will overwrite the permissions of mute role when a new channel is created'''

        # Getting Mute Role
        if self.mute_role == None:
            self.mute_role = discord.utils.get(self.client.get_guild(consts.SERVER_ID).roles, id=consts.ROLE_IDS["MUTE_ROLE_ID"])


        # Overwriting the permissions of mute role
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        await channel.set_permissions(self.mute_role, overwrite=overwrite)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        '''If a muted member leaves and joins back again'''

        # Getting Mute Role
        if self.mute_role == None:
            self.mute_role = discord.utils.get(self.client.get_guild(consts.SERVER_ID).roles, id=consts.ROLE_IDS["MUTE_ROLE_ID"])


        for muted_member in self.muted_members:
            if muted_member['member'].id == member.id:
                await member.add_roles(self.mute_role)
                break;


def setup(client):
    client.add_cog(Moderation_mute_unmute(client))
