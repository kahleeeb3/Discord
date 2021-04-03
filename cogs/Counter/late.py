import discord
from discord.ext import commands
from modules import time
import json

now = time.curr_time()


async def send_count(ctx, person):
    # Step 1: load in the data
    a_file = open("./cogs/Counter/data_file.json", "r")
    data = json.load(a_file)
    a_file.close()

    # Step 2: Send the data
    try:
        data = data["member"][f'{person.name}']
        embed = discord.Embed(title=f'Late Count: {data["count"]}',color=discord.Color.red())
        embed.set_author(name=f"{person}", icon_url=f"{person.avatar_url}")
        for case in data["cases"]:

            details = data["cases"][case]
            day = details["day"]
            date = details["date"]
            time = details["time"]

            embed.add_field(name=f'{case}. {date}',value = f'{day} at {time}', inline=False)

        await ctx.send(embed=embed)
    except:
        await ctx.channel.send('This person has never been late')

async def send_new_count(ctx, person):
    # Step 1: load in the data
    a_file = open("./cogs/Counter/data_file.json", "r")
    data = json.load(a_file)
    a_file.close()

    # Step 2: Send the data
    data = data["member"][f'{person.name}']
    embed = discord.Embed(title=f'Late Count: {data["count"]}',color=discord.Color.red())
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
    async def late(self, ctx, user, *option):
        """Adds +1 to a members late count
        `$late @<user> <null|list|reset>`"""
        # Step 1: load in the data or create the file
        try:
            a_file = open("./cogs/Counter/data_file.json", "r")
            data = json.load(a_file)
            a_file.close()
        except:
            data = {"member":{}}
            a_file = open("./cogs/Counter/data_file.json", "w")
            json.dump(data, a_file)
            a_file.close()

        # Step 2: Determine which person to target
        if not ctx.message.mentions or len(ctx.message.mentions)> 1:
            await ctx.channel.send('Please mention the member who is late')
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
                cases = data["member"][f'{person}']['cases']
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
                count = data["member"][f'{person}']['count']
                a_file = open("./cogs/Counter/data_file.json", "w")
                json.dump(data, a_file)
                a_file.close()

                person = ctx.message.mentions[0]
                await send_new_count(ctx, person)

            else:
                if option[0]=='list':
                    person = ctx.message.mentions[0]
                    await send_count(ctx, person)
                elif option[0]== 'reset':
                    if ctx.message.author.name == 'CalebP': 
                        data["member"][f"{person}"] = {}
                        a_file = open("./cogs/Counter/data_file.json", "w")
                        json.dump(data, a_file)
                        a_file.close()
                        await ctx.channel.send(f'Reset {person}\'s counter to 0')
                    else:
                        await ctx.channel.send(f'Only Caleb can reset the counter')
                else:
                    await ctx.channel.send('Please type `$late @<user> <list/reset>`')

def setup(client):
    client.add_cog(Counter(client))

