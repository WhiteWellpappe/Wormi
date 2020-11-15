# Libraries___________________________________________________________________________________________________________________________________________________________________________

# LINUX VERSION, AVOIDING LIBRARIES NOT AVAILABLE FOR LINUX
import discord, datetime, configparser, sys, json, os, asyncio
from discord.ext import commands
from discord.ext.commands import Bot, check, CheckFailure, command, HelpCommand

# Variables & Initialisation__________________________________________________________________________________________________________________________________________________________
bot = commands.Bot(command_prefix='!')

bot.load_extension('cogs.Fun')
bot.load_extension('cogs.Tools')
bot.load_extension('cogs.newAOO')
bot.load_extension('cogs.Calendar')
# bot.load_extension('cogs.YT') #WIP
bot.remove_command('help')  # Custom help command


# Program____________________________________________________________________________________________________________________________________________________________________________
@bot.event
async def on_ready():
    dt = datetime.datetime.now()
    print(dt.strftime("%d.%m.%Y %H:%M"))
    print(f'We have logged in as {bot.user}')
    print()
    # activity=discord.CustomActivity(name="hates Linux")
    activity = discord.Activity(name="hates linux", type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)


# Error handling
@bot.event
async def on_command_error(ctx, error):
    try:
        if ctx.guild.id == 717760982729883689:  # VpS
            channel = bot.get_channel(717774758149619743)
        elif ctx.guild.id == 530157406349688862:  # WgD
            channel = bot.get_channel(713320018984697956)
    except AttributeError:
        pass
    if isinstance(error, commands.CommandNotFound):
        if ctx.author.id == 517098993180868642:
            await ctx.send(
                f"Jeez {ctx.author.mention}, just look up <#722575695141929046> and stop bothering me with your weird requests.")
        else:
            await ctx.send(f"{ctx.author.mention} This command doesn't exist.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            f"{ctx.author.mention} I'm missing additional information/arguments to run the command. Try !help or ask around.")
    elif isinstance(error, commands.TooManyArguments):
        await ctx.send(f"{ctx.author.mention} There are to many arguments for this command. Try !help or ask around.")
    elif isinstance(error, commands.NoPrivateMessage):
        await ctx.send(f"{ctx.author.mention} This command can't be used in private channels.")
    elif isinstance(error, commands.MissingAnyRole):
        await ctx.send(f"{ctx.author.mention} You are missing the needed role to use this command.")
    elif isinstance(error, commands.CheckFailure):
        if ctx.guild.id == 530157406349688862:  # WgD
            await ctx.send(f"{ctx.author.mention} Please use {bot.get_channel(558632300737462272).mention}.")
        elif ctx.guild.id == 717760982729883689:  # VpS
            await ctx.send(f"{ctx.author.mention} Please use {bot.get_channel(717760982729883692).mention}.")
    else:
        await ctx.send(f"{ctx.author.mention} Something went wrong. :(")
        dt = datetime.datetime.now()
        print(dt.strftime("%d.%m.%Y %H:%M"))
        print(f'{ctx.command.name} was invoked incorrectly by {ctx.author.display_name}')
        print(error)
        print()
        try:
            await channel.send(f"{ctx.command.name} was invoked incorrectly by {ctx.author.display_name}\n{error}\n\n")
        except AttributeError:
            print("No channel found. Ctx is probably none")
        except UnboundLocalError:
            pass


# Welcoming new Members via DM, setting role to unverified
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'''Hello {member.mention}!
I'm Wormi, and you just joined {member.guild.name}'s discord server!
Please write a short message I can forward to the R4s.
This message should include your ingame name, so we can assign a proper rank to you and let you enjoy all these beautifull channels!
Additionally you should check out the lobby and change your nickname to avoid any confusion.

Please start your message with **!registration followed by your text**, else I wont recognize you are talking to me. You also can't send more than one message :(.
For example: !registration Hey Wormi, Im Wormi! Nice to meet you!''')
    server = await bot.fetch_guild(member.guild.id)
    if server.id == 717760982729883689:  # VpS
        role = server.get_role(719502497982447766)
    elif server.id == 530157406349688862:  # WgD
        role = server.get_role(643047153677369355)
    await member.add_roles(role)


# Forwarding PM to registration channel, removing unverified
@bot.command(name="registration", help="command for registration on discord, unverified role only")
async def registration(ctx, *, arg):
    server = await bot.fetch_guild(717760982729883689)
    member = await server.fetch_member(ctx.author.id)
    role = server.get_role(719502497982447766)
    if member.top_role == role:
        channel = bot.get_channel(717774509096042567)  # VpS(641262602730733568)WgD
        await channel.send(f'''Hey! {ctx.author.mention} has arrived! Here is a message for you!
{arg}''')
        await member.remove_roles(role)
        await ctx.send("Thank you! I forwarded your message.")
    else:
        await ctx.send(f"Role error. You need the role '{role}' in {server}")


