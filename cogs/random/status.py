import discord
from discord.ext import commands


class ChangeStatus(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def status(self, ctx, choice, *, new_status):

        status_type = discord.ActivityType.unknown
        
        if choice == 'w':
            # Setting 'watching' type
            status_type = discord.ActivityType.watching
        elif choice == 'p':
            # Setting 'play' type
            status_type = discord.ActivityType.streaming
        elif choice == 'l':
            # Setting 'listening' type
            status_type = discord.ActivityType.listening
        elif choice == 'c':
            # Setting 'competing in' type
            status_type = discord.ActivityType.competing            

        await self.client.change_presence(activity=discord.Activity(type = status_type, name = f'{new_status}') )
def setup(client):
    client.add_cog(ChangeStatus(client))
