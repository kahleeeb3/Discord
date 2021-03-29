import discord
from discord.ext import commands, tasks
from modules import canvas, time

class Canvas(commands.Cog):
    """Pulls canvas info for Caleb"""

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.check.start()

    @commands.command()
    async def canvas(self, ctx, offset):
        loading = await ctx.send('loading...')
        my_list = canvas.main(offset)
        await loading.edit(content = my_list)

    @tasks.loop(seconds= 60)
    async def check(self):

        channel_id = 768896234810245141
        channel = self.client.get_channel(channel_id)

        curr_time = time.curr_time()[1]

        if curr_time == '08:00 AM':
            my_list = canvas.main(1)
            await channel.send(my_list)


def setup(client):
    client.add_cog(Canvas(client))

