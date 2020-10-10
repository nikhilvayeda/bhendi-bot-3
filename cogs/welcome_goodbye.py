import discord
from discord.ext import commands
import Constants as consts

class Others_welcome_goodbye(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.channel = None


    @commands.Cog.listener()
    async def on_member_join(self, member):
        '''when a member joins the server'''

        if self.channel == None:
            self.channel = self.client.get_channel(consts.CHANNEL_IDS["WELCOME_GOODBYE"])

        _total_member = self.count_total_members()

        _embed = discord.Embed(title="New Member!", color=discord.Colour.blue())
        _embed.add_field(name=f"Hello", value=f"""Hello {member.mention}!({member}), Welcome to Say Station. \n
Be sure to read the rules in <#{consts.CHANNEL_IDS['RULES']}>. Go have a chat with the members in <#{consts.CHANNEL_IDS['GENERAL']}>""" )
        _embed.add_field(name="Member Count", value=f"#{_total_member + 1} members")
        _embed.set_image(url="https://cdn.discordapp.com/attachments/722370864229646377/733302632977924146/image0.gif")

        await self.channel.send(member.mention, embed=_embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        '''when a member leaves the server'''

        if self.channel == None:
            self.channel = self.client.get_channel(consts.CHANNEL_IDS["WELCOME_GOODBYE"])

        _total_member = self.count_total_members()

        _embed = discord.Embed(title=f"{member} has left the server. Can we get some F please", color=discord.Colour.red())
        _embed.set_image(url="https://cdn.discordapp.com/attachments/729979069248176162/731784988009168906/image0.gif")

        await self.channel.send(embed=_embed)


    def count_total_members(self):
        return len([m for m in self.channel.guild.members if not m.bot])


def setup(client):
    client.add_cog(Others_welcome_goodbye(client))
