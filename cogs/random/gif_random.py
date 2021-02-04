import discord
from discord.ext import commands
import random
from itertools import cycle


class GifRandom(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands
    
    @commands.command()
    async def gifr(self, ctx):
        channel_id = 771763970054684672
        channel = ctx.guild.get_channel(channel_id)
        

        gifs = ['https://tenor.com/view/emma-waston-emma-watson-hot-emma-watson-sexy-pin-hair-gif-14720138',
        'https://tenor.com/view/dancing-tongue-out-partying-emma-watson-gif-13970287',
        'https://tenor.com/view/emma-watson-uhh-ok-freak-out-gif-4800433',
        'https://tenor.com/view/emma-watson-wtf-shocked-face-surprised-gif-13845931',
        'https://tenor.com/view/emma-watson-smirk-gif-8685396',
        'https://media.tenor.com/images/55b2fb28afd438d1433b342ac17f10cb/tenor.gif',
        'https://media.tenor.com/images/523ac706056c955541799c7022732caa/tenor.gif',
        'https://media.tenor.com/images/911b7bddf4998de8ead0fbfa59004741/tenor.gif',
        'https://media.tenor.com/images/136b2feb14661016757edcd0aa3f692c/tenor.gif',
        'https://media.tenor.com/images/2e2dbf262e78af2c3f7f02fad38dc13b/tenor.gif',
        'https://tenor.com/view/emma-watson-gif-7891041',
        'https://tenor.com/view/emma-watson-interview-head-shake-no-gif-7918236',
        'https://media.tenor.com/images/6f7351f616ac3054c3dc9ed5ead2ef22/tenor.gif',
        'https://media.tenor.com/images/4d60eb77c942d948942cbe69bd90bdf0/tenor.gif',
        'https://media.tenor.com/images/f33e7a8e62c10b1da86f4a37cac7e6a3/tenor.gif',
        'https://media.tenor.com/images/86143f640fc98afbd75acd3b570d5520/tenor.gif',
        'https://tenor.com/view/qwer-sexy-inviting-mature-provocative-gif-13376780']

        gifr_message = await channel.send(f'{random.choice(gifs)}')
        await ctx.message.delete()

def setup(client):
    client.add_cog(GifRandom(client))
