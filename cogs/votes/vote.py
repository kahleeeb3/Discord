import discord
from discord.ext import commands
from itertools import cycle


class Votes(commands.Cog):
    """Initiates a vote for group decision"""

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
    
    @commands.command()
    async def vote(self, ctx, vote, choice1, choice2):
        court_soup_id= 768896233359802408
        court_soup = ctx.guild.get_channel(court_soup_id)

        vote_message = await court_soup.send(f'> {vote}\n> **1)** {choice1}\n > **2)** {choice2}')
        await vote_message.add_reaction("1️⃣")
        await vote_message.add_reaction("2️⃣")

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
    client.add_cog(Votes(client))
