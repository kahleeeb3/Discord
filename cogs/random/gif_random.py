import discord
from discord.ext import commands
import random
from itertools import cycle
from modules import lists


class GifRandom(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands
    
    @commands.command()
    async def gifr(self, ctx):       

        gifs = lists.read('gifs')

        await ctx.message.delete()
        await ctx.send(f'{random.choice(gifs)}')

    @commands.command()
    async def gifra(self, ctx, link):
        def add(file_name,new_info):
            a_file = open(f'./modules/lists/{file_name}.txt', "a")
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
    client.add_cog(GifRandom(client))
