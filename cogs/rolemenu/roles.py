import discord
from discord.ext import commands
from modules import lists, menus
from modules.json import json

correct_message_id = 811657569515864124
emoji_list = ['🖥','🫂','😂','🐶','🎬', '🎵', '🙌']
role_names = ["CSC Stuff",'General', "Memes", "Pets","Movies","Music",'Commoners']
class_list = ['chad','excellent','ross','Spongetard','joe']
class_names = ['Complex, Anal Si','Electronics','E&M','Theory of Programming Languages','Ad Lab']

class RoleReactions(commands.Cog):
    """Sends the role menu to the chat"""

    def __init__(self, client):
        self.client = client

    #channel_id = 785343273190555648
    #channel = self.client.get_channel(channel_id)

    @commands.command()
    async def rolemenu(self,ctx):
        data = json.load('rolemenu')
        title = data["menu"]["1"]["title"]
        description = data["menu"]["1"]["description"]
        embed = discord.Embed(title=f'{title}',description = description,color=discord.Color.red())

        for role in data["menu"]["1"]["roles"]:
            emoji = data["menu"]["1"]["roles"][role]["emoji"]
            embed.add_field(name=f'{emoji}',value = f'{role}', inline=True)

        menu = await ctx.send(embed=embed)
        await menus.add_right_arrow(menu)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        async def give_role(user,role):
            guild_id = payload.guild_id
            guild = self.client.get_guild(guild_id)
            role = discord.utils.get(guild.roles, name = role)
            if role in user.roles:
                await user.remove_roles(role)
            else:
                await user.add_roles(role)
        

        information = menus.get(payload)
        user = information['user']
        emoji= information['emoji']
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

def setup(client):
    client.add_cog(RoleReactions(client))