import discord
from discord.ext import commands
import random


class MemeReactions(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        async def send_dm():
            allowed = 'CalebP'
            member = message.author
            if member.name in allowed:
                #print(f'{user.name} laughed at your message')
                channel = await member.create_dm()
                await channel.send(f'{user.name} laughed at your message')
        
        async def check_previous():
            async for message in channel.history(limit = 1):
                if(message.author.id == 689673863008747553):
                    await message.edit(content= f'{message.content},  {user.mention}' )
                    alert = await channel.send('new laugh')
                    await alert.delete()
                else:
                    await channel.send(f'I very much like your meme {message.author.mention} \n - {user.mention}')

        



        #emoji id's
        LUL = 689621350511542374
        correct_Channel = 768896247288561725
        channel_id = payload.channel_id

        if (channel_id == correct_Channel):
            emoji_id = payload.emoji.id
            # For testing
            #if payload.emoji.name == '😂':
            # For server
            if emoji_id == LUL:
                channel = self.client.get_channel(channel_id)
                message_id = payload.message_id
                message = await channel.fetch_message(message_id)
                user_id = payload.user_id
                user = self.client.get_user(user_id)
                #await check_previous()
                await send_dm()
        


    



def setup(client):
    client.add_cog(MemeReactions(client))
