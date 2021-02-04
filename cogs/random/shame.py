import discord
from discord.ext import commands
import random


class Shame(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands
    @commands.command()
    async def shame(self, ctx, *, reason):
        await ctx.message.delete()
        await ctx.send(f'shame on {reason}')


def setup(client):
    client.add_cog(Shame(client))
