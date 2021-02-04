import discord
from discord.ext import commands
from itertools import cycle


class Votes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def vote(self, ctx, vote, choice1, choice2):
        court_soup_id= 768896233359802408
        court_soup = ctx.guild.get_channel(court_soup_id)

        vote_message = await court_soup.send(f'> {vote}\n> **1)** {choice1}\n > **2)** {choice2}')
        await vote_message.add_reaction("1️⃣")
        await vote_message.add_reaction("2️⃣")
        


def setup(client):
    client.add_cog(Votes(client))
