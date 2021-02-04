import discord
from discord.ext import commands
import asyncio
import os


class Memes(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands

    @commands.command()
    async def dump(self, ctx,folder):
        path = f'/Users/Caleb/OneDrive - Wabash College/Memes/{folder}'
        for filename in os.listdir(path):
            file = discord.File(f'{path}/{filename}', filename=f'{filename}')
            await ctx.send(file=file)


def setup(client):
    client.add_cog(Memes(client))
