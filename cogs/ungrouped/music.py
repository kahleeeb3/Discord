import discord
from discord.ext import commands
from discord import Spotify


class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def music(self,ctx):
        user = ctx.author
        for activity in user.activities:
            if isinstance(activity, Spotify):
                await ctx.send(f'{ctx.author.mention}:\nhttps://open.spotify.com/track/{activity.track_id}')
        await ctx.message.delete()

        



def setup(client):
    client.add_cog(Music(client))
