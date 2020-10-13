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

        await self.channel.edit(name=f"Members : {self.count_total_members()}")


    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        '''this will update the member count when a members joins'''

        if self.channel == None:
            self.channel = self.client.get_channel(consts.CHANNEL_IDS["MEMBERS"])

        await self.channel.edit(name=f"Members : {self.count_total_members()}")


    @commands.Cog.listener()
    async def on_member_remove(self, ctx):
        '''this will update the member count when a member leaves'''

        if self.channel == None:
            self.channel = self.client.get_channel(consts.CHANNEL_IDS["MEMBERS"])

        await self.channel.edit(name=f"Members : {self.count_total_members()}")


    def count_total_members(self):
        return len([m for m in self.channel.guild.members if not m.bot])

def setup(client):
    client.add_cog(Others_member_count(client))
