import discord
from discord.ext import commands, tasks
from time import sleep
from gpiozero import Button
import datetime

from modules import lists, drivers

class Display(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        button = Button(26)
        self.button.start(button)

    @commands.command()
    async def lcd(self, ctx,*,message):
        display = drivers.Lcd()

        if message == 'off':
            display.lcd_backlight(0)
        else:
            display.lcd_clear()
            if len(message) > 16:
                display.lcd_display_string(message[0:16], 1)
                display.lcd_display_string(message[16:32], 2)
            else:
                display.lcd_display_string("Message:", 1)
                display.lcd_display_string(message, 2)
            if len(message) > 32:
                await ctx.channel.send(f'32 Character Max ({len(message)}):\nSent: {message[0:32]}')

    @tasks.loop(seconds= 1)
    async def button(self,button):
        if button.is_active:
            list_of_lines = lists.read('todo')
            lists.cycle_display(list_of_lines)


def setup(client):
    client.add_cog(Display(client))
