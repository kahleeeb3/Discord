import discord
from discord.ext import commands


class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        if( '$punish' in ctx.message.content):
            await ctx.send('`Usage: $punish <user> for <reason>`')

        if("$clean" in ctx.message.content):
            await ctx.send('`Usage: $clean <number of messages to delete>`')

        if("$shame" in ctx.message.content):
            await ctx.send('`Usage: $shame <user> <reason why>`')

        if("$horny" in ctx.message.content):
            await ctx.send('`Usage: $horny <user>`')

        if("$q" in ctx.message.content):
            await ctx.send('`Usage: $q <Question to Answer>`')
        
        if("$suggest" in ctx.message.content):
            await ctx.send('`Usage: $suggest <thing to suggest>`')

        if("$vote" in ctx.message.content):
            await ctx.send('`Usage: $vote <thing to vote on> <option 1> <option 2>`')

        if("$remind" in ctx.message.content):
            await ctx.send('`Usage: $remind <new/edit/list>`')

        else:
            await ctx.send(error)
            print(error)

        #if isinstance(error, commands.MissingRequiredArgument):
            #await ctx.send('please pass in all aquired arguments')
        """
        await ctx.send(f'Try using *$help* since you clearly dont know wtf you\'re doing \n`{error}`')


def setup(client):
    client.add_cog(Errors(client))






