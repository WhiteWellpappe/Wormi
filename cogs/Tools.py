import datetime, json, discord
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
    @commands.command(name="kickinactive", help="kicks all inactive, roleless members (>30d)")
    @commands.has_any_role('Discord King', 'Leader', 'Officer')
    async def kickinactive (self, ctx):
        count=await ctx.prune_members(self, ctx, days=30, compute_prune_count=True, reason="You were inactive for 30 or more days. Hit us up when you are back!")
        await ctx.send(f"{ctx.author.mention} I kicked {count} members.")
    
    #Kicking all inactive members (>30d)
    @commands.command(name="checkinactive", help="check for inactive (>30d)")
    @commands.has_any_role('Discord King', 'Leader', 'Officer')
    async def checkinactive (self, ctx):
        count=await ctx.guild.estimate_pruned_members(days=30)
        await ctx.send(f"{ctx.author.mention} {count} members are inactive.")

    #Giving pairing suggestions based on keyword
    @commands.command(name="pairing", help="Keyword needed, gives suggestions")
    async def pairing(self, ctx, keyword):
        result=""
        embed=discord.Embed(
            colour=discord.Colour.gold(),
            title= "Pairings"
        )
        with open ("./pairings.json", "r") as p:
            dic=json.load(p)
        for pairing, key in dic.items():
            if keyword.lower() in key.lower():
                result+=pairing+"\n"
        embed.add_field(name="Result", value=f"{result}", inline=False)
        if result!="":
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{ctx.author.mention} No pairings found.")
