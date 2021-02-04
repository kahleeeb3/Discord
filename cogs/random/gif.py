import discord
from discord.ext import commands
from itertools import cycle
import random


class Gif(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gif(self, ctx):
        await ctx.message.delete()
        await ctx.send('https://tenor.com/view/emma-waston-emma-watson-hot-emma-watson-sexy-pin-hair-gif-14720138')
        


def setup(client):
    client.add_cog(Gif(client))
