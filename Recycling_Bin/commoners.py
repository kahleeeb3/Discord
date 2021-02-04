import discord
from discord.ext import commands
from itertools import cycle


class Common(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def commoners(self, ctx):

        await ctx.message.delete()
        join_message = await ctx.send(f'React here to request to be a Commoner')
        await join_message.add_reaction("✅")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if (payload.channel_id == 770018703697772596):
            if(payload.member.bot):
                pass
                #print('bob added reaction')
            else:
                if(payload.emoji.name == "✅"):
                    brown_id = 690005655389601811
                    brown = self.client.get_emoji(brown_id)

                    channel_id = payload.channel_id
                    channel = self.client.get_channel(channel_id)

                    court_soup_id= 768896233359802408
                    court_soup = channel.guild.get_channel(court_soup_id)

                

                    suggest_message = await court_soup.send(f'{payload.member.mention} would like to be a commoner')
                    await suggest_message.add_reaction(brown)
        


def setup(client):
    client.add_cog(Common(client))
