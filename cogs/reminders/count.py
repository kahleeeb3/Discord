import discord
from discord.ext import commands, tasks
from modules import time
import json

class Countdown(commands.Cog):
    """Show the Reminders"""

    def __init__(self, client):
        self.client = client
            
    @commands.Cog.listener()
    async def on_ready(self):
        self.check.start()

    @commands.command()
    async def count(self,ctx):
        # Step 1: load in the data or create the file
        try:
            a_file = open("./cogs/reminders/data_file.json", "r")
            data = json.load(a_file)
            a_file.close()
        except:
            data = {"Counters":{}}
            a_file = open("./cogs/reminders/data_file.json", "w")
            json.dump(data, a_file)
            a_file.close()
        embed = discord.Embed(title=f'Count Downs!',color=discord.Color.red())

        # Step 2: decrease the count value
        for counter in data["Counters"]:
            title = data["Counters"][counter]["title"]
            count = data["Counters"][counter]["quantity"]

            embed.add_field(name=f'{title}',value = f'{count}', inline=False)

        await ctx.send(embed=embed)
        """
        a_file = open("./cogs/Counter/data_file.json", "w")
        json.dump(data, a_file)
        a_file.close()
        """

            
    @tasks.loop(seconds= 60)
    async def check(self):
        # define the channel you want to send to
        channel_id = 768896234810245141
        channel = self.client.get_channel(channel_id)
        #get information about the current time
        today_day = time.curr_time()[0]
        curr_time = time.curr_time()[1]

        #print(curr_time)
        
            


def setup(client):
    client.add_cog(Countdown(client))
