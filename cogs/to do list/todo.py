import discord
from discord.ext import commands, tasks
import datetime
import pytz


class ToDo(commands.Cog):

    def __init__(self, client):
        self.client = client
            
    #@commands.Cog.listener()
    #async def on_ready(self):
        #self.check.start()

    @commands.command()
    async def todo(self,ctx,action):

        if action == 'new':
            a_file = open('./cogs/to do list/list.txt', "a")
            menu = await ctx.send(f'What would you like to add?')
            new_info = await self.client.wait_for('message')
            await new_info.delete()
            a_file.write(f'{new_info.content}\n')
            a_file.close()
            #reads new content of text file
            reminders = open('./cogs/to do list/list.txt')
            content = reminders.read()
            reminders.close()
            #edits the menu
            await menu.edit(content=content)
   
        if action == 'edit':
            #send the current list
            reminders = open('./cogs/to do list/list.txt')
            content = reminders.read()
            menu = await ctx.channel.send(f'{content}\n**Input text to replace:**')
            reminders.close()
            #ask for input on the new list
            new_list = await self.client.wait_for('message')
            await new_list.delete()
            #make changes to text file
            a_file = open('./cogs/to do list/list.txt', "w")
            a_file.write(new_list.content)
            a_file.close()
            #reads new content of text file
            reminders = open('./cogs/to do list/list.txt')
            content = reminders.read()
            reminders.close()
            #edits the menu
            await menu.edit(content=content)

        if action =='Place Holder':
            #reads content of text file
            reminders = open('./cogs/to do list/list.txt')
            content = reminders.read()
            reminders.close()
            #generates a list from text file
            a_file = open('./cogs/to do list/list.txt', "r")
            list_of_lines = a_file.readlines()
            a_file.close()
            #select item to delete
            menu = await ctx.channel.send(content + '**Which line would you like to edit? (Int)**')
            choice = await self.client.wait_for('message')
            await choice.delete()
            selection = int(choice.content) - 1
            #choice your changes
            await menu.edit(content = f'Input text to replace: `{list_of_lines[selection]}`')
            new_info = await self.client.wait_for('message')
            await new_info.delete()
            #make changes to text file
            list_of_lines[selection] = new_info.content + '\n'
            a_file = open('./cogs/to do list/list.txt', "w")
            a_file.writelines(list_of_lines)
            a_file.close()
            #reads new content of text file
            reminders = open('./cogs/to do list/list.txt')
            content = reminders.read()
            reminders.close()
            #edits the menu
            await menu.edit(content=content)

        if action == 'delete':
            #reads content of text file
            reminders = open('./cogs/to do list/list.txt')
            content = reminders.read()
            reminders.close()
            #generates a list from text file
            a_file = open('./cogs/to do list/list.txt', "r")
            list_of_lines = a_file.readlines()
            a_file.close()
            #select item to delete
            menu = await ctx.channel.send(content + '**Which line would you like to delete? (Int)**')
            choice = await self.client.wait_for('message')
            await choice.delete()
            selection = int(choice.content) - 1
            #edit the text file
            for position, line in enumerate(list_of_lines):
                if position > selection:
                    list_of_lines[position-1] = line
            list_of_lines[len(list_of_lines)-1] = ''
            a_file = open('./cogs/to do list/list.txt', "w")
            a_file.writelines(list_of_lines)
            a_file.close()
            #reads new content of text file
            reminders = open('./cogs/to do list/list.txt')
            content = reminders.read()
            reminders.close()
            #edits the menu
            await menu.edit(content=content)

        if action == 'list':
            reminders = open('./cogs/to do list/list.txt')
            content = reminders.read()
            await ctx.channel.send(content)
            reminders.close()

    #@tasks.loop(seconds= 60)
    async def check(self):
        channel_id = 768896234810245141
        channel = self.client.get_channel(channel_id)

        async def check_time(curr_time,list):
            if curr_time in list[place]:
                await channel.send(list[place+1])

        reminders = open('./cogs/reminders/reminders.txt')
        list_reminders = reminders.readlines()

        # current time info
        today_day = datetime.datetime.now().strftime('%a')
        tz_NY = pytz.timezone('America/New_York') 
        hour = datetime.datetime.now(tz_NY).strftime('%I')
        minute = datetime.datetime.now(tz_NY).strftime('%M')
        suffix = datetime.datetime.now(tz_NY).strftime('%p')

        curr_time = (f'{hour}:{minute} {suffix}')

        place = 0
        for lines in list_reminders:
            place += 1
            if today_day in lines:
                #print(place)
                await check_time(curr_time,list_reminders)
            


def setup(client):
    client.add_cog(ToDo(client))
