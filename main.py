import discord
from discord.ext import commands
import youtube_dl
import os
import asyncio

DISCORD_TOKEN = "MTAyNjIzOTk1MzE2MTY4Mjk0NQ.G8QMtT.y1-RXvr2T2tW4Ug7hiTaKtYP9RkpmVZ2ZSGThs"

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix='!', intents=intents)

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
    'socket_timeout': 20
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

if not discord.opus.is_loaded():
    opus_path = '/opt/homebrew/Cellar/opus/1.5.2/lib/libopus.0.dylib'
    discord.opus.load_opus(opus_path)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')
        self.filename = data['filepath']

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=True))

        if 'entries' in data:
            data = data['entries'][0]

        filename = ytdl.prepare_filename(data)
        data['filepath'] = filename
        return cls(discord.FFmpegPCMAudio(executable="ffmpeg", source=filename, **ffmpeg_options), data=data)

    async def cleanup(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

queue = []
current_player = None

async def play_next(ctx):
    global current_player
    if queue:
        url = queue.pop(0)
        try:
            player = await YTDLSource.from_url(url, loop=bot.loop, stream=False)
            current_player = player
            ctx.voice_client.play(player, after=lambda e: bot.loop.create_task(play_next(ctx)))
            await ctx.send(f'**Now playing:** {player.title}')
            while ctx.voice_client and (ctx.voice_client.is_playing() or ctx.voice_client.is_paused()):
                await asyncio.sleep(1)
            await player.cleanup()
        except Exception as e:
            print(f'Error playing {url}: {e}')
            await ctx.send(f'Error playing {url}: {e}')
            await play_next(ctx)
    else:
        if ctx.voice_client:
            await ctx.voice_client.disconnect()

@bot.command(name='join', help='Bot join voice chat')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send(f"{ctx.message.author.name} not connected to a voice channel")
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='Bot leave voice chat')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("bot is not connected to a voice channel")

@bot.command(name='play', help='play a music on voice chat')
async def play(ctx, url):
    queue.append(url)
    if not ctx.voice_client.is_playing():
        await play_next(ctx)
    else:
        await ctx.send(f'**Add to queue:** {url}')

@bot.command(name='pause', help='Stop music on voice chat')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client and voice_client.is_playing():
        voice_client.pause()
        await ctx.send("The music has been paused.")
    else:
        await ctx.send("The bot is not playing")

@bot.command(name='resume', help='Resume music on voice chat')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client and voice_client.is_paused():
        voice_client.resume()
        await ctx.send("The music has been resumed.")
    else:
        await ctx.send("The bot is not playing")

@bot.command(name='stop', help='Stop music on voice chat')
async def stop(ctx):
    global current_player
    voice_client = ctx.message.guild.voice_client
    if voice_client and voice_client.is_playing():
        voice_client.stop()
        await ctx.send("The music has been stopped")
    else:
        await ctx.send("The bot is not playing")
    if current_player:
        await current_player.cleanup()
        current_player = None
    for url in queue:
        try:
            data = await bot.loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
            filename = ytdl.prepare_filename(data)
            if os.path.exists(filename):
                os.remove(filename)
        except Exception as e:
            print(f'Error cleaning {url}: {e}')
    queue.clear()

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} has connected to Discord!')

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
