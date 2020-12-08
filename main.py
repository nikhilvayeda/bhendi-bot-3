import os
import sys
import discord
from discord.ext import commands
import Constants as consts


# Instances
client = commands.Bot(command_prefix=consts.PREFIX, case_insensitive=True)
client.remove_command("help")


@client.event
async def on_ready():
    print("[Bhendi Bot 3.0] Ready...")


# To load cogs
@client.command()
async def load(ctx, extension=None):
    if int(ctx.author.id) in consts.DEVS_IDS and extension is not None:
        if str(extension) in consts.ALL_EXTENSIONS:

            try:
                client.load_extension(f"cogs.{extension}")
                print(f"[Bhendi Bot 3.0] Loaded : {extension}")
                await ctx.send(f"Loaded the {extension} Cog")

            except Exception as e:
                print(f"[Bhendi Bot 3.0] Failed to load : {extension}")
                print(f"[Bhendi Bot 3.0] ERROR : {e}")


# To unload cogs
@client.command()
async def unload(ctx, extension=None):
    if int(ctx.author.id) in consts.DEVS_IDS and extension is not None:
        if str(extension) in consts.ALL_EXTENSIONS:

            try:
                client.unload_extension(f"cogs.{extension}")
                print(f"[Bhendi Bot 3.0] Unloaded : {extension}")
                await ctx.send(f"Unloaded the {extension} Cog")

            except Exception as e:
                print(f"[Bhendi Bot 3.0] Failed to unload : {extension}")
                print(f"[Bhendi Bot 3.0] ERROR : {e}")


# To reload cogs
@client.command()
async def reload(ctx, extension=None):
    await unload(ctx, extension)
    await load(ctx, extension)


# This will block all the dms
@client.check
async def globally_block_dms(ctx):
    return ctx.guild is not None

# This will block all the messages by bots
@client.check
async def disable_bot_messages(ctx):
    return not ctx.author.bot


# Loading all the cogs in the starting
for filename in os.listdir(os.path.join(os.getcwd(), "cogs")):
    if filename.endswith(".py") and filename[:-3] in consts.ALL_EXTENSIONS:
        client.load_extension(f"cogs.{filename[:-3]}")


# Running
client.run(consts.BOT_TOKEN, reconnect=True)
