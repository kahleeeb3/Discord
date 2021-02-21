import discord
from discord.ext import commands


class NotHorny(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands

    @commands.command(aliases = ['nh'])
    async def nothorny(self, ctx, victim):

        message = ctx.message
        guild = message.guild
        role = discord.utils.get(guild.roles, name ='Horny Ass')
        role2 = discord.utils.get(guild.roles, name ='Super Horny')


        async def empty_role(role):

            if not role.members:
                await role.delete()

        async def remove(message,role):
            if message.mention_everyone:
                for x in role.members:
                    await x.remove_roles(role)
            else:
                victim = message.mentions
                for x in victim:
                    #if user is horny, remove
                    if role in x.roles:
                        await x.remove_roles(role)

        if role != None:
            await remove(message,role)
            await empty_role(role)
        if role2 != None:
            await remove(message,role2)
            await empty_role(role2)

        if message.mention_everyone:
            await message.channel.send(f'Group Ejaculation!!!')



def setup(client):
    client.add_cog(NotHorny(client))
