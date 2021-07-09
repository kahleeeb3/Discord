import discord
from discord.ext import commands, tasks

from modules import lists, drivers

async def display(ctx,message):
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