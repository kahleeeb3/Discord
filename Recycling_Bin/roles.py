import discord
from discord.ext import commands


class RoleMenu(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rolemenu(self,ctx):

        async def change_message(self):
            print('started loop')

            # waits for users next message
            enter_class = await channel.send('Type Class Name (or "none"):')
            new_class = await self.client.wait_for('message')
            await enter_class.delete()
            await new_class.delete()
            print(f'Entered Class: {new_class.content}')

            # if new message is 'end', stop loop
            if(new_class.content=="none"):
                print("ended loop")

            else:

                # waits for users next reaction
                enter_emoji = await channel.send('React With Class Emoji')
                new_class_emoji = await self.client.wait_for('reaction_add')
                await enter_emoji.delete()
                print(f'Class Emoji: {new_class_emoji[0]}')

                # assigns users message to 'original' message
                await original.edit(content= f'{original.content}\n \n{new_class_emoji[0]} : `{new_class.content}`' )
                await original.add_reaction(new_class_emoji[0])
                # run the loop again
                await change_message(self)

        # gets the channel command was typed in
        channel = ctx.channel
        #print(channel)
        # send original messsage
        original = await channel.send('**Classes for the Semester**\nReact to give yourself the role')
        # start the loop
        await change_message(self)
            




def setup(client):
    client.add_cog(RoleMenu(client))
