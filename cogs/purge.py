import discord
from discord.ext import commands
from Constants import PREFIX

class Moderation_purge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def purge(self, ctx, *args):
        '''Purge Messages'''

        if args == None:
            await ctx.send(f"Use `{PREFIX}help purge`to see a help message.")
            return False

        _number = None
        try:
            _number = int(args[-1]) + 1
            if not _number in range(1, 1002):
                await ctx.send("Number of messages should be in between `0` and `1000`")
                return False

        except:
            await ctx.send(f"Please provide the number of messages to delete.\n"\
                           f"Use `{PREFIX}help purge` for a help message.")
            return False


        # Purging all messages
        if len(args) == 1 and args[0] == args[-1]:
            try:
                await ctx.message.delete()
                _deleted = await ctx.channel.purge(limit=_number)
            except:
                await ctx.send("Failed to delete messages.")
                return False

            if len(_deleted) > 0:
                await ctx.send(f"Deleted {len(_deleted) - 1} messages.", delete_after=3.0)
            else:
                await ctx.send(f"Couldn't find any messages which is not older than 2 weeks.", delete_after=3.0)

            return True

        # Purging messages: if by bots
        if args[0] == "bot":
            try:
                await ctx.message.delete()
                _deleted = await ctx.channel.purge(limit=_number, check=self.check_bot)
            except:
                await ctx.send("Failed to delete messages.")
                return False

            await ctx.send(f"Deleted {len(_deleted) - 1} messages.", delete_after=3.0)


        # Purging messages: if by humans
        elif args[0] == "human":
            try:
                await ctx.message.delete()
                _deleted = await ctx.channel.purge(limit=_number, check=self.check_human)
            except:
                await ctx.send("Failed to delete messages.")
                return False

            await ctx.send(f"Deleted {len(_deleted)} messages.", delete_after=3.0)


        else:
            await ctx.send(f"wdym by **{args[0]}**??\nUse  `{PREFIX}help purge`")


    def check_bot(self, _m):
        return _m.author.bot

    def check_human(self, _m):
        return not _m.author.bot

def setup(client):
    client.add_cog(Moderation_purge(client))

