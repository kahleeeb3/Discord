import discord
from discord.ext import commands


class Clean(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clean(self,ctx, amount:int):
        await ctx.channel.purge(limit=amount+1)
        cleanMessage = await ctx.send(f'Cleared {amount} messages')
        await cleanMessage.delete(delay = 3)

        



def setup(client):
    client.add_cog(Clean(client))
