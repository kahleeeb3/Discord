import discord
from discord.ext import commands
from modules import lists, menus,time
import random
import tempfile
import requests
import os

class SavePhoto(commands.Cog):

    def __init__(self, client):
        self.client = client

    #channel_id = 785343273190555648
    #channel = self.client.get_channel(channel_id)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        async def check_file(files):
            for pics in files:
                if pics.filename.endswith('.png'):
                    await download_file(pics)
                elif pics.filename.endswith('.jpg'):
                    await download_file(pics)
                else:
                    await channel.send('Error: Must be a PNG/JPG')
                    await message.add_reaction('❌')

        async def download_file(pic):
            filename = tempfile.NamedTemporaryFile().name
            filename = filename[5:]
            filetype = pic.filename[-4:]
            url = pic.url
            r = requests.get(url, allow_redirects=True)
            open(f'/home/pi/Desktop/Discord/Photos/{filename}{filetype}', 'wb').write(r.content)
            await message.add_reaction('✅')

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
                await check_file(files)


    @commands.command()
    async def rpic(self, ctx):
        await ctx.message.delete()

        import os, random
        picture = random.choice(os.listdir('/home/pi/Desktop/Discord/Photos/')) #change dir name to whatever
        await ctx.send(file=discord.File(f'/home/pi/Desktop/Discord/Photos/{picture}'))

def setup(client):
    client.add_cog(SavePhoto(client))