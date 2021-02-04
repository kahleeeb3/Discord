import discord
from discord.ext import commands


class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self,message):
        
        
        async def change_message(self):
            print('started loop')

            # waits for users next message
            new_content = await self.client.wait_for('message')

            # if new message is 'end', stop loop
            if(new_content.content=="end"):
                print("ended loop")
                # delets message user sent
                await new_content.delete()

            else:

                # assigns users message to 'original' message
                await original.edit(content= f'{original.content}\n `{new_content.author}`: `{new_content.content}`' )
                # delets message user sent
                await new_content.delete()
                # run the loop again
                await change_message(self)
        
        #type $test to begin
        if message.content.startswith('$test'):
            # gets the channel command was typed in
            channel = message.channel
            # send original messsage
            original = await channel.send('New Messages Go Here:')
            # start the loop
            await change_message(self)




def setup(client):
    client.add_cog(Test(client))
