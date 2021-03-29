import discord
from discord.ext import commands, tasks
import datetime
import pytz
from time import sleep

from modules import lists, time


class Reminder(commands.Cog):
    """Show the Reminders"""

    def __init__(self, client):
        self.client = client
            
    @commands.Cog.listener()
    async def on_ready(self):
        self.check.start()

    @commands.command()
    async def remind(self,ctx,action):
            
        if action == 'add':
            menu = await ctx.send(f'What would you like to add?')
            new_info = await self.client.wait_for('message')
            await new_info.delete()
            lists.add('reminders',new_info)
            #reads new content of text file
            content = lists.to_string('reminders')
            #edits the menu
            await menu.edit(content=content)
   
        if action == 'edit':
            #send the current list
            content = lists.to_string('reminders')
            menu = await ctx.channel.send(f'{content}**Input text to replace:**')
            #ask for input on the new list
            new_list = await self.client.wait_for('message')
            #make changes to text file
            lists.edit('reminders',new_list.content)
            await new_list.delete()
            #reads new content of text file
            content = lists.to_string('reminders')
            #edits the menu
            await menu.edit(content=content)

        if action == 'delete':
            #reads content of text file
            content = lists.to_string('reminders')
            #select item to delete
            menu = await ctx.channel.send(content + '**Which line would you like to delete? (Int)**')
            choice = await self.client.wait_for('message')
            await choice.delete()
            selection = int(choice.content) - 1
            #edits the file
            lists.delete('reminders',selection)
            #reads new content of text file
            content = lists.to_string('reminders')
            #edits the menu
            await menu.edit(content=content)

        if action == 'list':
            content = lists.to_string('reminders')
            await ctx.send(content)

    @commands.command()
    async def time(self,ctx):
        day = time.curr_time()[0]        
        curr_time = time.curr_time()[1]
        await ctx.channel.send(f'Current Time: {day} {curr_time}')
            
    @tasks.loop(seconds= 60)
    async def check(self):
        channel_id = 768896234810245141
        channel = self.client.get_channel(channel_id)
        
        list_reminders = lists.read('reminders')

        today_day = time.curr_time()[0]
        curr_time = time.curr_time()[1]

        #get the index of the list with todays date in it
        events = lists.in_list('reminders',today_day)
        if not events:
            pass
        else:
            for index in events:
                if curr_time in list_reminders[index+1]:
                    await channel.send(list_reminders[index+2])
            


def setup(client):
    client.add_cog(Reminder(client))
