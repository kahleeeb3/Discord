import discord
from discord.ext import commands
import random


class Horny(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands

    @commands.command()
    async def horny(self, ctx, victim):
        message = ctx.message
        guild = message.guild

        async def check_for_role():
            exists = False

            # if role already exists:
            # return the role
            for roles in guild.roles:
                if roles.name == 'Horny Ass':
                    #print('Role exists already')
                    exists = True
                    role = roles

            # If the role does not exist:
            # Create it!
            if (exists is False):
                role = await guild.create_role(name = 'Horny Ass', hoist = True)
                all_roles = await guild.fetch_roles()
                num_roles = len(all_roles)
                #print(f'The server has {num_roles} roles')
                await role.edit(reason = None, colour = 16711680, position = num_roles-2)
                #print('created new role')

            return role
            

        # runs the checks for role function
        role = await check_for_role()
        #print(role)

        # did the command mention everyone?
        # Yes:
        if message.mention_everyone:
            #print("You picked everyone")
            async for x in message.guild.fetch_members(limit=100):
                #print(x)
                await x.add_roles(role)
            await message.channel.send(f'You have been bad boys. Take it to #Horny-Soup')
        # No:
        else:
            victim = message.mentions
            for x in victim:
                await x.add_roles(role)
                await message.channel.send(f'You have been a bad boy, {x.mention}. Take it to #Horny-Soup')



def setup(client):
    client.add_cog(Horny(client))
