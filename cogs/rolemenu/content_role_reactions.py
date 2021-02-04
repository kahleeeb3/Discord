import discord
from discord.ext import commands
import random


class ClassRoleReactions(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        # defines the channel this command runs in
        role_channel_id = 770018703697772596
        court_id = 768896233359802408
        suggest_channel_id = 768896230423265281
        # defines the role's emoji's
        emoji_list = ["🖥","😂","🐶","🙌","🗳"]

        async def get_role_object(role_name):
            role = discord.utils.get(message.guild.roles, name = role_name)
            return role
        
        async def get_role():
            if(emoji.name == emoji_list[0]):
                role = await get_role_object('CSC Stuff')
                await user.add_roles(role)

            if(emoji.name == emoji_list[1]):
                role = await get_role_object('Memes')
                await user.add_roles(role)

            if(emoji.name == emoji_list[2]):
                role = await get_role_object('Pets')
                await user.add_roles(role)

            if(emoji.name == emoji_list[3]):
                await vote_to_join_commoners()

            if(emoji.name == emoji_list[4]):
                await vote_to_join_admins()
                
                #print(f'{user.name} is now in {role.name}')

        async def check_emoji():
            if(emoji.name in emoji_list):
                await get_role()
            else:
                await message.remove_reaction(payload.emoji, user)
                error = await channel.send(f'That was not a choice {user.mention}')
                await error.delete(delay = 5)

        async def get():
            channel = self.client.get_channel(payload.channel_id)
            message_id = payload.message_id
            message = await channel.fetch_message(message_id)
            user = payload.member
            emoji = payload.emoji
            return {'channel': channel, 'message': message, 'user': user, 'emoji': emoji}

        async def check_channel():
            channel_id = payload.channel_id
            if (channel_id == role_channel_id):
                return 'true'
                # check if the right reaction was added

        async def vote_to_join_commoners():
            court = self.client.get_channel(court_id)
            voteRevive = await court.send(f'{payload.member.mention} would like to join Commoners')
            await voteRevive.add_reaction('🔁')

        async def vote_to_join_admins():
            vote = self.client.get_channel(suggest_channel_id)
            suggest_message = await vote.send(f'Make {payload.member.mention} an admin')
            await suggest_message.add_reaction("✅")
            await suggest_message.add_reaction("❌")
            await suggest_message.add_reaction("❔")

        # this is the main code
        # check if reaction was added to the right channel
        correct_channel = await check_channel()
        if correct_channel == 'true':
            reaction_info = await get()

            channel = reaction_info['channel']
            message = reaction_info['message']
            user = reaction_info['user']
            emoji = reaction_info['emoji']

            # check for the emoji added
            await check_emoji()


    



def setup(client):
    client.add_cog(ClassRoleReactions(client))
