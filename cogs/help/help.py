import discord
from discord.ext import commands
from discord.errors import Forbidden

async def send_embed(ctx, embed):
    """
    Function that handles the sending of embeds
    -> Takes context and embed to send
    - tries to send embed in channel
    - tries to send normal message when that fails
    - tries to send embed private with information abot missing permissions
    If this all fails: https://youtu.be/dQw4w9WgXcQ
    """
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)


class Help(commands.Cog):
    """Sends this help message"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx, *input):
        # !SET THOSE VARIABLES TO MAKE THE COG FUNCTIONAL!
        prefix = '$' # ENTER YOUR PREFIX - loaded from config, as string or how ever you want!

        if not input:
            emb = discord.Embed(title=f'Commands:', color=discord.Color.blue())
            for cog in self.bot.cogs:
                commandName = ''
                # getting commands from cog
                for command in self.bot.get_cog(cog).get_commands():
                    # if cog is not hidden
                    if not command.hidden:
                        commandName = f'`{prefix}{command.name}` ' + commandName
                # Checks if the module has no commands
                if commandName != '':
                    #gets the cog description
                    cogs_desc = f'\n {self.bot.cogs[cog].__doc__}\n'
                    # adds the module with commands list
                    emb.add_field(name=f"**{cog}: ** {commandName}", value= cogs_desc, inline=False)
                    
        elif len(input) == 1:

            # iterating trough cogs
            for cog in self.bot.cogs:
            # getting commands from cog
                for command in self.bot.get_cog(cog).get_commands():
                    # check if cog is the matching one
                    if (command.name).lower() == input[0].lower():
                        print('match')
                        # making title - getting description from doc-string below class
                        emb = discord.Embed(title='Usage', description=self.bot.cogs[cog].__doc__,
                                            color=discord.Color.green())
                        emb.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                        break

            # if input not found
            # yes, for-loops have an else statement, it's called when no 'break' was issued
            """
            else:
                emb = discord.Embed(title="What's that?!",
                                    description=f"I've never heard from a module called `{input[0]}` before :scream:",
                                    color=discord.Color.orange())
            """

        # too many cogs requested - only one at a time allowed
        elif len(input) > 1:
            emb = discord.Embed(title="That's too much.",
                                description="Please request only one module at once :sweat_smile:",
                                color=discord.Color.orange())

        await send_embed(ctx, emb)

def setup(bot):
    bot.add_cog(Help(bot))