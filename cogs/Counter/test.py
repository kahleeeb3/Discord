import discord
from discord.ext import commands
from modules.json import json


class Test(commands.Cog):
    """IM drunk and dont want to mess things up"""

    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def test(self, ctx):
        data = json.load('test')

def setup(client):
    client.add_cog(Test(client))

