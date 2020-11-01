import discord
from discord.ext import commands
import Constants as consts

class Others_member_count(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.channel = None

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def update_member_count(self, ctx):
        '''update member count command'''

        if self.channel == None:
            self.channel = self.client.get_channel(consts.CHANNEL_IDS["MEMBERS"])

        _c = await self.count_total_members()
        await self.channel.edit(name=f"Members : {_c}")

    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        '''this will update the member count when a members joins'''

        if self.channel == None:
            self.channel = self.client.get_channel(consts.CHANNEL_IDS["MEMBERS"])

        _c = await self.count_total_members()
        await self.channel.edit(name=f"Members : {_c}")

    @commands.Cog.listener()
    async def on_member_remove(self, ctx):
        '''this will update the member count when a member leaves'''

        if self.channel == None:
            self.channel = self.client.get_channel(consts.CHANNEL_IDS["MEMBERS"])

        _c = await self.count_total_members()
        await self.channel.edit(name=f"Members : {_c}")


    async def count_total_members(self):
        _count = 0
        for i in self.channel.guild.members:
            if not i.bot:
                _count += 1
        return _count
       
def setup(client):
    client.add_cog(Others_member_count(client))
