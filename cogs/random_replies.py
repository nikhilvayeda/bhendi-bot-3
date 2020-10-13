import discord
from discord.ext import commands
import Constants as consts

class Other_random_replies(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if str(message.content).lower() in consts.RANDOM_REPLIES:
            await message.channel.send(consts.RANDOM_REPLIES[str(message.content).lower()])


def setup(client):
    client.add_cog(Other_random_replies(client))
