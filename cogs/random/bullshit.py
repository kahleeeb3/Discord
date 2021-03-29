import discord
from discord.ext import commands
from itertools import cycle
import random
from modules import lists


class Random(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def status(self, ctx, choice, *, new_status):

        status_type = discord.ActivityType.unknown
        
        if choice == 'w':
            # Setting 'watching' type
            status_type = discord.ActivityType.watching
        elif choice == 'p':
            # Setting 'play' type
            status_type = discord.ActivityType.streaming
        elif choice == 'l':
            # Setting 'listening' type
            status_type = discord.ActivityType.listening
        elif choice == 'c':
            # Setting 'competing in' type
            status_type = discord.ActivityType.competing            

        await self.client.change_presence(activity=discord.Activity(type = status_type, name = f'{new_status}') )
    
    @commands.command()
    async def shame(self, ctx, *, reason):
        await ctx.message.delete()
        await ctx.send(f'shame on {reason}')
    
    @commands.command()
    async def gif(self, ctx):
        await ctx.message.delete()
        await ctx.send('https://tenor.com/view/emma-waston-emma-watson-hot-emma-watson-sexy-pin-hair-gif-14720138')
    
    @commands.command()
    async def bullshit(self, ctx, description="This is the brief description"):
        await ctx.send('**The Dr.Brown**:tm: says: *bullshit*')
        
    @commands.command(aliases=['8ball', 'q', 'question'])
    async def _8ball(self, ctx, *, question):
        asker = ctx.message.author
        await ctx.message.delete()

        responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Reply hazy, try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes – definitely.',
                 'You may rely on it.']
        await ctx.send(f'`{asker} : {question}`\n*{random.choice(responses)}*')

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
    client.add_cog(Random(client))
