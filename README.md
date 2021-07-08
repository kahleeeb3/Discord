# Emma Watson
This is a repository for my discord bot. The original GitHub Repo was created 2020-10-25 20:49:50. Amen.

For this bot to work, the repository should be placed in the following directory:

```
cd /home/pi/Desktop/
```
## Setup (Linux Terminal on Raspberry Pi OS):
```
cd /home/pi/Desktop
git clone https://github.com/kahleeeb3/Discord.git
python3 -m pip install -U discord.py
pip3 install pytz
pip3 install icalendar
touch token.txt
sudo nano token.txt
<paste the token in here and then save>
cd Discord
python3 main.py
```
## Setup LCD
https://www.youtube.com/watch?v=3XLjVChVgec&ab_channel=MakerTutor
```
cd /home/pi/Desktop
git clone https://github.com/the-raspberry-pi-guy/lcd.git
cd lcd
sudo sh install.sh
```

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

## Directories
# main.py:
this is where the main code is run manually for the purpose of quick changes
# selfboot.py:
this code is set to run on boot
# boot:
This folder contains the necissary files and instructions for booting the bot from startup on linux
# cogs:
This folder contains a breakdown of each command in a sperate folder
# modules:
This folder is where commonly used lines of code are placed for importation
# Recycling_Bin:
This folder is intended for files that will not be run and are just being saved for future reference