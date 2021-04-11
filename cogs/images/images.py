import discord
from discord.ext import commands, tasks
from modules import lists, menus,time
import random
import tempfile
import requests
import os
from modules.json import json


class Picture(commands.Cog):
    """Sends a randdom picture to the chat"""

    def __init__(self, client):
        self.client = client
        self.check.start()

    #channel_id = 785343273190555648
    #channel = self.client.get_channel(channel_id)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        async def download_file(pic):
            filename = tempfile.NamedTemporaryFile().name
            filename = filename[5:]
            filetype = pic.filename[-4:]
            url = pic.url
            r = requests.get(url, allow_redirects=True)
            open(f'/home/pi/Desktop/Discord/modules/Photos/{filename}{filetype}', 'wb').write(r.content)
            await message.add_reaction('✅')
            # send Caleb a DM of who added the photo
            user_id = payload.user_id
            user = self.client.get_user(user_id)
            caleb = self.client.get_user(487323172492935189)
            channel = await caleb.create_dm()
            await channel.send(f'{user.name} added a ⭐ to a file')

        star = '⭐'
        if payload.emoji.name == star:
            # get the id values from payload
            channel_id = payload.channel_id
            message_id = payload.message_id

            #get objects from the id's
            channel = self.client.get_channel(channel_id)
            message = await channel.fetch_message(message_id)
            files = message.attachments
            if not files:
                #print('None')
                await message.add_reaction('❌')
            else:
                #await check_file(files)
                for pic in files:
                    await download_file(pic)
        

    @commands.command()
    async def rpic(self, ctx):
        user = ctx.message.author.name
        # get the current count
        data = json.load('rpic')
        try:
            count = data["users"][user]["count"]
        except:
            data = {"users":{user:{"count": 0}}}
            count = data["users"][user]["count"]

        if count < 5:

            await ctx.message.delete()

            import os, quantumrandom
            pictures = os.listdir('/home/pi/Desktop/Discord/modules/Photos/')
            number = int(quantumrandom.randint(0, len(pictures)))
            picture = pictures[number]
            await ctx.send(file=discord.File(f'/home/pi/Desktop/Discord/modules/Photos/{picture}'))

            #add 1 to the count
            data["users"][user]["count"] = count + 1

            # upload new data
            json.edit('rpic',data)
        
        else:
            await ctx.send('Please Stop.')

    @tasks.loop(minutes = 3)
    async def check(self):
        print('reset')
        json.edit('rpic',{})

def setup(client):
    client.add_cog(Picture(client))