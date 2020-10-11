import discord
from discord.ext import commands
import Constants as consts

class Other_deleted_edited(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.deleted = []
        self.edited = []
        self.edited_embed = discord.Embed(title="__**Last Edited Messages**__", color=discord.Colour.blue())
        self.deleted_embed = discord.Embed(title="__**Last Deleted Messages**__", color=discord.Colour.blue())


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def deleted(self, ctx):
        '''deleted command'''

        _temp_deleted_embed = self.deleted_embed.copy()

        if len(self.deleted) > 0:
            for msg in self.deleted:
                _temp_deleted_embed.add_field(name=f"By {msg['author']}",
                    value=f'Message : **{msg["message"]}**\n¯\n_',
                    inline=False
                )

        else:
            _temp_deleted_embed.add_field(name="No message was deleted after I woke up", value="¯\\_(ツ)_/¯")

        await ctx.send(embed=_temp_deleted_embed)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def edited(self, ctx):
        '''edited command'''

        _temp_edited_embed = self.edited_embed.copy()
        if len(self.edited) > 0:
            for msg in self.edited:
                _temp_edited_embed.add_field(name=f"by {msg['author']}",
                    value=f"Original Message : {msg['message_before']}\nEdited Message : {msg['message_after']}\n¯\n_",
                    inline=False
                )

        else:
            _temp_edited_embed.add_field(name="No message was edited after I woke up", value="¯\\_(ツ)_/¯")

        await ctx.send(embed=_temp_edited_embed)


    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        '''will record deleted messages'''

        if payload.cached_message != None:
            if not payload.cached_message.author.bot and 0 < len(payload.cached_message.content) < 1024:
                _msg = {"author" : payload.cached_message.author, "message" : payload.cached_message.content}
                self.deleted.append(_msg)

                if len(self.deleted) > 5:
                    del self.deleted[0]


    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not before.author.bot:
            if 0 < len(before.content) < 1024 and 0 < len(after.content) < 1024:
                _msg = { "author" : before.author, "message_before" : before.content,
                "message_after" : after.content }

                self.edited.append(_msg)

                if len(self.edited) > 5:
                    del self.edited[0]


def setup(client):
    client.add_cog(Other_deleted_edited(client))
