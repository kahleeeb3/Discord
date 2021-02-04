import discord
from discord.ext import commands


class DeletedMessage(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        #print('message deleted')
        send_channel_id = 768896250195738675
        send_channel = self.client.get_channel(send_channel_id)

        if(payload.cached_message.author.bot):
            pass
        elif(payload.user.id == 689673863008747553):
            pass
        else:
            await send_channel.send(f"""`Deleted Message:`\n{payload.cached_message.content}\n`{payload.cached_message.author}: {payload.cached_message.channel}`""")


def setup(client):
    client.add_cog(DeletedMessage(client))