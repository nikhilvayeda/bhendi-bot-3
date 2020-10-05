import discord
from discord.ext import commands
import Constants as consts

class Utility_config(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.commands_channels = None

    @commands.command()
    async def all_channels(self, ctx):
        if self.commands_channels == None:
            self.commands_channels = [ctx.guild.get_channel(consts.CHANNEL_IDS["COMMANDS"]),
            ctx.guild.get_channel(consts.CHANNEL_IDS["BOT"])]

        if ctx.channel in self.commands_channels:

            _main_str = ""
            for i in ctx.guild.channels:
                _main_str += f"{i} : `{i.id}`\n"

            for i in self.split_string(_main_str):
                await ctx.send(i)
            return True

        await ctx.send(f"Please use this command in <#{self.commands_channels[0].id}>.")


    @commands.command()
    async def all_roles(self, ctx):
        if self.commands_channels == None:
            self.commands_channels = [ctx.guild.get_channel(consts.CHANNEL_IDS["COMMANDS"]),
            ctx.guild.get_channel(consts.CHANNEL_IDS["BOT"])]

        if ctx.channel in self.commands_channels:

            _main_str = ""
            for i in ctx.guild.roles:
                _main_str += f"`{i}` : `{i.id}`\n"

            for i in self.split_string(_main_str):
                await ctx.send(i)
            return True

        await ctx.send(f"Please use this command in <#{self.commands_channels[0].id}>.")

    @commands.command()
    async def all_emojis(self, ctx):
        if self.commands_channels == None:
            self.commands_channels = [ctx.guild.get_channel(consts.CHANNEL_IDS["COMMANDS"]),
            ctx.guild.get_channel(consts.CHANNEL_IDS["BOT"])]

        if ctx.channel in self.commands_channels:

            _main_str = ""
            for i in ctx.guild.emojis:
                _main_str += f"{i} : {i.id}\n"

            for i in self.split_string(_main_str):
                await ctx.send(i)

            return True

        await ctx.send(f"Please use this command in <#{self.commands_channels[0].id}>.")


    def split_string(self, _string):
        if len(_string) >= 1999:
            chunks, chunk_size = len(_string), 1999
            return [ _string[i:i+chunk_size] for i in range(0, chunks, chunk_size)]

        return [_string]



def setup(client):
    client.add_cog(Utility_config(client))
