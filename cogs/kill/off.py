import discord
from discord.ext import commands


class Kill(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def off(self, ctx):
        print(ctx.message.author.name)
        if ctx.message.author.name == 'CalebP':
            await ctx.channel.send(f'https://tenor.com/view/cry-sad-toy-story-woody-so-long-partner-gif-9797730')
            exit()
        else:
            await ctx.channel.send(f'Shut the fuck up {ctx.message.author.name}, you dont have the authority for that.')

    @commands.command()
    async def restart(self, ctx):
        import os
        os.system("sudo reboot")
        exit()
        


def setup(client):
    client.add_cog(Kill(client))
