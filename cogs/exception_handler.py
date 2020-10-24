import traceback
import sys
import discord
from discord.ext import commands
import Constants as consts

class Exception_handler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        ignored = (commands.CommandNotFound, )

        # Ignoring these exceptions
        if isinstance(error, ignored):
            return None

        # handeling for disabled exception
        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')


        # handeling for bot missing permssions exception
        if isinstance(error, commands.BotMissingPermissions):

            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]

            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)

            _message = 'I need the **{}** permission(s) to run this command.'.format(fmt)

            await ctx.send(_message)
            return None


        # handeling for user misssing permissions exception
        if isinstance(error, commands.MissingPermissions):

            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]

            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)

            _message = 'You need the **{}** permission(s) to use this command.'.format(fmt)

            await ctx.send(_message)
            return None

        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(str(error.__cause__))
            return None


        # handeling for check failure exception
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You do not have permission to use this command.")
            return None

        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"To many arguments were passed.\nUse `{consts.PREFIX}help`")
            return None

        if isinstance(error, commands.BadArgument):
            await ctx.send("Bad arguments were passed")
            return None

        # ignore all other exception types, but print them to console
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(client):
    client.add_cog(Exception_handler(client))
