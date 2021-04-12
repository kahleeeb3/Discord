import discord
from discord.ext import commands
from modules import lists, menus
from modules.json import json

"""
"Complex": "chad",
"Electronics": "excellent",
"E&M": "ross",
"Theory of Programming Languages": "Spongetard",
"Ad Lab": "joe"
"""

class RoleReactions(commands.Cog):
    """Sends the role menu to the chat"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rolemenu(self,ctx):
        # creates the embed
        embed = menus.get_embed(1)
        menu = await ctx.send(embed=embed)
        # add the reactions
        await menus.add_emojis(menu, 1)
        # change the role menu id
        menus.change_id(menu.id)


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        # Gets the information from reaction
        information = menus.get(payload)
        user = information['user']
        emoji= information['emoji']

        # checks if input is from bot
        if user.bot:
            pass
        else:
            #check if reaction is ◀ or ▶
            if emoji.name == '▶':
                await menus.flip_right(self.client, payload)
            """
            channel = self.client.get_channel(payload.channel_id)
            msg = await channel.fetch_message(payload.message_id)
            embed = msg.embeds[0]
            print(embed.title[0])
            """
        """
        # gives the user the role
        async def give_role(user,role):
            guild_id = payload.guild_id
            guild = self.client.get_guild(guild_id)
            role = discord.utils.get(guild.roles, name = role)
            if role in user.roles:
                await user.remove_roles(role)
            else:
                await user.add_roles(role)
        
        # Gets the information from reaction
        information = menus.get(payload)
        user = information['user']
        emoji= information['emoji']

        # checks if input is from bot
        if user.bot:
            pass
        else:
            if menus.match(information['message_id'], correct_message_id):
                reaction = emoji
                #check if reaction is ◀ or ▶
                if reaction.name == '▶':
                    await menus.flip_right(self.client, payload)

            #check if the reaction should trigger a role adding
                try:
                    index = emoji_list.index(emoji.name)
                    role = role_names[index]
                    await give_role(user,role)
                except:
                    try:
                        index = class_list.index(emoji.name)
                        role = class_names[index]
                        await give_role(user,role)
                    except:
                        pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):

        async def take_role(user,role):
            guild_id = payload.guild_id
            guild = self.client.get_guild(guild_id)
            role = discord.utils.get(guild.roles, name = role)
            await user.remove_roles(role)
        

        channel = self.client.get_channel(payload.channel_id)
        message_id = payload.message_id
        message = await channel.fetch_message(message_id)
        user_id = payload.user_id
        user = await message.guild.fetch_member(user_id)
        emoji = payload.emoji

        if user.bot:
            pass
        else:
            if menus.match(message_id,correct_message_id):
            #check if the reaction should trigger a role adding
                try:
                    index = emoji_list.index(emoji.name)
                    role = role_names[index]
                    await take_role(user,role)
                except:
                    try:
                        index = class_list.index(emoji.name)
                        role = class_names[index]
                        await take_role(user,role)
                    except:
                        pass
    """
def setup(client):
    client.add_cog(RoleReactions(client))