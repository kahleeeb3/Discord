import discord
from discord.ext import commands
from itertools import cycle
import random


class Suggestions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        suggestions_id= 768896230423265281
        suggestion_channel = ctx.guild.get_channel(suggestions_id)

        suggest_message = await suggestion_channel.send(f'{suggestion}')
        await suggest_message.add_reaction("✅")
        await suggest_message.add_reaction("❌")
        await suggest_message.add_reaction("❔")
        


def setup(client):
    client.add_cog(Suggestions(client))
