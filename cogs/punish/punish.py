import discord
from discord.ext import commands
import asyncio
import random
from itertools import cycle


class Punish(commands.Cog):

    def __init__(self, client):
        self.client = client


    # commands
    @commands.command()
    async def punish(self, ctx, victim, *, reason):


        channel_id = 768896233359802408
        channel = ctx.guild.get_channel(channel_id)


        vote_message = await channel.send(f'> Vote to Cancel {victim} for {reason}: \n **Shame** - 🛑 \n **Shun** - ⚠ \n **Undo** - 🔁')
        #add the reactions
        await vote_message.add_reaction('🛑')
        await vote_message.add_reaction('⚠')
        await vote_message.add_reaction('🔁')
            


def setup(client):
    client.add_cog(Punish(client))
