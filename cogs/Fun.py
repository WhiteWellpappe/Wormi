import random, discord, os, re, json, asyncio, configparser
from discord.ext import commands
from googleapiclient.discovery import build

random.seed()

def setup(bot):
    bot.add_cog(Fun(bot))


class Fun(commands.Cog, name='Fun'):
    def __init__(self, bot):
        self.bot = bot

    def checkchannel(self):
        if self.guild.id == 717760982729883689:  # Vps
            return self.channel.id == 717760982729883692
        elif self.guild.id == 530157406349688862:  # WgD
            return self.channel.id == 558632300737462272

    @commands.Cog.listener()
    async def on_message(self, message):
        m = str(message.content)
        if message.author.bot:
            return
        elif message.author.id == '547508375592632330':
            if random.randint(1, 6) == 5:
                await message.channel.send(
                    f"{message.author.mention} Hey, I heard you wish to kill me? BRING IT ON BITCH!")
        elif message.channel.id == 558632300737462272 or message.channel.id == 717760982729883692:
            if ("Wormi" in m) or ("wormi" in m):
                if "show" in m:
                    if ("lama" in m) or ("alpaca" in m):
                        pool = os.listdir('./pics/lama')
                        image = random.choice(pool)
                        path = './pics/lama/' + image
                        await message.channel.send(f"{message.author.mention}")
                        await message.channel.send(file=discord.File(path))
                    elif "pizza" in m:
                        pool = os.listdir('./pics/pizza')
                        image = random.choice(pool)
                        path = './pics/pizza/' + image
                        await message.channel.send(f"{message.author.mention}")
                        await message.channel.send(file=discord.File(path))
                    elif "senor" in m:
                        path = './pics/hardjan/senor_hardjan.png'
                        await message.channel.send(f"{message.author.mention}")
                        await message.channel.send(file=discord.File(path))
                    elif ("pet" in m) or ("moral" in m):
                        pool = os.listdir('./pics/pet')
                        image = random.choice(pool)
                        path = './pics/pet/' + image
                        await message.channel.send(f"{message.author.mention}")
                        await message.channel.send(file=discord.File(path))

    @commands.command(name='8ball', help='Magic 8 Ball, Wormi answers any question')
    async def magic8ball(self, ctx):
        answer = ['It is as certain as WW is awesome.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.',
                  'You may rely on it.', 'As I see it, yes.', 'Most likely.',
                  'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.',
                  'Better not tell you now.', 'Cannot predict now, better ask Meg.', 'Concentrate and ask again.',
                  "Don't count on it.", 'My reply is no.', 'LOL, you wish.', 'Outlook not so good.', 'Nah.']
        response = random.choice(answer)
        await ctx.send(f"{ctx.author.mention} {response}")

        # RPS Paper

    @commands.command(name="paper", help="Paper for RPS")
    async def paper(self, ctx):
        x = random.randint(1, 3)
        await ctx.send(f"{ctx.author.mention} Scissor! I won! :)") if x == 1 else None
        await ctx.send(f"{ctx.author.mention} Rock! I lost! :(") if x == 2 else None
        await ctx.send(f"{ctx.author.mention} Paper! A tie!") if x == 3 else None

    # RPS Rock
    @commands.command(name="rock", help="Rock for RPS")
    async def rock(self, ctx):
        x = random.randint(1, 3)
        await ctx.send(f"{ctx.author.mention} Paper! I won! :)") if x == 1 else None
        await ctx.send(f"{ctx.author.mention} Scissor! I lost! :(") if x == 2 else None
        await ctx.send(f"{ctx.author.mention} Rock! A tie!") if x == 3 else None

    # RPS Scissor
    @commands.command(name="scissor", help="Scissor for RPS")
    async def scissor(self, ctx):
        x = random.randint(1, 3)
        await ctx.send(f"{ctx.author.mention} Rock! I won! :)") if x == 1 else None
        await ctx.send(f"{ctx.author.mention} Paper! I lost! :(") if x == 2 else None
        await ctx.send(f"{ctx.author.mention} Scissor! A tie!") if x == 3 else None

    # J4F
    @commands.command(name="smash", help="smash?")
    async def smash(self, ctx):
        x = random.randint(1, 50)
        await ctx.send(f"{ctx.author.mention} I have a wormfriend.") if x == 10 else await ctx.send(
            f"{ctx.author.mention} No.")

    # Custom Dice rolls
    @commands.command(name="roll", help="rolls XdY dice")
    async def roll(self, ctx, arg):
        rlist, erg = ('', 0)
        try:
            arg = str(arg)
        except:
            await ctx.send("Converting Error Dice Count - Please use a valid number.")
        x = arg.find("d")
        arg1, arg2 = (arg[:x], arg[x + 1:])
        try:
            arg1 = int(arg1)
            arg2 = int(arg2)
        except:
            await ctx.send("Converting Error Dice Size - Please use a valid number.")
        if arg1 > 100:
            await ctx.send(
                f"{ctx.author.mention} Please don't roll so much dice, I don't have big enough hands! Wait .... what?")
        elif arg2 > 300:
            await ctx.send(f"{ctx.author.mention} Please don't roll such big dice, I can't read the numbers anymore!")
        else:
            for _ in range(0, arg1):
                rlist = rlist + "+" if rlist != "" else None
                r = random.randint(1, arg2)
                rlist = rlist + str(r)
                erg = erg + r
            await ctx.send(f"{ctx.author.mention} {rlist} = {erg}")

    # Trolling Woody
    @commands.command(name="piney", aliases=["woody", "Piney", "Woody"], help="just to troll woody")
    @commands.check(checkchannel)
    async def piney(self, ctx):
        woody = ctx.guild.get_member(548926176316358657)
        path = "./pics/woody.jpg"
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Woody", description=f"{woody.mention}", color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(f"{woody.mention}", file=image, embed=embed)

    # Trolling Deedee
    @commands.command(name="deedee", aliases=["dee", "Dee", "DeeDee", "Deedee"], help="revenge for woody")
    @commands.check(checkchannel)
    async def deedee(self, ctx):
        deedee = ctx.guild.get_member(548924284836380698)
        pool = os.listdir('./pics/deedee')
        image = random.choice(pool)
        path = './pics/deedee/' + image
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Deedee", description=f"{deedee.mention}", color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(f"{deedee.mention}", file=image, embed=embed)

    # Trolling Ada
    @commands.command(name="ada", help="revenge for woody")
    @commands.check(checkchannel)
    async def ada(self, ctx):
        ada = ctx.guild.get_member(541287316769996800)
        pool = os.listdir('./pics/ada')
        image = random.choice(pool)
        path = './pics/ada/' + image
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Ada", description=f"{ada.mention}", color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(f"{ada.mention}", file=image, embed=embed)

    # Trolling Nana/Lucky
    @commands.command(name="nana", help="no idea")
    @commands.check(checkchannel)
    async def nana(self, ctx):
        lucky = ctx.guild.get_member(602110022394052618)
        path = "./pics/nana.jpg"
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Nana", description=f"{lucky.mention} behave!", color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(f"{lucky.mention}", file=image, embed=embed)

    @commands.command(name="lama", aliases=["Lama"], help="random lama")
    @commands.check(checkchannel)
    async def lama(self, ctx):
        pool = os.listdir('./pics/lama')
        image = random.choice(pool)
        path = './pics/lama/' + image
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Lama", description=f"{ctx.author.mention}", color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=image, embed=embed)

    @commands.command(name="pet", aliases=["Pet"], help="random WgD moral support")
    @commands.check(checkchannel)
    async def pet(self, ctx):
        pool = os.listdir('./pics/pet')
        image = random.choice(pool)
        path = './pics/pet/' + image
        imagename = image
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Moral support",
                              description=f"Moral support arrived {ctx.author.mention}! I am showing {imagename}",
                              color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=image, embed=embed)

    @commands.command(name="hardjan", aliases=["Hardjan", "Hard"], help="deedee's rok bf")
    @commands.check(checkchannel)
    async def hardjan(self, ctx):
        hardjan = ctx.guild.get_member(341379990228697090)
        pool = os.listdir('./pics/hardjan')
        image = random.choice(pool)
        path = './pics/hardjan/' + image
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Hardjan", description=f"{hardjan.mention} aka Deedee's RoK boyfriend",
                              color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(f"{hardjan.mention}", file=image, embed=embed)

    @commands.command(name="pizza", aliases=["Pizza"], help="random pizza")
    @commands.check(checkchannel)
    async def pizza(self, ctx):
        pool = os.listdir('./pics/pizza')
        image = random.choice(pool)
        path = './pics/pizza/' + image
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Pizza", description=f"{ctx.author.mention}", color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=image, embed=embed)

    @commands.command(name="tp", help="some toilet paper")
    @commands.check(checkchannel)
    async def tp(self, ctx):
        pool = os.listdir('./pics/tp')
        image = random.choice(pool)
        path = './pics/tp/' + image
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="TP", description=f"{ctx.author.mention}", color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=image, embed=embed)

    @commands.command(name="chris", aliases=["chri5", "Chris", "Chri5"], help="our friendly whale")
    @commands.check(checkchannel)
    async def chris(self, ctx):
        chris = ctx.guild.get_member(404296742872416258)
        pool = os.listdir('./pics/chris')
        image = random.choice(pool)
        path = './pics/chris/' + image
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Chris", description=f"{chris.mention}", color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(f"{chris.mention}", file=image, embed=embed)

    @commands.command(name="sexychris", aliases=["sexychri5", "SexyChris", "Sexychris", "SexyChri5", "Sexychri5"],
                      help="our sexy whale")
    @commands.check(checkchannel)
    async def sexychris(self, ctx):
        chris = ctx.guild.get_member(404296742872416258)
        path = './pics/chris/chris_sexy.jpg'
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Sexy Chris", description=f"{chris.mention} Hey sexy :smirk:",
                              color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(f"{chris.mention}", file=image, embed=embed)

    @commands.command(name="dez", help="rip doggo")
    @commands.check(checkchannel)
    async def dez(self, ctx):
        pool = os.listdir('./pics/dez')
        dez = ctx.guild.get_member(142121221893390336)
        image = random.choice(pool)
        path = './pics/dez/' + image
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Dez", description=f"{dez.mention}", color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(f"{dez.mention}", file=image, embed=embed)

    @commands.command(name="mork", aliases=["m0rk", "Mork", "M0rk"], help="that's him - probably on the toilet")
    @commands.check(checkchannel)
    async def mork(self, ctx):
        pool = os.listdir('./pics/mork')
        mork = ctx.guild.get_member(520167922367201280)
        image = random.choice(pool)
        path = './pics/mork/' + image
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Mork", description=f"{mork.mention}", color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=image, embed=embed)

    @commands.command(name="pumba", aliases=["pumbaa", "Pumba", "Pumbaa"], help="pumbaa /shrug")
    @commands.check(checkchannel)
    async def dez(self, ctx):
        pool = os.listdir('./pics/pumba')
        pumba = ctx.guild.get_member(517098993180868642)
        image = random.choice(pool)
        path = './pics/pumba/' + image
        image = discord.File(path, filename="image.png")
        embed = discord.Embed(title="Pumba", description=f"{pumba.mention}", color=discord.Colour.gold())
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=image, embed=embed)

    @commands.command(name="burn", help="In discord, Wormi burns you!")
    async def burn(self, ctx, target):
        if len(target) > 3:
            target = f"\\w*{target}*\\w*"
        else:
            target = f"\\w*{target}\\w*"
        regex = re.compile(target, re.I)
        if ctx.guild.id == 530157406349688862:  # WgD
            with open("./memberWgD.json", "r") as d:
                dic = json.load(d)
        elif ctx.guild.id == 717760982729883689:  # VpS
            with open("./memberVpS.json", "r") as d:
                dic = json.load(d)
        for key in dic:
            if regex.search(key) != None:
                await ctx.send(
                    f"{dic[key]} <a:panda_fire:715502370229846027><a:panda_fire:715502370229846027><a:panda_fire:715502370229846027>")
                break
            else:
                continue

    @commands.command(name="google", help="first google result")
    async def google(self, ctx, *, arg):
        cp = configparser.ConfigParser()
        cp.read('./config.ini')
        key = cp.get('DEFAULT', 'gapi')
        id = cp.get('DEFAULT', 'gid')

        def google_query(query, key, id, **kwargs):
            query_service = build("customsearch", "v1", developerKey=key)
            query_results = query_service.cse().list(q=query, cx=id, **kwargs).execute()
            return query_results['items']

        results_list = []
        results = google_query(arg, key, id, num=1)
        for result in results:
            results_list.append(result['link'])

        try:
            url = results_list[0]
        except IndexError:
            await ctx.send(f"{ctx.author.mention} No results found.")
        else:
            await ctx.send(f"{ctx.author.mention} Here is your google result:\n{url}")
    
    
    @commands.command(name="hangman", help="play hangman with wormi!")
    async def hangman(self, ctx):
        stage=[ #raw AND escaping to deal with discord formatting
r"""
    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    |\/
    |
    |
    |
    |
    |
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    |\/   |
    |
    |
    |
    |
    |
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    |\/   |
    |   (\_)
    |
    |
    |  
    |       
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    |\/   |
    |   (\_)
    |     |
    |     |
    |
    |
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    |\/   |
    |   (\_)
    |   \/|
    |     |
    |
    |
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    |\/   |
    |   (\_)
    |   \/|\
    |     |
    |
    |
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    |\/   |
    |   (\_)
    |   \/|\
    |     |
    |   \/
    |
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    |\/   |
    |   (\_)
    |   \/|\
    |     |
    |   \/ \
    |
    |\_\_\_"""]
        words = ["automobile", "cookies", "homeoffice", "wormageddon", "cheese", "dice", "bottle", "gaming", "riseofkingdoms", "bacon", "caterpillar", "servant", "geometry", "halloween", "telephone", "triangle", "farming", "hunting", "trade", "vegetable", "border", "grandmother", "policeman", "remarkable", "occasionally", "explanation", "fireplace", "discussion", "manufacturing", "mathematics", "biology", "shark", "tiger", "dolphin", "horse", "beer", "distance", "mysterious", "selection", "communism", "capitalism", "arrangement", "doctor", "raft", "waterfall", "jungle", "teabag"]
        if ctx.channel.id == 697082176432373831 or ctx.channel.id == 718825098462625853:
            word = random.choice(words)
            mask = "`"
            for _ in range(len(word)):
                mask += r"_ "
            mask += "`"
            turn, wrong = 0, ""
            name, text = "default", "default"
            embed = discord.Embed(colour=discord.Colour.gold(), title="Hangman")
            playing = True
            while playing:
                embed.clear_fields()
                name = (f"{stage[turn]}\n")
                text = (f"{mask}\nWrong letters: {wrong}\nPlease make your guess.\n")
                # text+=(f"Wrong letters: {wrong}\n")
                # text+=(f"Please make your guess.\n")
                embed.add_field(name=name, value=text, inline=False)
                await ctx.send(embed=embed)

                # custom check for wait_for
                def check(waited):
                    if ctx.channel.id == 697082176432373831:
                        id = 697082176432373831
                    elif ctx.channel.id == 718825098462625853:
                        id = 718825098462625853
                    return waited.author.bot == False and waited.channel.id == id

                try:
                    mes = await self.bot.wait_for("message", timeout=30, check=check)
                except asyncio.TimeoutError:
                    await ctx.send(f"Time is over! The word was '{word}'.")
                    playing = False
                    break
                char = mes.content.lower()
                if char == "ff":
                    await ctx.send("You forfeited.")
                    playing = False
                    break
                elif (len(char) > 1) or (char not in "abcdefghijklmnopqrstuvwxyz") or (char in wrong):
                    continue
                correct = False
                for p, l in enumerate(word):
                    if l == char:
                        mask = mask[0:2 * p + 1] + l + mask[2 * p + 2:]
                        correct = True
                if "_" not in mask:
                    await ctx.send(mask)
                    await ctx.send(f"Congratulations! You won! The correct word was {word}.")
                    playing = False
                    break
                elif correct == False and turn == 6:
                    await ctx.send(f"You lost! The correct word was {word}.")
                    playing = False
                    break
                else:
                    if correct:
                        await ctx.send("Correct!")
                    else:
                        await ctx.send("Incorrect!")
                        wrong += f"{char} "
                        turn += 1
        else:
            if ctx.guild.id == 530157406349688862:  # WgD
                await ctx.send(f"{ctx.author.mention} Please use {self.bot.get_channel(697082176432373831).mention}.")
            elif ctx.guild.id == 717760982729883689:  # VpS
                await ctx.send(f"{ctx.author.mention} Please use {self.bot.get_channel(718825098462625853).mention}.")
