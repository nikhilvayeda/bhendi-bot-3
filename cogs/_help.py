import discord
from discord.ext import commands
from Constants import SUB_COMMANDS_TEXT, SUB_SUB_COMMANDS_TEXT

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.SUB_COMMANDS = [i.lower() for i in SUB_COMMANDS_TEXT]
        self.SUB_SUB_COMMANDS  = [i.lower() for i in SUB_SUB_COMMANDS_TEXT]

        self.SUB_COMMANDS_EMBEDS = {}
        self.SUB_SUB_COMMANDS_EMBEDS = {}

        self.create_main_help_embed()
        self.create_sub_help_embeds()
        self.create_sub_sub_help_embeds()

    @commands.command()
    async def help(self, ctx, term=None):
        '''Main help command'''
        if term == None:
            _temp_embed = self.main_help_embed
            await ctx.send(embed=_temp_embed.set_footer(text=f"ordered by {ctx.author}",
                            icon_url=ctx.author.avatar_url))

        elif term.lower() in self.SUB_COMMANDS:
            _temp_embed = self.SUB_COMMANDS_EMBEDS[term.lower()]
            await ctx.send(embed=_temp_embed.set_footer(text=f"ordered by {ctx.author}",
                            icon_url=ctx.author.avatar_url))

        elif term.lower() in self.SUB_SUB_COMMANDS:
            _temp_embed = self.SUB_SUB_COMMANDS_EMBEDS[term.lower()]
            await ctx.send(embed=_temp_embed.set_footer(text=f"ordered by {ctx.author}",
                            icon_url=ctx.author.avatar_url))

        else:
            await ctx.send(f"No Sub Command such as **'{term}'** was found.")


    def create_main_help_embed(self):
        '''This function will Create the main help embeds in the starting'''
        self.main_help_embed = discord.Embed(title="**__Bhendi Bot 3__**", color=discord.Colour.blue())
        self.main_help_embed.add_field(name="**Fun**", value="Simple and Fun Commands", inline=False)
        self.main_help_embed.add_field(name="**Moderation**", value="Commands for Mods", inline=False)
        self.main_help_embed.add_field(name="**Utility**", value="Utility commands", inline=False)
        self.main_help_embed.add_field(name="**Help**", value="Incase you need help", inline=False)


    def create_sub_help_embeds(self):
        '''This function will create the sub command help embeds in the starting'''
        for _sub_command in SUB_COMMANDS_TEXT:
            _embed = discord.Embed(title=f"**__{_sub_command}__**", color=discord.Colour.blue())

            for _sub_sub_command in SUB_COMMANDS_TEXT[_sub_command]:
                _embed.add_field(name=f"**{_sub_sub_command}**", value=SUB_COMMANDS_TEXT[_sub_command][_sub_sub_command], inline=False)

            self.SUB_COMMANDS_EMBEDS[_sub_command.lower()] = _embed

    def create_sub_sub_help_embeds(self):
        '''This will create help embeds for each and ever command'''

        for _sub_sub_command in SUB_SUB_COMMANDS_TEXT:
            _embed = discord.Embed(title=f"**__{_sub_sub_command.title()}__**", color=discord.Colour.blue())

            for _each_commands in SUB_SUB_COMMANDS_TEXT[_sub_sub_command]:
                _embed.add_field(name=f"**{_each_commands}**", value=SUB_SUB_COMMANDS_TEXT[_sub_sub_command][_each_commands], inline=False)

            self.SUB_SUB_COMMANDS_EMBEDS[_sub_sub_command.lower()] = _embed




def setup(client):
    client.add_cog(Help(client))
