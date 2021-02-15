import discord
from discord.ext import commands, tasks
import datetime
import pytz

from modules import lists, time


class ToDo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def todo(self,ctx,action):

        if action == 'add':
            menu = await ctx.send(f'What would you like to add?')
            new_info = await self.client.wait_for('message')
            await new_info.delete()
            lists.add('todo',new_info)
            #reads new content of text file
            content = lists.to_string('todo')
            #edits the menu
            await menu.edit(content=content)
   
        if action == 'edit':
            #send the current list
            content = lists.to_string('todo')
            menu = await ctx.channel.send(f'{content}**Input text to replace:**')
            #ask for input on the new list
            new_list = await self.client.wait_for('message')
            #make changes to text file
            lists.edit('todo',new_list.content)
            await new_list.delete()
            #reads new content of text file
            content = lists.to_string('todo')
            #edits the menu
            await menu.edit(content=content)

        if action == 'delete':
            #reads content of text file
            content = lists.to_string('todo')
            #select item to delete
            menu = await ctx.channel.send(content + '**Which line would you like to delete? (Int)**')
            choice = await self.client.wait_for('message')
            await choice.delete()
            selection = int(choice.content) - 1
            #edits the file
            lists.delete('todo',selection)
            #reads new content of text file
            content = lists.to_string('todo')
            #edits the menu
            await menu.edit(content=content)

        if action == 'list':
            content = lists.to_string('todo')
            await ctx.send(content)


def setup(client):
    client.add_cog(ToDo(client))
