import discord
from discord.ext import commands


class Random(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clean(self,ctx, amount:int):
        deleted= await ctx.channel.purge(limit = amount+1) #clears the messages + the command message
        cleanMessage = await ctx.send(f'Cleared {len(deleted)-1} messages') #returns the number of messages deleted minus the command message
        await cleanMessage.delete(delay = 3)

        



def setup(client):
    client.add_cog(Random(client))
