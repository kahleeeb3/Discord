# Emma Watson
This is a repository for my discord bot. The original GitHub Repo was created 2020-10-25 20:49:50. Amen.

## Recycling_Bin:
This folder is intended for files that will no be run and are just being saved for future reference
## cogs:
This folder contains a breakdown of each command into a sperate folder
## modules:
This folder is where commonly used cogs is placed for importation into future code

The 'driver' folder contains the files for the LCD driver

The 'lists' folder is where .txt files are read/write to using the 'lists.py' module

## main.py:
this is where the main code is run manually for the purpose of changes

## selfboot.py:
this code is set to run on boot

```python
print('Starting Bot...')
# IMPORTS
import discord
from discord.ext import commands, tasks
import os

# defines the prefix for all commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '$', intents=intents)


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
    await client.change_presence(activity=discord.Game(f'UPDATING!'))

 
# place token code in the following directory
client.run(open('/home/pi/Desktop/token.txt', "r").read())
```

> *'Procfile', 'package.json', and 'requirements.txt'* are only needed for running the bot on *Heroku*

## Pushing to Github on Linux:

```
git commit -a
git push
```
