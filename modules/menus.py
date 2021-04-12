import discord
from modules import lists
from modules.json import json


def get_embed(number:int):
    # loads in the data
    data = json.load('rolemenu')
    # define the embed
    title = data["menu"][f"{number}"]["title"]
    description = data["menu"][f"{number}"]["description"]
    embed = discord.Embed(title=f'{title}',description = description,color=discord.Color.red())

    for role in data["menu"][f"{number}"]["roles"]:
        emoji = data["menu"][f"{number}"]["roles"][role]["emoji"]
        embed.add_field(name=f'{emoji}',value = f'{role}', inline=True)

    return embed

async def add_emojis(menu, number:int):
    data = json.load('rolemenu')
    for role in data["menu"][f"{number}"]["roles"]:
        emoji = data["menu"][f"{number}"]["roles"][role]["emoji"]
        await menu.add_reaction(emoji)

    await menu.add_reaction('▶')

def change_id(message_id):
    data = json.load('rolemenu')
    data["message_id"] = message_id
    json.edit('rolemenu',data)

async def get_msg(bot,payload):
    # get menu number
    channel = bot.get_channel(payload.channel_id)
    msg = await channel.fetch_message(payload.message_id)
    return msg

async def flip_right(bot,payload):
    # get menu number
    msg = await get_msg(bot, payload)
    embed = msg.embeds[0]
    current = int(embed.title[0])
    try:
        embed2 = get_embed(current + 1)
        current = current + 1
    except:
        embed2 = get_embed(1)
        current = 1
    await msg.clear_reactions()
    await msg.edit(embed = embed2)
    await add_emojis(msg, current)

def get(payload):
    user = payload.member
    message_id = payload.message_id
    emoji = payload.emoji
    return {'user': user,'message_id': message_id, 'emoji': emoji}

def check_message_id(message_id):
# checks if the reaction was added to the role menu
    # loads in the data
    data = json.load('rolemenu')
    correct_message_id = data["message_id"]
    if message_id == correct_message_id:
        return True
    else:
        return False

def get_role_id(menu_num, reaction):
# returns the role id for the given reaction
    data = json.load('rolemenu')
    for role in data["menu"][f"{menu_num}"]["roles"]:
        if reaction.name in data["menu"][f"{menu_num}"]["roles"][f"{role}"]["emoji"]:
            return data["menu"][f"{menu_num}"]["roles"][f"{role}"]["id"]
