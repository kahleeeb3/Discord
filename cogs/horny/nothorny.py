import discord
from discord.ext import commands
import random


class NotHorny(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands

    @commands.command()
    async def nothorny(self, ctx, victim):
        message = ctx.message
        guild = message.guild

        async def users_horny():
            #print('checking if anyone is horny')
            # if nobody is horny:
            if not role.members:
                #print('nobody is horny')
                await role.delete()
            else:
                #print(f'{role.members}')
                pass

        
                
        role = discord.utils.get(guild.roles, name ='Horny Ass')

        if message.mention_everyone:
            #print("You picked everyone")
            async for x in message.guild.fetch_members(limit=100):
                #print(x)
                await x.remove_roles(role)
            await message.channel.send(f'Group Ejaculation!!!')
        else:
            victim = message.mentions
            for x in victim:
                await x.remove_roles(role)
                await message.channel.send(f'Dont worry guys, {x.mention} got off.')
        await users_horny()



def setup(client):
    client.add_cog(NotHorny(client))
