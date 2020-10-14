import discord
from discord.ext import commands
from Constants import PREFIX

class Moderation_purge(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.older_than_2weeks_message = "No messages deleted, make sure messages aren't over two weeks old."
        self.link_types = ["https://", "http://"]
        self.DELETING = False

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, *args):
        '''Purge Messages'''

        if self.DELETING:
            await ctx.send("A purge is in progress, calm down.")
            return False

        if args == None:
            await ctx.send(f"Use `{PREFIX}help purge`to see a help message.")
            return False

        _number = None
        try:
            _number = int(args[-1])
            if not (_number + 1) in range(1, 1002):
                await ctx.send("Number of messages should be in between `0` and `1000`")
                return False

        except:
            await ctx.send(f"Please provide the number of messages to delete.\n"\
                           f"Use `{PREFIX}help purge` for a help message.")
            return False


        # Purging all messages
        if len(args) == 1 and args[0] == args[-1]:
            try:
                self.DELETING = True
                await ctx.message.delete()
                _deleted = await ctx.channel.purge(limit=_number)
                self.DELETING = False
            except:
                await ctx.send("Failed to delete messages.")
                return False

            if len(_deleted) > 0:
                await ctx.send(f"Deleted {len(_deleted)} messages.", delete_after=3.0)
            else:
                await ctx.send(self.older_than_2weeks_message)

            return True


        # Purging messages: if by bots
        if args[0] == "bot":
            try:
                self.DELETING = True
                await ctx.message.delete()
                _deleted = await ctx.channel.purge(limit=_number, check=self.check_bot)
                self.DELETING = False

            except:
                await ctx.send("Failed to delete messages.")
                return False

            if len(_deleted) > 0:
                await ctx.send(f"Deleted {len(_deleted)} messages.", delete_after=3.0)
            else:
                await ctx.send(self.older_than_2weeks_message)

            return True


        # Purging messages: if by humans
        elif args[0] == "human":
            try:
                self.DELETING = True
                await ctx.message.delete()
                _deleted = await ctx.channel.purge(limit=_number, check=self.check_human)
                self.DELETING = False

            except:
                await ctx.send("Failed to delete messages.")
                return False

            if len(_deleted) > 0:
                await ctx.send(f"Deleted {len(_deleted)} messages.", delete_after=3.0)
            else:
                await ctx.send(self.older_than_2weeks_message)

            return True


        # Purging messages: by a certain user
        elif args[0] == "user":
            if len(args) == 3:
                try:
                    member_id = int(args[1][:-1][2:])
                    member = ctx.guild.get_member(member_id)

                    if member:
                        try:
                            self.deleting_member = member
                            self.DELETING = True
                            await ctx.message.delete()
                            _deleted = await ctx.channel.purge(limit=_number, check=self.check_user)
                            self.DELETING = False

                            if len(_deleted) > 0:
                                await ctx.send(f"Deleted {len(_deleted)} messages.", delete_after=3.0)
                            else:
                                await ctx.send(self.older_than_2weeks_message)


                        except Exception as e:
                            print(e)
                            await ctx.send(f"Failed to delete messages.")
                            return False

                except:
                    await ctx.send(f"Please provide a valid user.")
                    return False


        # Purging messages: if contains embed
        elif args[0] == "embeds":
            try:
                self.DELETING = True
                await ctx.message.delete()
                _deleted = await ctx.channel.purge(limit=_number, check=self.check_embed)
                self.DELETING = False

                if len(_deleted) > 0:
                    await ctx.send(f"Deleted {len(_deleted)} messages.", delete_after=3.0)
                else:
                    await ctx.send(self.older_than_2weeks_message)

            except:
                await ctx.send("Failed to delete messages.")
                return False


        # Purging messages: if contains attachments
        elif args[0] == "images":
            try:
                self.DELETING = True
                await ctx.message.delete()
                _deleted = await ctx.channel.purge(limit=_number, check=self.check_attachments)
                self.DELETING = False

                if len(_deleted) > 0:
                    await ctx.send(f"Deleted {len(_deleted)} messages.", delete_after=3.0)
                else:
                    await ctx.send(self.older_than_2weeks_message)

            except:
                await ctx.send("Failed to delete messages.")
                return False


        # Purging messages: if contains mentions
        elif args[0] == "mentions":
            try:
                self.DELETING = True
                await ctx.message.delete()
                _deleted = await ctx.channel.purge(limit=_number, check=self.check_mentions)
                self.DELETING = False

                if len(_deleted) > 0:
                    await ctx.send(f"Deleted {len(_deleted)} messages.", delete_after=3.0)
                else:
                    await ctx.send(self.older_than_2weeks_message)

            except:
                await ctx.send("Failed to delete messages.")
                return False


        # Purging messages: if contains mentions
        elif args[0] == "links":
            try:
                self.DELETING = True
                await ctx.message.delete()
                _deleted = await ctx.channel.purge(limit=_number, check=self.check_links)
                self.DELETING = False

                if len(_deleted) > 0:
                    await ctx.send(f"Deleted {len(_deleted)} messages.", delete_after=3.0)
                else:
                    await ctx.send(self.older_than_2weeks_message)

            except:
                await ctx.send("Failed to delete messages.")
                return False

        else:
            await ctx.send(f"wdym by **{args[0]}**??\nUse  `{PREFIX}help purge`")


    def check_bot(self, _m):
        return _m.author.bot

    def check_human(self, _m):
        return not _m.author.bot

    def check_user(self, m):
        return self.deleting_member.id == m.author.id

    def check_embed(self, m):
        return len(m.embeds)

    def check_attachments(self, m):
        return len(m.attachments)

    def check_mentions(self, m):
        return max(len(m.raw_mentions), len(m.raw_role_mentions))

    def check_links(self, m):
        for i in self.link_types:
            if i in m.content:
                return True
        return False


def setup(client):
    client.add_cog(Moderation_purge(client))
