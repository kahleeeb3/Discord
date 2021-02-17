import discord
from modules import lists

async def add_emojis(bot,payload,message):
    emojis = []
    for line in message.content.split():
        if len(line) == 1 and line != ':':
            emojis.append(line)
        elif line.startswith('<'):
            emojis.append(line)

    #get the emoji objects
    for emoji_name in emojis:
        try:
            await message.add_reaction(emoji_name)
        except:
            await message.add_reaction(emoji_name)
    
    #finally, add the right arrow
    await add_right_arrow(message)

def get(payload):
    user = payload.member
    message_id = payload.message_id
    emoji = payload.emoji
    return {'user': user,'message_id': message_id, 'emoji': emoji}

def match(a,b):
    if a==b:
        return True
    else:
        return False

async def flip_right(bot,payload):
    #get menu information
    channel = bot.get_channel(payload.channel_id)
    message_id = payload.message_id
    message = await channel.fetch_message(message_id)
    #get current menu number
    menu_number = int(message.content.split('\n')[0].split(' ')[1].replace(':',''))-1
    # get the next menu content
    menu_content = lists.to_string('rolemenus')
    try:
        menu_next = menu_content.split("END OF LIST")[menu_number+1]
    except:
        menu_next = menu_next = menu_content.split("END OF LIST")[0]
    # change the menu
    await message.edit(content = menu_next)
    # remove all emojis and add new ones
    await message.clear_reactions()
    await add_emojis(bot,payload,message)
    
async def add_right_arrow(menu):
    await menu.add_reaction('▶')

async def remove_right_arrow(menu):
    await menu.remove_reaction('▶')
