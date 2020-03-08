import datetime
from discord.ext import commands

def setup(bot):
    bot.add_cog(Tools(bot))

class Tools(commands.Cog, name='Tools'):
    def __init__(self, bot):
        self.bot = bot
    
    #Servertime
    @commands.command(name="utc", help="shows current utc time")
    async def utc (self, ctx):
        DT="It's "+datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M")+" UTC"
        await ctx.send(DT)