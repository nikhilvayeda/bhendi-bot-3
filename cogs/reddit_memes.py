import discord
from discord.ext import commands, tasks
import praw
import Constants as consts

class Others_reddit_memes(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.channel = None
        self.ALL_MEMES = []
        self.MEME_COUNT = 0
        self.RES = praw.Reddit(client_id=consts.REDDIT_KEY, client_secret=consts.REDDIT_SECRET,
            user_agent="bhendi")

        self.update_memes()
        self.send_meme.start()

    @tasks.loop(minutes=10.0)
    async def send_meme(self):

        if self.MEME_COUNT >= 144:
            self.update_memes()

        if self.channel == None:
            self.channel = self.client.get_channel(consts.CHANNEL_IDS["REDDIT_MEMES"])

        _current_meme = self.ALL_MEMES[self.MEME_COUNT]
        self.MEME_COUNT += 1

        _embed = discord.Embed(title="Reddit Review", color=discord.Colour.blue())
        _embed.add_field(name='Author', value=f"[u/{_current_meme['author']}]({_current_meme['author_profile']})")
        _embed.add_field(name="Post", value=f"[{_current_meme['post_title']}]({_current_meme['post_link']})")
        _embed.set_image(url=_current_meme['image_url'])

        await self.channel.send(embed=_embed)


    @send_meme.before_loop
    async def before_send_meme(self):
        await self.client.wait_until_ready()

    def update_memes(self):

        for i in self.RES.subreddit("SaimanSays").hot(limit=200):

            if str(i.url).endswith(("jpg", "png", "jpeg", "gif", "webp")):
                _meme = {'author' : i.author, 'author_profile' : f"https://www.reddit.com/u/{i.author}"
                , "image_url" : i.url,"post_title" : i.title,
                "post_link" : f"https://reddit.com{i.permalink}"}

                self.ALL_MEMES.append(_meme)

        self.MEME_COUNT = 0



def setup(client):
    client.add_cog(Others_reddit_memes(client))
