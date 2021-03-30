import discord
from discord.ext import commands
from itertools import cycle
import random
from modules import lists


class Random(commands.Cog):
    """A series of commands meant for random fun"""

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

def setup(client):
    client.add_cog(Random(client))
