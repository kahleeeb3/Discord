import discord
from discord.ext import commands, tasks
import datetime
import pytz


class Time(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.send_reminder.start()
    
    @tasks.loop(minutes= 1)
    async def send_reminder(self):

        def get_curr_time():   
            tz_NY = pytz.timezone('America/New_York') 

            day_week = datetime.datetime.now().strftime('%a')
        
            hour = datetime.datetime.now(tz_NY).strftime('%I')
            minute = datetime.datetime.now(tz_NY).strftime('%M')
            suffix = datetime.datetime.now(tz_NY).strftime('%p')

            curr_time = (f'{day_week} {hour}:{minute} {suffix}')
        
            return curr_time

        def get_channel():
            channel_id = 770310518564454471
            channel = self.client.get_channel(channel_id)
            return channel
        
        def is_events():
            #print('testing')
            #print(curr_time)
            if curr_time in events:
                return True
            else:
                return False

        async def get_message():
            if channel == None:
                pass
            else:
                if curr_time == events[0]:
                    await channel.send('Reminding you of this thing!')

        # This is the start of the code
        # gets the current time
        curr_time = get_curr_time()
        #get lists of events
        events = ["Wed 09:00 PM"]

        # if current time is an event
        if(is_events()):
            channel = get_channel()
            #print(channel)
            await get_message()        
        
    @commands.command()
    async def time(self,ctx):
        def get_curr_time():   
            tz_NY = pytz.timezone('America/New_York') 

            day_week = datetime.datetime.now().strftime('%a')
        
            hour = datetime.datetime.now(tz_NY).strftime('%I')
            minute = datetime.datetime.now(tz_NY).strftime('%M')
            suffix = datetime.datetime.now(tz_NY).strftime('%p')

            curr_time = (f'{day_week} {hour}:{minute} {suffix}')
        
            return curr_time
        
        time = get_curr_time()
        await ctx.channel.send(f'Current Time: {time}')

    @commands.command()
    async def reminder(self,ctx,action):
        if action == 'new':
            await ctx.channel.send('What days would You like this reminder to occur on? `M/Tu/W/Th/F/Sa/Su`')
            new_content = await self.client.wait_for('message')

            list_of_lines[1] = f'{new_content.content}\n'
            a_file = open('./cogs/reminders/reminders.txt', "w")
            a_file.writelines(list_of_lines)
            a_file.close()

            await ctx.channel.send('Sent!')
            await ctx.channel.purge(limit=4)

        if action == 'edit':
            await ctx.channel.send('``Example: Mon 08:00 PM``')
            a_file = open('./cogs/reminders/reminders.txt', "r")
            list_of_lines = a_file.readlines()

            new_content = await self.client.wait_for('message')

            list_of_lines[1] = f'{new_content.content}\n'
            a_file = open('./cogs/reminders/reminders.txt', "w")
            a_file.writelines(list_of_lines)
            a_file.close()

            await ctx.channel.send('Sent!')
            await ctx.channel.purge(limit=4)

        if action == 'list':
            reminders = open('./cogs/reminders/reminders.txt')
            content = reminders.read()
            await ctx.channel.send(content)
            reminders.close()

    @tasks.loop(minutes= 1)
    async def temp_reminder(self):

        def get_curr_time():   
            tz_NY = pytz.timezone('America/New_York') 

            day_week = datetime.datetime.now().strftime('%a')
        
            hour = datetime.datetime.now(tz_NY).strftime('%I')
            minute = datetime.datetime.now(tz_NY).strftime('%M')
            suffix = datetime.datetime.now(tz_NY).strftime('%p')

            curr_time = (f'{day_week} {hour}:{minute} {suffix}')
        
            return curr_time

        def get_channel():
            channel_id = 770310518564454471
            channel = self.client.get_channel(channel_id)
            return channel
        
        def is_events():
            #print('testing')
            #print(curr_time)
            if curr_time in events:
                return True
            else:
                return False

        async def get_message():
            if channel == None:
                pass
            else:
                if curr_time == events[0]:
                    await channel.send('Reminding you of this thing!')

        # This is the start of the code
        # gets the current time
        curr_time = get_curr_time()
        #get lists of events
        events = ["Wed 09:00 PM"]

        # if current time is an event
        if(is_events()):
            channel = get_channel()
            #print(channel)
            await get_message()        
        



def setup(client):
    client.add_cog(Time(client))
