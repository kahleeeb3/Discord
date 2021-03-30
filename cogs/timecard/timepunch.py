import discord
from discord.ext import commands, tasks
from modules import lists, time

import requests

jobs = {
        'QSC' : '21949',
        'ETC' : '21591',
        'SI' : '21647',
        'qsc' : '21949',
        'etc' : '21591',
        'si' : '21647',
        }

payload = {
    'username':'cmpowell22',
    'password':'teamCMP3',
    'login': 'Login',
    'logMeln':'1'
}

class TimeCard(commands.Cog):
    """Clocks Caleb in and out of his WISE Job"""

    def __init__(self, client):
        self.client = client
            
    """
    @commands.Cog.listener()
    async def on_ready(self):
        self.check.start()
    """
    #the above is for automation

    @commands.command()
    async def ci(self,ctx,jobname):
        """Clock in"""

        def check_job(name):
            if jobname in jobs:
                return True
            else:
                return False

        def clock_in(id):
            s = requests.session()
            response = s.post('https://www.wabash.edu/timecard/login.cfm', data = payload)
            login = s.get(f'https://www.wabash.edu/timecard/home.cfm?login={jobs[jobname]}')
            s.close()
        
        if ctx.message.author.name == 'CalebP':
            if check_job(jobname):
                clock_in(jobs[jobname])
                await ctx.send(f'Clocked into {jobname}.')
            else:
                await ctx.send(f'{jobname} is not a real job')
        else: pass
            
    @commands.command()
    async def co(self,ctx,jobname):
        """Clock Out"""

        def check_job(name):
            if jobname in jobs:
                return True
            else:
                return False

        def clock_out(id):
            s = requests.session()
            response = s.post('https://www.wabash.edu/timecard/login.cfm', data = payload)
            logout = s.get(f'https://www.wabash.edu/timecard/home.cfm?leave={jobs[jobname]}')
            s.close()
        
        if ctx.message.author.name == 'CalebP':
            if check_job(jobname):
                clock_out(jobs[jobname])
                await ctx.send(f'Clocked out of {jobname}.')
            else:
                await ctx.send(f'{jobname} is not a real job')
        else: pass
            


    # this is for automation
    """
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
    """
            


def setup(client):
    client.add_cog(TimeCard(client))
