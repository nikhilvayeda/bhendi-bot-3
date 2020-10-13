import requests
import json
import discord
from discord.ext import commands
import Constants as consts

class Other_counters(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.temp_total_counteded = {"bruh" : 0, "nice" : 0}
        nice_list = ['nice', 'naice', 'nais', 'noice']
        bruh_list = ['bruh', 'bruhh', 'bruuh', 'bruuhh']
        self.all_words_list = [bruh_list, nice_list]
        self.counted_words = ['bruh', 'nice']
        self.counters_ = ['bruh_counter', 'nice_counter']
        self.total_counted = {"bruh" : self.get_total_word_counted(0), "nice" : self.get_total_word_counted(1)}


    @commands.Cog.listener()
    async def on_message(self, message):
        _index_of_word_counted = self.check_counted_words_present(str(message.content).lower())
        if _index_of_word_counted != None:

            _word_counted = self.counted_words[_index_of_word_counted]
            self.temp_total_counteded[_word_counted] += 1
            self.total_counted[_word_counted] += 1

            if self.temp_total_counteded[_word_counted] >= 20:
                self.update_database(_index_of_word_counted, self.total_counted[self.counted_words[_index_of_word_counted]])
                self.temp_total_counteded[_word_counted] = 0


    @commands.command()
    async def total(self, ctx, *, word):
        ''' to check the number of counts'''
        if str(word).lower() in self.counted_words:
            await ctx.send(f"Total {word} counted : {self.total_counted[str(word.lower())]}")
            return True

        await ctx.send(f"No counter as {word} was found.")

    def get_total_word_counted(self, word_index):
        _counter = self.counters_[word_index]

        _gotvalue = False
        while not _gotvalue:
            _res = requests.get(f"{consts.DREAMLO_URL}/json")
            if _res.status_code == 200:
                try:
                    _total = json.loads(_res.text)
                    _gotvalue = True
                except Exception as e:
                    print("Failed to get value")

        for _counted in _total['dreamlo']['leaderboard']['entry']:
            if _counted["name"] == _counter:
                return int(_counted['score'])

        return None


    def update_database(self, word_index, value):
        _counter = self.counters_[word_index]
        _status_code_a = 0
        while _status_code_a != 200:
            _status_code_a = requests.get(f"{consts.DREAMLO_URL}/delete/{_counter}").status_code

        _status_code_b = 0
        while _status_code_b != 200:
            _status_code_b = requests.get(f"{consts.DREAMLO_URL}/add/{_counter}/{value}").status_code


    def check_counted_words_present(self, message):
        _message_list = str(message).split(' ')

        if len(_message_list) == 1:
            for i, _list in enumerate(self.all_words_list):
                if message in _list:
                    return i
        else:
            for _message_item in _message_list:
                for i, _list in enumerate(self.all_words_list):
                    if _message_item in _list:
                        return i

        return None

def setup(client):
    client.add_cog(Other_counters(client))