@bot.event
async def on_member_remove(member):
    if member.guild.id == 717760982729883689:  # VpS
        channel = bot.get_channel(717774509096042567)
    elif member.guild.id == 530157406349688862:  # WgD
        channel = bot.get_channel(641262602730733568)
    await channel.send(f'{member.mention} ({member.display_name}) left the server.')


@bot.command(name="logout", help="Terminate Bot")
@commands.has_any_role('Discord King', 'Leader')
async def sysexit(ctx):
    await ctx.send(f'{ctx.author.mention} Bye!')
    await bot.logout()


@bot.command(name="updatejson")
@commands.has_any_role('Discord King', 'Leader')
async def update_json(ctx):
    dic = {}
    for member in ctx.guild.members:
        dic[member.display_name] = member.mention
    if ctx.guild.id == 717760982729883689:  # VpS
        with open('./memberVpS.json', 'w') as d:
            json.dump(dic, d)
            d.truncate()
        await ctx.send(f"{ctx.author.mention} JSON updated.")
    elif ctx.guild.id == 530157406349688862:  # WgD
        with open('./memberWgD.json', 'w') as d:
            json.dump(dic, d)
            d.truncate()
        await ctx.send(f"{ctx.author.mention} JSON updated.")


# WIP
@bot.command(name='help', help='Shows all commands')
async def CustomHelpCommand(ctx):
    embed = discord.Embed(
        colour=discord.Colour.gold(),
        title="Help")
    # sorting out all non-usable commands for calling user
    # total_commands=bot.commands
    # print(total_commands)
    # comm=await HelpCommand.filter_commands(total_commands, total_commands, sort=False, key=None) #ERROR Type=Set
    # print(comm)
    helptext1 = ""
    for command in bot.commands:
        if command.cog is None:
            if len(helptext1) > 1:
                helptext1 += f", `{command}`"
            else:
                helptext1 += f"`{command}`"
    embed.add_field(name=":bug: General", value=helptext1, inline=False)
    helptext2 = ""
    for command in bot.commands:
        if command.cog is not None:
            if command.cog.qualified_name == "newAOO":
                if len(helptext2) > 1:
                    helptext2 += f", `{command}`"
                else:
                    helptext2 += f"`{command}`"
    embed.add_field(name=":crossed_swords: Ark of Osiris:", value=helptext2, inline=False)
    helptext3 = ""
    for command in bot.commands:
        if command.cog is not None:
            if command.cog.qualified_name == "Fun":
                if len(helptext3) > 1:
                    helptext3 += f", `{command}`"
                else:
                    helptext3 += f"`{command}`"
    embed.add_field(name=":partying_face: Fun:", value=helptext3, inline=False)
    helptext4 = ""
    for command in bot.commands:
        if command.cog is not None:
            if command.cog.qualified_name == "Tools":
                if len(helptext4) > 1:
                    helptext4 += f", `{command}`"
                else:
                    helptext4 += f"`{command}`"
    embed.add_field(name=":tools: Tools:", value=helptext4, inline=False)
    helptext5 = ""
    for command in bot.commands:
        if command.cog is not None:
            if command.cog.qualified_name == "Calendar":
                if len(helptext5) > 1:
                    helptext5 += f", `{command}`"
                else:
                    helptext5 += f"`{command}`"
    if helptext5 == "":
        helptext5 = "Placeholder"
    embed.add_field(name=":calendar_spiral: Calendar:", value=helptext5, inline=False)
    await ctx.send(embed=embed)


@bot.command(name="restart", help="restart wormi, checking for updates")
@commands.has_any_role("Discord King")
async def restart(ctx):
    await ctx.send("Restarting. Please wait.")
    await bot.logout()
    try:
        os.system("cd /home/pi/Python/Wormi/\npython3.8 ./restart.py")
    except Exception:
        bot.run(token)


if __name__ == "__main__":
    # Checking for update
    try:
        file1 = open("version.txt", "r")
        version1 = int(file1.readline())
        file1.close()
        file2 = open("/home/pi/share/version.txt", "r")
        version2 = int(file2.readline())
        file2.close()
    except Exception:
        print(f"Error in update check\n{Exception}")
        # skipping update
        version1, version2 = 0, 0
    if not (version1 < version2):
        print("No update found.")
        # Token needed to access discord
        cp = configparser.ConfigParser()
        cp.read('./config.ini')
        token = cp.get('DEFAULT', 'token')
        bot.run(token)
    else:
        print("Update found. Starting update.py")
        try:
            os.system("cd /home/pi/Python/Wormi/\npython3.8 ./update.py")
        except Exception:
            print(f"update.py not found.\n{Exception}")
