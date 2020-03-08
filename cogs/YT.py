import discord, youtube_dl
from discord import FFmpegPCMAudio
from discord.ext import commands

youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {'format': 'bestaudio/best', 'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s', 'restrictfilenames': True, 'noplaylist': True,
    'nocheckcertificate': True, 'ignoreerrors': False, 'logtostderr': False, 'quiet': True, 'no_warnings': True, 'default_search': 'auto', 'source_address': '0.0.0.0'} #bind to ipv4 since ipv6 addresses cause issues sometimes
ffmpeg_options = {'options': '-vn'}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

def setup(bot):
    bot.add_cog(YT(bot))


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=1):
        super().__init__(source, volume)

        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class YT(commands.Cog, name='Youtube'):
    def __init__(self, bot):
        self.bot = bot
    
    async def dc(self, bot):
        await self.bot.voice_clients.disconnect()
    
    @commands.Cog.listener()
    async def on_message(self, message):
        url=str(message.content)
        vc=self.bot.get_channel(636503430017449985)

        if message.author.bot:
            return

        elif message.channel.id==682176530163433499:
            if self.bot.voice_clients:
                pass
            else:
                await vc.connect()
            vid = await YTDLSource.from_url(url, loop=self.bot.loop) #stream=True)
            lvc=self.bot.voice_clients
            lvc=lvc[0]
            lvc.play(vid, after=lambda e: print('Player error: %s' % e) if e else None)
            #await lvc.disconnect()