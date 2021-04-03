import discord
from discord.ext import commands
import os
import subprocess
import json


class Kill(commands.Cog):
    """Commands For Caleb's Use"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def t(self, ctx, *, command):
        """Run Terminal Commands"""

        """
        # Step 1: load in the data or create the file
        try:
            a_file = open("./cogs/kill/data_file.json", "r")
            data = json.load(a_file)
            a_file.close()
        except:
            data = {"commands":{}}
            a_file = open("./cogs/kill/data_file.json", "w")
            json.dump(data, a_file)
            a_file.close()

        # step 2 combine the commands
        collection = ''
        for item in data["commands"]:
            if collection == '':
                collection = data["commands"][item]
            else:
                collection = collection + '; '+ data["commands"][item]

        collection = collection + '; '+ command
        print(collection)
        
        # Step 2: See if the command worked
        async def run():
            try:
                output = str(subprocess.check_output(collection, shell=True))
                output = output.replace("b\'","").replace("\\n\'","").replace("\\n","\n")
                await ctx.channel.send(f'`{output}`')
                return True
            except:
                output = str(subprocess.check_output(collection, shell=True))
                output = output.replace("b\'","").replace("\\n\'","").replace("\\n","\n")
                await ctx.channel.send(f'`{output}`')
                return False

        if await run():
            # Step 3: get new data
            numCommands = len(data["commands"])
            data["commands"][str(numCommands+1)] = command
            # Step 4: Add the data
            a_file = open("./cogs/kill/data_file.json", "w")
            json.dump(data, a_file)
            a_file.close()

        if command == 'reset':
            data["commands"] = {}
            a_file = open("./cogs/kill/data_file.json", "w")
            json.dump(data, a_file)
            a_file.close()
            await ctx.channel.send(f'Reset terminal')
        """
        output = str(subprocess.check_output(command, shell=True))
        output = output.replace("b\'","").replace("\\n\'","").replace("\\n","\n")
        await ctx.channel.send(f'{output}')

    @commands.command()
    async def github(self, ctx, *, message):
        """Pushes all the files to github repo"""
        command = f'cd /home/pi/Desktop/Discord; git add --all; git commit -a -m "{message}";git push'
        output = str(subprocess.check_output(command, shell=True))
        output = output.replace("b\'","").replace("\\n\'","").replace("\\n","\n")
        await ctx.channel.send(f'{output}')

    @commands.command()
    async def timeout(self, ctx, *max_time):
        """Deletes all messages for a given period of time
        can pass in the amount of time as a variable `$timeout <time>`"""
        import time

        if not max_time:
            max_time = 600
        else:
            max_time = max_time[0]

        await ctx.channel.send(f'**Due to conflict:** Chat is disabled for {max_time} seconds')

        start_time = time.time()  # remember when we started
        while (time.time() - start_time) < int(max_time):
            thing = await self.client.wait_for('message')
            await thing.delete()

        await ctx.channel.send(f'Chat is enabled. Please be friends.')
    
    @commands.command()
    async def off(self, ctx):
        """Turns the Bot off"""
        if ctx.message.author.name == 'CalebP':
            await ctx.channel.send(f'https://tenor.com/view/cry-sad-toy-story-woody-so-long-partner-gif-9797730')
            exit()
        else:
            await ctx.channel.send(f'Shut the fuck up {ctx.message.author.name}, you dont have the authority for that.')

    @commands.command()
    async def restart(self, ctx):
        """Restarts the Bot"""
        if ctx.message.author.name == 'CalebP':
            await self.client.change_presence(activity=discord.Activity(type = discord.ActivityType.streaming, name = f'Rebooting...') )
            import os
            os.system("sudo reboot")
            exit()
        else:
            await ctx.channel.send(f'Shut the fuck up {ctx.message.author.name}, you dont have the authority for that.')
        


def setup(client):
    client.add_cog(Kill(client))
