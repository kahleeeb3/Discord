import discord
from discord.ext import commands
from discord.utils import get
import random


class Reactions(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        votes_to_pass = 4
        court_id = 768896233359802408

        school_roles =["Ad Lab","Electronics", "Complex, Anal Si","E&M","Theory of Programming Languages"]
        punish_roles =["Commoners", "Shunned", "Shame"]

        async def get_roles():
            role_dict={}
            for role in message.guild.roles:
                if role.name in school_roles:
                    role_dict[f'{role.name}'] = role
                elif role.name in punish_roles:
                    role_dict[f'{role.name}'] = role

            return role_dict
        
        #get information about where the reaction was added
        async def get_reaction_information():
            #print('Getting Reaction Information...')

            # get the id values from payload
            channel_id = payload.channel_id
            message_id = payload.message_id

            #get objects from the id's
            channel = self.client.get_channel(channel_id)
            message = await channel.fetch_message(message_id)

            #check the channel
            return (channel, message)

        #checks for the right channel
        def check_channel():
            if (payload.channel_id == court_id):
                return True
            else:
                return False
                

        #gets the victim of the vote
        async def get_victim():
            #print('finding the victim')
            for mentions in message.mentions:
                mentioned = mentions.id
            async for people in message.guild.fetch_members(limit=100):
                if(people.id == mentioned):
                    victim = people
                    return victim

        # checks the vote count
        async def check_vote():

            for reaction in message.reactions:
                # checks if enough votes have passed
                if reaction.count == votes_to_pass:
                    return (True, reaction)
            return (False, 'null')

        async def determine_punish():
            if reaction.emoji == "🛑":
                await punish("Shame")
            if reaction.emoji == "⚠":
                await punish("Shun")
            if reaction.emoji == "🔁":
                await punish("Revive")

        
        async def punish(punishment):
            Commoners = roles["Commoners"]
            Shame = roles["Shame"]
            Shun = roles["Shunned"]
            
            if punishment == "Shame":
                print(f'Shamming {victim}')
                await victim.remove_roles(Commoners)
                await victim.add_roles(Shame)
                await message.delete()
                await message.channel.send(f'{Shame.mention} upon you {victim.mention}. You have been removed from **COMMONERS.**')
                voteRevive = await message.channel.send(f'4 Votes to Revive {victim.mention}')
                await voteRevive.add_reaction('🔁')

            elif punishment == "Shun":
                #print(f'Shunning {victim}')
                for x in roles:
                    await victim.remove_roles(roles[x])
                await victim.add_roles(Shun)
                await message.delete()
                await message.channel.send(f'{victim.mention} has been {Shun.mention}')
                voteRevive = await message.channel.send(f'4 Votes to Revive {victim.mention}')
                await voteRevive.add_reaction('🔁')
            
            elif punishment == "Revive":
                #print(f'Revivng {victim}')
                await victim.remove_roles(Shame, Shun)
                await victim.add_roles(Commoners)
                await message.delete()
                await message.channel.send(f'You have been **Revived** {victim.mention}')

            
        if(check_channel()):
            reaction_info = await get_reaction_information()
            channel = reaction_info[0]
            message = reaction_info[1]
            votes_to_pass_reached = await check_vote()
            if(votes_to_pass_reached[0]):
                reaction = votes_to_pass_reached[1]
                victim = await get_victim()
                roles = await get_roles()
                await determine_punish()

def setup(client):
    client.add_cog(Reactions(client))
