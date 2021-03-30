import discord
from discord.ext import commands
from itertools import cycle
import random
from modules import lists


async def sendGif(self,ctx, link):
    embed = discord.Embed()
    embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
    embed.set_image(url = link)

    await ctx.send(embed=embed)

class Gifs(commands.Cog):
    """A series of commands to send GIFS"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def yes(self, ctx):
        """Send the 'yes' gif"""
        await sendGif(self, ctx, 'https://media1.tenor.com/images/79f8be09f39791c6462d30c5ce42e3be/tenor.gif?itemid=18386674')

    @commands.command()
    async def no(self, ctx):
        """Send the 'yes' gif"""
        await sendGif(self, ctx, 'https://media2.giphy.com/media/W2zOnQonnYsNXnUxXo/giphy.gif')

    @commands.command()
    async def nice(self, ctx):
        """Send the 'yes' gif"""
        await sendGif(self, ctx, 'https://thumbs.gfycat.com/CoordinatedEnergeticChipmunk-size_restricted.gif')

    @commands.command()
    async def gif(self, ctx):
        await ctx.message.delete()
        await sendGif(self, ctx, 'https://media1.tenor.com/images/636ee91868d5b1602feed8e61afb62c0/tenor.gif?itemid=14720138')

    @commands.command()
    async def gifr(self, ctx):       

        gifs = lists.read('gifs')

        await ctx.message.delete()
        await ctx.send(f'{random.choice(gifs)}')

    @commands.command()
    async def gifra(self, ctx, link):
        def add(file_name,new_info):
            a_file = open(f'/home/pi/Desktop/Discord/modules/lists/{file_name}.txt', "a")
            a_file.write(f'{new_info}\n')
            a_file.close()
                
        gifs = lists.to_string('gifs')
        await ctx.message.delete()

        if link in gifs:
            await ctx.send('Already in the list')
        else:
            add('gifs',link)
            await ctx.send('Added to list')

def setup(client):
    client.add_cog(Gifs(client))