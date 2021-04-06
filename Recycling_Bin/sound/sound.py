import discord
from discord.ext import commands
from gtts import gTTS

def speak(phrase):
    tts = gTTS(text = phrase, lang = 'en')
    audio_file = 'audio.mp3'
    tts.save(f'/home/pi/Desktop/Discord/cogs/sound/{audio_file}')

class Sound(commands.Cog):
    """A series of commands to make the bot speak"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, *, stuff):
        """Sends data to Bots Speaker in Calebs room"""

        import os
        speak(f'{stuff}.')
        os.system('omxplayer -o local /home/pi/Desktop/Discord/cogs/sound/audio.mp3')
        

def setup(client):
    client.add_cog(Sound(client))
