import discord
from discord.ext import commands
from modules.json import json


async def send_count(ctx, person):
    # Step 1: load in the data
    data = json.load("miss")

    # Step 2: Send the data
    try:
        data = data["member"][f'{person.name}']
        embed = discord.Embed(title=f'Miss Count: {data["count"]}',color=discord.Color.red())
        embed.set_author(name=f"{person}", icon_url=f"{person.avatar_url}")
        for case in data["cases"]:

            details = data["cases"][case]
            day = details["day"]
            date = details["date"]
            time = details["time"]

            embed.add_field(name=f'{case}. {date}',value = f'{day} at {time}', inline=False)

        await ctx.send(embed=embed)
    except:
        await ctx.channel.send('This person has never missed')

async def send_new_count(ctx, person):
    # Step 1: load in the data
    data = json.load("miss")

    # Step 2: Send the data
    data = data["member"][f'{person.name}']
    embed = discord.Embed(title=f'Miss Count: {data["count"]}',color=discord.Color.red())
    embed.set_author(name=f"{person}", icon_url=f"{person.avatar_url}")
    numCases = len(data["cases"])

    details = data["cases"][str(numCases)]
    day = details["day"]
    date = details["date"]
    time = details["time"]

    embed.add_field(name=f'{date}',value = f'{day} at {time}', inline=False)

    await ctx.send(embed=embed)

class Counter(commands.Cog):
    """Keeps count of the number of times a thing occurs"""

    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def miss(self, ctx, user, *option):
        """Adds +1 to a members miss count
        `$miss @<user> <null|list|reset>`"""
        # Step 1: load in the data or create the file
        data = json.load('miss')
        try:
            data["member"]
        except:
            data= {"member":{}}
            json.edit("miss",data)

        # Step 2: Determine which person to target
        if not ctx.message.mentions or len(ctx.message.mentions)> 1:
            await ctx.channel.send('Please mention the member who is miss')
        else:
            person = ctx.message.mentions[0].name

            if not option:
                # Step 3: add 1 to their counter 
                try:
                    data["member"][f'{person}']['count'] = data["member"][f'{person}']['count'] + 1
                    caseNum = len(data["member"][f'{person}']['cases']) + 1
                except:
                    data["member"][f'{person}'] = {"count": 1,"cases":{}}
                    caseNum = 1

                
                # Step 3: get new data
                from modules import time
                cases = data["member"][f'{person}']['cases']
                now = time.curr_time()
                day = now[0]
                time = now[1]
                date = now[2]
                newCase = {
                        "day": f"{day}",
                        "date": f"{date}",
                        "time": f"{time}"
                        }
                cases[f'{caseNum}'] = newCase

                # Step 4: Add the data
                json.edit("miss",data)

                person = ctx.message.mentions[0]
                await send_new_count(ctx, person)

            else:
                if option[0]=='list':
                    person = ctx.message.mentions[0]
                    await send_count(ctx, person)
                elif option[0]== 'reset':
                    if ctx.message.author.name == 'CalebP': 
                        data["member"][f"{person}"] = {}
                        json.edit("miss",data)
                        await ctx.channel.send(f'Reset {person}\'s counter to 0')
                    else:
                        await ctx.channel.send(f'Only Caleb can reset the counter')
                else:
                    await ctx.channel.send('Please type `$miss @<user> <list/reset>`')

def setup(client):
    client.add_cog(Counter(client))

