import discord
from discord.ext import commands
from itertools import cycle
import random


class Bullshit(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bullshit(self, ctx):
        await ctx.send('**The Dr.Brown**:tm: says: *bullshit*')
        


def setup(client):
    client.add_cog(Bullshit(client))
