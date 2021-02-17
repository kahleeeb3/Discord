import discord
from discord.ext import commands


class Pick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pick(self, ctx, pick):

        async def get_emoji(name):
            for emoji in ctx.guild.emojis:
                if emoji.name == name:
                    return emoji

        async def content(reactions):
            await ctx.message.delete()
            role_menu = await ctx.send(f"""
**Available Server Content**
React to get access to content
{reactions[0]} : `CSC Stuff`

{reactions[1]}  : `Memes`

{reactions[2]} : `Pet Photos`
            
{reactions[3]} : `Join Commoners`
            
{reactions[4]}  : `Request Admin`
            """)
            for emojis in reactions:
                await role_menu.add_reaction(emojis)
        
        async def Class(reactions):
            await ctx.message.delete()
            role_menu = await ctx.send(f"""
**Classes for the Semester**
React to give yourself the role
{reactions[0]} : `Complex Analysis`

{reactions[1]}  : `Electronics`

{reactions[2]} : `Electromagnetic Theory`
            
{reactions[3]} : `Theory of Programming Languages`
            
{reactions[4]}  : `Advanced Lab`
            """)
            for emojis in reactions:
                await role_menu.add_reaction(emojis)

        
        
        if pick == 'content':
            reactions = ("🖥","😂","🐶","🙌","🗳")
            await content(reactions)
        
        elif pick == 'class':

            ross = await get_emoji('ross')
            brown = await get_emoji('excellent')
            chad = await get_emoji('chad')
            tard = await get_emoji('Spongetard')
            joe = await get_emoji('joe')

            reactions = (chad, brown, ross, tard, joe)
            await Class(reactions)

        elif pick == "test":
            ross = await get_emoji('ross')
            brown = await get_emoji('excellent')
            chad = await get_emoji('chad')  
            await ctx.send(f' {ross} {brown} {chad}')



    
            

def setup(client):
    client.add_cog(Pick(client))
