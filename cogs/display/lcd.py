import discord
from discord.ext import commands, tasks
from time import sleep
from gpiozero import Button
import datetime

from modules import lists, drivers, lcd

class Display(commands.Cog):
    """Puts a message on an LCD 16x2 Display"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lcd(self, ctx,*,message):
        if ctx.message.author.name == 'CalebP':
            await lcd.display(ctx,message)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if 'Direct Message' in str(message.channel) and message.author.name == 'bailey':
            if '$' in message.content:
                pass
            else:
                await lcd.display(message,message.content)
    
    @commands.Cog.listener()
    async def on_ready(self):
        # Python Program to Get IP Address 
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IPAddr= s.getsockname()[0]
        s.close()
        lists.cycle_display([IPAddr])
        # RUN THE BUTTON SCRIPT
        button = Button(26)
        self.button.start(button)

    @commands.command()
    async def ip(self, ctx):
        """Returns and displays the IP address of the bot"""
        # Python Program to Get IP Address 
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IPAddr= s.getsockname()[0]
        s.close()
        await ctx.send(IPAddr)

    @tasks.loop(seconds= 1)
    async def button(self,button):
        if button.is_active:
            """
            #un-comment this for todo
            list_of_lines = lists.read('todo')
            lists.cycle_display(list_of_lines)
            """
            # Python Program to Get IP Address 
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            IPAddr= s.getsockname()[0]
            s.close()
            lists.cycle_display([IPAddr])
        


def setup(client):
    client.add_cog(Display(client))
