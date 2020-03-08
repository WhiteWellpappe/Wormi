#Libraries___________________________________________________________________________________________________________________________________________________________________________

#LINUX VERSION, AVOIDING LIBRARIES NOT AVAIBLE FOR LINUX

import os, random, discord, datetime, configparser, sys
from discord.ext import commands
from discord.ext.commands import Bot, check, CheckFailure, command
from openpyxl import Workbook, load_workbook


#Variables & Initialisation__________________________________________________________________________________________________________________________________________________________
random.seed()
bot=commands.Bot(command_prefix='!')

registered=0
bot.load_extension('cogs.Fun')
bot.load_extension('cogs.Tools')
bot.load_extension('cogs.AOO')
bot.load_extension('cogs.YT')

#Program____________________________________________________________________________________________________________________________________________________________________________
@bot.event
async def on_ready():
    DT=datetime.datetime.now()
    print(DT.strftime("%d.%m.%Y %H:%M"))
    print(f'We have logged in as {bot.user}')
    print()
    #activity=discord.CustomActivity(name="hates Linux")
    activity = discord.Activity(name="hates linux", type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)


#Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"{ctx.author.mention} This command doesnt exist.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.author.mention} I'm missing additional information/arguments to run the command. Try !help or just ask around.")
    elif isinstance(error, commands.TooManyArguments):
        await ctx.send(f"{ctx.author.mention} There are to many arguments for this command. Try !help or just ask around.")
    elif isinstance(error, commands.NoPrivateMessage):
        await ctx.send(f"{ctx.author.mention} This command can't be used in private channels.")
    elif isinstance(error, commands.MissingAnyRole):
        await ctx.send(f"{ctx.author.mention} You are missing the needed role to use this command.")
    else:
        await ctx.send(f"{ctx.author.mention} Something went wrong. :(")
        DT=datetime.datetime.now()
        print(DT.strftime("%d.%m.%Y %H:%M"))
        print(f'"', ctx.command.name, '" was invoked incorrectly by ', ctx.author.display_name, sep="")
        print(error)
        print()


#Welcoming new Members via DM, setting role to unverified
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'''Hello {member.mention}!
Im Wormi, and you just joined the [WgD] Discord Server!
Please write a short message I can forward to the Server Admins.
This message should include your Ingame name, so we can assign a proper rank to you and let you enjoy all these beautifull channels!
Additionally you could check out the lobby and change your nickname to avoid any confusion.

Please start your message with **!registration followed by your text**, else I wont recognize you are talking to me. You also can't send more than one message.
For example: !registration Hey, Im Wormi, nice to meet you!''')
    server= await bot.fetch_guild(530157406349688862)
    role=server.get_role(643047153677369355)
    await member.add_roles(role)

#Forwarding PM to registration channel, removing not-verified
@bot.command(name="registration", help="command for registration on discord, not-verified role only")
async def registration(ctx, *, arg):
    server= await bot.fetch_guild(530157406349688862)
    member=await server.fetch_member(ctx.author.id)
    role=server.get_role(643047153677369355)
    if member.top_role==role:
        channel = bot.get_channel(641262602730733568)
        await channel.send(f'''Hey! {ctx.author.mention} has arrived! Here is a message for you!
{arg}''')
        await member.remove_roles(role)
        await ctx.send("Thank you! I forwarded your message.")
    else:
        await ctx.send(f"Role error. You need the role '{role}' in {server}")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(641262602730733568)
    await channel.send(f'{member.mention} left the server.')


@bot.command(name="sys.exit", help="Close Bot")
async def quit(ctx):
    await ctx.send(f'{ctx.author.mention} Bye!')
    sys.exit(0)


#WIP
async def DefaultHelpCommand(dm_help=True):
    pass


#@bot.command(name="test")
#@commands.has_any_role('Discord King')
#async def test(ctx):
    #await ctx.channel.purge(limit=5)
    #await ctx.send(file=discord.File('pics\woody.jpg'))


#Token needed to access discord
cp=configparser.ConfigParser()  
#cp.read('/home/nico/Python/Wormi/config.ini') #Linux
cp.read('D:/Systemzeuchs/Python/Wormi/config.ini') #Windows
token=cp.get('DEFAULT', 'token')
bot.run(token)