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

    #Kicking all inactive members (>45d)
    @commands.command(name="kickinactive", help="kicks all inactive, roleless members (>45d)")
    @commands.has_any_role('Discord King', 'Leader', 'Officer')
    async def (self, ctx):
        count=await ctx.prune_members(self, ctx, 45, compute_prune_count=True, reason="You were inactive for 45 or more days. Hit us up when you are back!")
        await ctx.send(f"{ctx.author.mention} I kicked {count} members.")
    
    #Kicking all inactive members (>45d)
    @commands.command(name="checkinactive", help="check for inactive (>45d)")
    @commands.has_any_role('Discord King', 'Leader', 'Officer')
    async def (self, ctx):
        count=await ctx.guild.estimate_pruned_members(*, 45)
        await ctx.send(f"{ctx.author.mention} {count} members are inactive.")  
