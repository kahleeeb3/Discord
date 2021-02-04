import discord
from discord.ext import commands
import os
from github import Github



class ChatLog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def log(self, ctx, command):
        
        
        async def log_message(next_message):
            print(f'Logging: {next_message.content}')
            log = open("./cogs/chatlog/log.txt", "a")
            log.write(f'{next_message.author} : {next_message.content}\n')
            log.close()

        def find_files():
            for folder in os.listdir('./cogs/chatlog/'):
                print(folder)

        async def read_log():
            file_directory = "./cogs/chatlog/log.txt"
            num_lines = sum(0 for line in open(file_directory))
            
            f = open(file_directory)
            lines=f.readlines()

            i = 1
            stuff = ""
            while i < 6:
                stuff = f'{stuff}{lines[num_lines-i]}'
                i += 1

            return stuff

        def break_loop():
            print('stopped logging')

        async def wait_for_message():
            skip_list ={'$log end', '$log status', '$log upload', '$log read'}
            next_message = await self.client.wait_for('message')
            
            if(next_message.content == '$log read'):
                log = await read_log()
                await ctx.channel.send(f'{log}')
                await wait_for_message()
            
            if(next_message.content == '$log status'):
                await ctx.channel.send('Currently Logging')
                await wait_for_message()

            if(next_message.content == '$log upload'):
                await ctx.channel.send('Status: Logging')
                log = await read_log()
                await upload_github(log)
                await wait_for_message()

            elif(next_message.guild == guild):
                if(next_message.content not in skip_list):
                    await log_message(next_message)
                    await wait_for_message()
            else:
                await wait_for_message()

        async def upload_github(message):
            g = Github("kahleeeb3", "Willisamotherfuckingcunt24")
            for repo in g.get_user().get_repos():
                #print(repo.name)
                if repo.name == "discordtestbot":
                    my_repo = repo
            contents = my_repo.get_contents("test.txt")
            my_repo.update_file(contents.path, "Label of push", message, contents.sha, branch="main")
            #await ctx.channel.send('Upload: True')
            

        if command == 'start':
            guild = ctx.message.guild
            await ctx.message.delete()
            await ctx.channel.send('Now logging all messages in Guild')
            await wait_for_message()
        if command == 'end':
            await ctx.channel.send('Status: Not Logging')
            pass
            

        


def setup(client):
    client.add_cog(ChatLog(client))
