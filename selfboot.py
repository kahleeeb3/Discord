#test is a test
import discord
import os
import asyncio
from discord.ext import commands, tasks
from itertools import cycle
from time import sleep

print('wait 15 seconds')
sleep(15)

intents = discord.Intents.all()
# defines the prefix for all commands
client = commands.Bot(command_prefix = '$', intents=intents)
status_list = cycle( ['Clone Wars', 'The Mandalorian', 'You'] )

# loads all folders within the cogs folder
for folder in os.listdir('/home/pi/Desktop/Discord/cogs'):
    # ignores the cache folder
    if folder == '__pycache__':
        pass
    else:
        # loads all files in folder
        for filename in os.listdir(f'/home/pi/Desktop/Discord/cogs/{folder}'):
            #if its a python folder:
            if filename.endswith('.py'):
                #create a cog with the files in that folder
                client.load_extension(f'cogs.{folder}.{filename[:-3]}')

@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(activity=discord.Game(f'Bot Updated'))
    await client.wait_for('message')
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.watching, name = f'you, Wazowski. Always watching.') )
    #change_status.start()

@tasks.loop(seconds=10.0)
async def change_status():
    #await client.change_presence(activity=discord.Game(f"""with {next(status)}'s heart""" ) )
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.watching, name = f'{next(status_list)}') )
    
    

# Gets bot token stored on heroku server
#client.run(os.environ['BOT_TOKEN'])
 
# placed here for running the bot locally 
client.run(open('/home/pi/Desktop/token.txt', "r").read())