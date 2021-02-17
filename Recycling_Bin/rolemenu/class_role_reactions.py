import discord
from discord.ext import commands
import random


class ClassRoleReactions(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        # define the guild
        guild_id = payload.guild_id
        guild = self.client.get_guild(guild_id)
        # defines the channel this command runs in
        role_channel_id = 811501154230992926

        async def get_emoji_list():
            ross = await get_emoji('ross')
            brown = await get_emoji('excellent')
            chad = await get_emoji('chad')
            tard = await get_emoji('Spongetard')
            joe = await get_emoji('joe')

            reactions = (chad, brown, ross, tard, joe)

            return reactions

        async def get_emoji(name):
            for emoji in guild.emojis:
                if emoji.name == name:
                    return emoji

        async def get_role_object(role_name):
            role = discord.utils.get(message.guild.roles, name = role_name)
            return role
        
        async def get_role():
            if(emoji == emoji_list[0]):
                role = await get_role_object('Complex, Anal Si')

            if(emoji == emoji_list[1]):
                role = await get_role_object('Electronics')

            if(emoji == emoji_list[2]):
                role = await get_role_object('E&M')

            if(emoji == emoji_list[3]):
                role = await get_role_object('Theory of Programming Languages')

            if(emoji == emoji_list[4]):
                role = await get_role_object('Ad Lab')
                
            await user.add_roles(role)
                #print(f'{user.name} is now in {role.name}')

        async def check_emoji():
            if(emoji in emoji_list):
                await get_role()
            else:
                await message.remove_reaction(payload.emoji, user)
                error = await channel.send(f'That was not a choice {user.mention}')
                await error.delete(delay = 3)

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

    
        
        # this is the main code
        # check if reaction was added to the right channel
        correct_channel = await check_channel()
        if correct_channel == 'true':

            # get a list of all the reactions
            emoji_list = await get_emoji_list()

            reaction_info = await get()

            channel = reaction_info['channel']
            message = reaction_info['message']
            user = reaction_info['user']
            emoji = reaction_info['emoji']

            # check for the emoji added
            await check_emoji()


    



def setup(client):
    client.add_cog(ClassRoleReactions(client))