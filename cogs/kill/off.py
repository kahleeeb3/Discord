import discord
from discord.ext import commands


class Kill(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def off(self, ctx):
        exit()
        


def setup(client):
    client.add_cog(Kill(client))
