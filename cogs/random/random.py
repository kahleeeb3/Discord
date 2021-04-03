import discord
from discord.ext import commands
from itertools import cycle
import random
from modules import lists
import pickle


class Random(commands.Cog):
    """A series of commands meant for random fun"""

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == False and 'yikes' in message.content.lower():
            await message.channel.send('Thats a big fucking yikes right there.')

        if message.author.bot == False and 'emma' in message.content.lower():

            responses = [
                'Books! And cleverness! There are more important things! — Friendship! And Bravery!',
                'It means “dirty blood.” Mudblood’s a foul name for someone who’s Muggle-born. Someone with non-magic parents. Someone like me. It’s not a term one usually hears in civilized conversation.',
                'One person can’t feel all that at once, they’d explode.',
                'It would be quite nice if you stopped jumping down out throats, Harry, because in case you haven’t noticed, Ron and I are on your side.',
                'A warmth was spreading through him that had nothing to do with the sunlight; a tight obstruction in his chest seemed to be dissolving. He knew that Ron and Hermione were more shocked than they were letting on, but the mere fact that they were still there on either side of him, speaking bracing words of comfort, not shrinking from him as though he were contaminated or dangerous, was worth more than he could ever tell them.',
                'I mean, it’s sort of exciting isn’t it? Breaking the rules.',
                'Fear of a name only increases fear of the thing itself.',
                'I’m hoping to do some good in the world!',
                'I mean, you could claim that anything’s real if the only basis for believing in it is that nobody’s proved it doesn’t exist!',
                'Just because you have the emotional range of a teaspoon doesn’t mean we all have!',
                'Next time there’s a ball, ask me before someone else does, and not as a last resort!',
                'Just because it’s taken you three years to notice, Ron, doesn’t mean no one else has spotted I’m a girl!',
                'Actually I’m highly logical which allows me to look past extraneous detail and perceive clearly that which others overlook.',
                'You know, the Egyptians used to worship cats.',
                'I checked this out weeks ago for a bit of light reading.',
                'No, Harry. Even in the wizarding world, hearing voices isn’t a good sign.',
                'Now if you two don’t mind, I’m going to bed before either of you come up with another clever idea to get us killed - or worse, expelled.',
                'Are you sure that’s a real spell? Well, it’s not very good, is it?',
                'What’s got your wand in a knot?',
                'Stop, stop, stop! You’re going to take someone’s eye out. Besides, you’re saying it wrong. It’s leviosa, not leviosar!',
                'Always the tone of surprise.',
                'Honestly, don’t you two read?'
            ]
            await message.channel.send(f'{random.choice(responses)}')
    
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
