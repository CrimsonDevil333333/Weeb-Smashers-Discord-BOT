import asyncio
import youtube_dl
import discord
from discord.ext import commands
import os

try:
    if not discord.opus.is_loaded():
        discord.opus.load_opus('libopus.so')
        print("its added")
    else:
        print("already there")
except:
    print("erorr came maybe its allready loaded or file is not here ")

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': 'music_cache',
    #+'.%(ext)s'
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()
        await ctx.send(f"Joined :- {channel}")

    @commands.command()
    async def play(self, ctx, *, query):
        """Plays a file from the local filesystem"""
        
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('song/'+query))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
        if query == '1':
            await ctx.send('Now playing: {}'.format("Marshmello & Halsey - Be Kind"))
        if query == "2":
            await ctx.send('Now playing: {}'.format("Ali Gatie - What If I Told You That I Love You"))
        if query == "3":
            await ctx.send('Now playing: {}'.format("Brand New Day by (Rei Yasuda) "))
        if query == "4":
            await ctx.send('Now playing: {}'.format("R3HAB, HRVY - Be Okay"))

    @commands.command()
    async def yt(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""
        if os.path.exists('music_cache'):
            print("cache is being removed ...")
            os.remove("music_cache")
            print("cache is removed!")
        else:
            print("cache dosn't exist yet")
        await ctx.send("Lemme get files ready 😶")
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format(player.title))

    @commands.command()
    async def stream(self, ctx, *, url):
        """Streams from a url (same as yt, but doesn't predownload)"""
        await ctx.send("Lemme get files ready 😶")
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now Streaming: {}'.format(player.title))

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send("Changed volume to {}%".format(volume))

    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()
        await ctx.send("Music is now stoped!")

    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()