#Libraries___________________________________________________________________________________________________________________________________________________________________________

#LINUX VERSION, AVOIDING LIBRARIES NOT AVAIBLE FOR LINUX

import discord, datetime, configparser, sys, json
from discord.ext import commands
from discord.ext.commands import Bot, check, CheckFailure, command, HelpCommand


#Variables & Initialisation__________________________________________________________________________________________________________________________________________________________
bot=commands.Bot(command_prefix='!')

bot.load_extension('cogs.Fun')
bot.load_extension('cogs.Tools')
bot.load_extension('cogs.AOO')
bot.load_extension('cogs.YT') #WIP
bot.remove_command('help') #Custom help command


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
        await ctx.send(f"{ctx.author.mention} I'm missing additional information/arguments to run the command. Try !help or ask around.")
    elif isinstance(error, commands.TooManyArguments):
        await ctx.send(f"{ctx.author.mention} There are to many arguments for this command. Try !help or ask around.")
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


@bot.command(name="sys.exit", help="Terminate Bot")
@commands.has_any_role('Discord King', 'Leader')
async def sysexit(ctx):
    await ctx.send(f'{ctx.author.mention} Bye!')
    sys.exit(0)


@bot.command(name="updatejson")
@commands.has_any_role('Discord King', 'Leader')
async def update_json(ctx):
    memlist=ctx.guild.members
    dic={}
    for mem in memlist:
        dic[mem.display_name]=mem.mention
    with open ('./member.json', 'w') as d:
        json.dump(dic, d)
        d.truncate()
    await ctx.send(f"{ctx.author.mention} JSON updated.")


#WIP
@bot.command(name='help', help='Shows all commands')
async def CustomHelpCommand(ctx):
    embed=discord.Embed(
        colour=discord.Colour.gold(),
        title= "Help")
    #sorting out all non-usable commands for calling user
    total_commands=bot.commands
    print(total_commands)
    comm=await HelpCommand.filter_commands(total_commands, total_commands, sort=False, key=None) #ERROR Type=Set
    print(comm)
    helptext1=""
    for command in comm:
        if command.cog==None:
            if len(helptext1)>1:
                helptext1+=f", `{command}`"
            else:
                helptext1 +=f"`{command}`"
    embed.add_field(name=":bug: General", value=helptext1, inline=False)
    helptext2=""
    for command in comm:
        if command.cog!=None:
            if command.cog.qualified_name=="AOO":
                if len(helptext2)>1:
                    helptext2+=f", `{command}`"
                else:
                    helptext2+=f"`{command}`"
    embed.add_field(name=":crossed_swords: Ark of Osiris:", value=helptext2, inline=False)
    helptext3=""
    for command in comm:
        if command.cog!=None:
            if command.cog.qualified_name=="Fun":
                if len(helptext3)>1:
                    helptext3+=f", `{command}`"
                else:
                    helptext3+=f"`{command}`"
    embed.add_field(name=":partying_face: Fun:", value=helptext3, inline=False)
    helptext4=""
    for command in comm:
        if command.cog!=None:
            if command.cog.qualified_name=="Tools":
                if len(helptext4)>1:
                    helptext4+=f", `{command}`"
                else:
                    helptext4+=f"`{command}`"
    embed.add_field(name=":tools: Tools:", value=helptext4, inline=False)
    await ctx.send(embed=embed)


#Token needed to access discord
cp=configparser.ConfigParser()  
cp.read('./config.ini')
token=cp.get('DEFAULT', 'token')
bot.run(token)