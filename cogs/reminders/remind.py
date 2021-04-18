import discord
from discord.ext import commands, tasks
import datetime
import pytz
from time import sleep

from modules import lists, time
from modules.json import json


class Reminder(commands.Cog):
    """Show the Reminders"""

    def __init__(self, client):
        self.client = client
            
    @commands.Cog.listener()
    async def on_ready(self):
        self.check.start()
        self.check_event.start()

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
    async def event(self,ctx, *action):
        async def get_input():
            msg = await self.client.wait_for("message")
            if msg.author == ctx.author and msg.channel == ctx.channel:
                await msg.delete()
            else:
                print('Wrong')
                msg = await get_input()
            return msg

        if not action:
            pass
        elif action[0] == 'create':
            data = json.load('events')
            ## GET INFORMATION ABOUT THE EVENT
            # ask for the date of the event
            menu = await ctx.channel.send('What date is your event?')
            date = (await get_input()).content
            await menu.edit(content = f'{menu.content}\n`{date}`')
            # ask for the title of the event
            await menu.edit(content = f'{menu.content}\nWhat is the name of your event?')
            title = (await get_input()).content
            await menu.edit(content = f'{menu.content}\n`{title}`')
            # ask for the description of the event
            await menu.edit(content = f'{menu.content}\nGive a description of your event')
            description = (await get_input()).content
            await menu.edit(content = f'{menu.content}\n`{description}`')
            # ask what time the event is
            await menu.edit(content = f'{menu.content}\nWhat time is your event?')
            time = (await get_input()).content
            await menu.edit(content = f'{menu.content}\n`{time}`')
            # ask if the information is correct
            ask = await ctx.channel.send('Is the above information correct? (y/n)')
            ans = (await get_input()).content
            if ans == 'y':
                # Show a confirmation
                await menu.edit(content = f'{menu.content}\n**Confirmed!**')
                ## SAVE THE DATA
                # Check if there is already an event in that date
                try:
                    # there is at least one event on that date already
                    eventNum = len(data["date"][f'{date}']) + 1
                except:
                    # None exist
                    eventNum = 1
                    try:
                        data["date"][date]={}
                    except:
                        data = {"date":{f"{date}":{}}}
                # change the data
                data["date"][date][eventNum]={
                    "title":title,
                    "description":description,
                    "time":time
                }
                json.edit('events',data)
            else:
                pass
            await ask.delete()
    
    @commands.command()
    async def time(self,ctx):
        day = time.curr_time()[0]        
        curr_time = time.curr_time()[1]
        date = time.curr_time()[2]
        await ctx.channel.send(f'Current Time: {day} {date} {curr_time}')
            
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
            
    @tasks.loop(seconds= 60)
    async def check_event(self):
        channel_id = 768896234810245141
        channel = self.client.get_channel(channel_id)

        day = time.curr_time()[0]        
        curr_time = time.curr_time()[1]
        date = time.curr_time()[2]

        data = json.load('events')
        # look through all events dates
        for event_date in data["date"]:
            # if event is on today
            if event_date == date:
                # look through all events times
                for numEvent in data["date"][event_date]:
                    # if event is at this time
                    if curr_time == data["date"][event_date][numEvent]["time"]:
                        title = data["date"][event_date][numEvent]["title"]
                        description = data["date"][event_date][numEvent]["description"]
                        await channel.send(f'{title} - {description}')
                    else:
                        pass
                        #print(curr_time)

            

def setup(client):
    client.add_cog(Reminder(client))
