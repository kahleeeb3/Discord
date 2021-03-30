import discord
from discord.ext import commands
import random


class Horny(commands.Cog):
    """Labels a memeber horny in the chat""" 

    def __init__(self, client):
        self.client = client

    # commands

    @commands.command(aliases = ['h'])
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

    @commands.command(aliases = ['nh'])
    async def nothorny(self, ctx, victim):

        message = ctx.message
        guild = message.guild
        role = discord.utils.get(guild.roles, name ='Horny Ass')
        role2 = discord.utils.get(guild.roles, name ='Super Horny')


        async def empty_role(role):

            if not role.members:
                await role.delete()

        async def remove(message,role):
            if message.mention_everyone:
                for x in role.members:
                    await x.remove_roles(role)
            else:
                victim = message.mentions
                for x in victim:
                    #if user is horny, remove
                    if role in x.roles:
                        await x.remove_roles(role)

        if role != None:
            await remove(message,role)
            await empty_role(role)
        if role2 != None:
            await remove(message,role2)
            await empty_role(role2)

        if message.mention_everyone:
            await message.channel.send(f'Group Ejaculation!!!')

    @commands.command(aliases= ['sh'] )
    async def superhorny(self, ctx, victim):
        message = ctx.message
        guild = message.guild

        async def check_for_role():
            exists = False

            # if role already exists:
            # return the role
            for roles in guild.roles:
                if roles.name == 'Super Horny':
                    #print('Role exists already')
                    exists = True
                    role = roles

            # If the role does not exist:
            # Create it!
            if (exists is False):
                role = await guild.create_role(name = 'Super Horny', hoist = True)
                all_roles = await guild.fetch_roles()
                num_roles = len(all_roles)
                #print(f'The server has {num_roles} roles')
                await role.edit(reason = None, colour = 16711897, position = num_roles-2)
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
            await message.channel.send(f'You have been bad boys. Take it to <#768896248903368725>')
        # No:
        else:
            victim = message.mentions
            for x in victim:
                await x.add_roles(role)
                await message.channel.send(f'{x.mention} is down bad boys. Take him to the <#768896248903368725>')



def setup(client):
    client.add_cog(Horny(client))
