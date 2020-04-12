import random, discord, os, re, json, asyncio
from discord.ext import commands

random.seed()

def setup(bot):
    bot.add_cog(Fun(bot))


class Fun(commands.Cog, name='Fun'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        m=str(message.content)
        if message.author.bot:
            return
        
        elif message.author.id=='547508375592632330':
            if random.randint(1,6)==5:
                await message.channel.send(f"{message.author.mention} Hey, I heard you wish to kill me? BRING IT ON BITCH!")
        
        elif message.channel.id==558632300737462272:
            if ("Wormi" in m) or ("wormi" in m):
                if "show" in m:
                    if ("lama" in m) or ("alpaca" in m):
                        pool=os.listdir('./pics/lama')
                        image=random.choice(pool)
                        path='./pics/lama/'+image
                        await message.channel.send(f"{message.author.mention}")                       
                        await message.channel.send(file=discord.File(path))
                    elif "pizza" in m:
                        pool=os.listdir('./pics/pizza')
                        image=random.choice(pool)
                        path='./pics/pizza/'+image
                        await message.channel.send(f"{message.author.mention}")
                        await message.channel.send(file=discord.File(path))
                    elif "senor" in m:
                        path='./pics/hardjan/senor_hardjan.png'
                        await message.channel.send(f"{message.author.mention}")
                        await message.channel.send(file=discord.File(path))
                    elif ("pet" in m) or ("moral" in m):
                        pool=os.listdir('./pics/pet')
                        image=random.choice(pool)
                        path='./pics/pet/'+image
                        await message.channel.send(f"{message.author.mention}")
                        await message.channel.send(file=discord.File(path))

    
    @commands.command(name='8ball', help='Magic 8 Ball, Wormi answers any question')
    async def magic8ball(self, ctx):
            answer=['It is as certain as WW is awesome.','It is decidedly so.','Without a doubt.','Yes - definitely.','You may rely on it.','As I see it, yes.','Most likely.',
            'Outlook good.','Yes.','Signs point to yes.','Reply hazy, try again.','Ask again later.','Better not tell you now.','Cannot predict now, better ask Meg.','Concentrate and ask again.',
            "Don't count on it.",'My reply is no.','LOL, you wish.','Outlook not so good.','Nah.']
            response=random.choice(answer)
            await ctx.send(f"{ctx.author.mention} {response}")        


    #RPS Paper
    @commands.command(name="paper", help="Paper for RPS")
    async def paper(self, ctx):
        x=random.randint(1,3)
        await ctx.send(f"{ctx.author.mention} Scissor! I won! :)") if x==1 else None
        await ctx.send(f"{ctx.author.mention} Rock! I lost! :(") if x==2 else None
        await ctx.send(f"{ctx.author.mention} Paper! A tie!") if x==3 else None

    #RPS Rock
    @commands.command(name="rock", help="Rock for RPS")
    async def rock(self, ctx):
        x=random.randint(1,3)
        await ctx.send(f"{ctx.author.mention} Paper! I won! :)") if x==1 else None
        await ctx.send(f"{ctx.author.mention} Scissor! I lost! :(") if x==2 else None
        await ctx.send(f"{ctx.author.mention} Rock! A tie!") if x==3 else None

    #RPS Scissor
    @commands.command(name="scissor", help="Scissor for RPS")
    async def scissor(self, ctx):
        x=random.randint(1,3)
        await ctx.send(f"{ctx.author.mention} Rock! I won! :)") if x==1 else None
        await ctx.send(f"{ctx.author.mention} Paper! I lost! :(") if x==2 else None
        await ctx.send(f"{ctx.author.mention} Scissor! A tie!") if x==3 else None


    #J4F
    @commands.command(name="smash", help="smash?")
    async def smash(self, ctx):
        x=random.randint(1, 50)
        await ctx.send(f"{ctx.author.mention} I have a wormfriend.") if x==10 else await ctx.send(f"{ctx.author.mention} No.")


    #Custom Dice rolls
    @commands.command(name="roll", help="rolls XdY dice")
    async def roll(self, ctx, arg):
        rlist, erg = ('', 0)
        try:
            arg=str(arg)
        except:
            await ctx.send("Converting Error Dice Count - Please use a valid number.")
        x=arg.find("d")
        arg1, arg2 = (arg[:x], arg[x+1:])
        try:
            arg1=int(arg1)
            arg2=int(arg2)
        except:
            await ctx.send("Converting Error Dice Size - Please use a valid number.")
        if arg1>100:
            await ctx.send(f"{ctx.author.mention} Please don't roll so much dice, I don't have big enough hands! Wait .... what?")
        elif arg2>300:
            await ctx.send(f"{ctx.author.mention} Please don't roll such big dice, I can't read the numbers anymore!")
        else:
            for _ in range(0,arg1):
                rlist=rlist+"+" if rlist!="" else None
                r=random.randint(1,arg2)
                rlist=rlist+str(r)
                erg=erg+r
            await ctx.send(f"{ctx.author.mention} {rlist} = {erg}")

    #Trolling Woody
    @commands.command(name="piney", help="just to troll woody")
    async def piney(self, ctx):
        if ctx.channel.id!=558632300737462272:
            await ctx.send(f"{ctx.author.mention} Please use the {self.bot.get_channel(558632300737462272).mention}. ;)")   
        else:
            woody=ctx.guild.get_member(548926176316358657)
            path="./pics/woody.jpg"
            await ctx.send(f"{woody.mention}")
            await ctx.send(file=discord.File(path))

    #Trolling Deedee
    @commands.command(name="deedee", help="revenge for woody")
    async def deedee(self, ctx):
        if ctx.channel.id!=558632300737462272:
            await ctx.send(f"{ctx.author.mention} Please use the {self.bot.get_channel(558632300737462272).mention}. ;)")   
        else:
            deedee=ctx.guild.get_member(548924284836380698)
            pool=os.listdir('./pics/deedee')
            image=random.choice(pool)
            path='./pics/deedee/'+image
            await ctx.send(f"{deedee.mention}")
            await ctx.send(file=discord.File(path))

    #Trolling Ada
    @commands.command(name="ada", help="revenge for woody")
    async def ada(self, ctx):
        if ctx.channel.id!=558632300737462272:
            await ctx.send(f"{ctx.author.mention} Please use the {self.bot.get_channel(558632300737462272).mention}. ;)")   
        else:
            ada=ctx.guild.get_member(541287316769996800)
            pool=os.listdir('./pics/ada')
            image=random.choice(pool)
            path='./pics/ada/'+image
            await ctx.send(f"{ada.mention}")
            await ctx.send(file=discord.File(path))

    #Trolling Nana/Lucky
    @commands.command(name="nana", help="no idea")
    async def nana(self, ctx):
        if ctx.channel.id!=558632300737462272:
            await ctx.send(f"{ctx.author.mention} Please use the {self.bot.get_channel(558632300737462272).mention}. ;)")   
        else:
            lucky=ctx.guild.get_member(602110022394052618)
            path="./pics/nana.jpg"
            await ctx.send(file=discord.File(path))
            await ctx.send(f"{lucky.mention} Behave!")
    
    @commands.command(name="lama", help="random lama")
    async def lama(self, ctx):
        if ctx.channel.id!=558632300737462272:
            await ctx.send(f"{ctx.author.mention} Please use the {self.bot.get_channel(558632300737462272).mention}. ;)")   
        else:
            pool=os.listdir('./pics/lama')
            image=random.choice(pool)
            path='./pics/lama/'+image
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(file=discord.File(path))

    @commands.command(name="pet", help="random WgD moral support")
    async def pet(self, ctx):
        if ctx.channel.id!=558632300737462272:
            await ctx.send(f"{ctx.author.mention} Please use the {self.bot.get_channel(558632300737462272).mention}. ;)")   
        else:
            pool=os.listdir('./pics/pet')
            image=random.choice(pool)
            path='./pics/pet/'+image
            await ctx.send(f"Moral support arrived {ctx.author.mention}! I am showing {image}")
            await ctx.send(file=discord.File(path))

    @commands.command(name="hardjan", help="deedee's rok bf")
    async def hardjan(self, ctx):
        if ctx.channel.id!=558632300737462272:
            await ctx.send(f"{ctx.author.mention} Please use the {self.bot.get_channel(558632300737462272).mention}. ;)")   
        else:
            hardjan=ctx.guild.get_member(341379990228697090)
            pool=os.listdir('./pics/hardjan')
            image=random.choice(pool)
            path='./pics/hardjan/'+image
            await ctx.send(f"{hardjan.mention} aka 'DeeDee's RoK boyfriend'")
            await ctx.send(file=discord.File(path))

    @commands.command(name="pizza", help="random pizza")
    async def pizza(self, ctx):
        if ctx.channel.id!=558632300737462272:
            await ctx.send(f"{ctx.author.mention} Please use the {self.bot.get_channel(558632300737462272).mention}. ;)")   
        else:
            pool=os.listdir('./pics/pizza')
            image=random.choice(pool)
            path='./pics/pizza/'+image
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(file=discord.File(path))

    @commands.command(name="tp", help="some toilet paper")
    async def tp(self, ctx):
        if ctx.channel.id!=558632300737462272:
            await ctx.send(f"{ctx.author.mention} Please use the {self.bot.get_channel(558632300737462272).mention}. ;)")   
        else:
            pool=os.listdir('./pics/tp')
            image=random.choice(pool)
            path='./pics/tp/'+image
            await ctx.send(f"{ctx.author.mention}")
            await ctx.send(file=discord.File(path))
    
    @commands.command(name="burn", help="In WgD discord, Wormi burns you!")
    async def burn(self, ctx, target):
        if len(target)>3:
            target=f"\\w*{target}*\\w*"
        else:
            target=f"\\w*{target}\\w*"
        regex=re.compile(target, re.I)
        with open ("./member.json", "r") as d:
            dic=json.load(d)
        for key in dic:
            if regex.search(key)!=None:
                await ctx.send(f"{dic[key]} :fire::fire::fire:")
                break
            else:
                continue
    
    
    @commands.command(name="hangman", help="play hangman with wormi!")
    async def hangman(self, ctx):
        stage=[ #raw AND escaping to deal with discord formatting
r"""
    \_\_\_\_\_\_\_\_\_
    |\/
    |
    |
    |
    |
    |
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_\_
    |\/   |
    |
    |
    |
    |
    |
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_\_
    |\/   |
    |   (\_)
    |
    |
    |  
    |       
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_
    |\/   |
    |   (\_)
    |     |
    |     |
    |
    |
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_
    |\/   |
    |   (\_)
    |   \/|
    |     |
    |
    |
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_
    |\/   |
    |   (\_)
    |   \/|\
    |     |
    |
    |
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_
    |\/   |
    |   (\_)
    |   \/|\
    |     |
    |   \/
    |
    |\_\_\_""",
r"""
    \_\_\_\_\_\_\_\_
    |\/   |
    |   (\_)
    |   \/|\
    |     |
    |   \/ \
    |
    |\_\_\_"""]
        words=["automobile", "cookies", "homeoffice", "wormageddon", "cheese", "dice", "bottle", "gaming", "riseofkingdoms", "bacon", "caterpillar", "servant", "geometry", "halloween", "telephone", "triangle", "farming", "hunting", "trade", "vegetable", "border", "grandmother", "policeman", "remarkable", "occasionally", "explanation", "fireplace", "discussion", "manufacturing", "mathematics", "biology", "shark", "tiger", "dolphin", "horse", "beer", "distance", "mysterious", "selection", "communism", "capitalism", "arrangement", "doctor", "raft", "waterfall", "jungle", "teabag"]
        if ctx.channel.id!=697082176432373831:
            await ctx.send(f"{ctx.author.mention} Please use {self.bot.get_channel(697082176432373831).mention}.")
        else:
            word=random.choice(words)
            mask="`"
            for _ in range(len(word)):
                mask+=r"_ "
            mask+="`"
            turn, wrong=0, ""
            name, text="default", "default"
            embed=discord.Embed(colour=discord.Colour.gold(), title= "Hangman")
            playing=True
            while playing:
                embed.clear_fields()
                name=(f"{stage[turn]}\n")
                text=(f"{mask}\nWrong letters: {wrong}\nPlease make your guess.\n")
                #text+=(f"Wrong letters: {wrong}\n")
                #text+=(f"Please make your guess.\n")
                embed.add_field(name=name, value=text, inline=False)
                await ctx.send(embed=embed)

                #custom check for wait_for
                def check(waited):
                    return waited.author.bot==False and waited.channel.id==697082176432373831
                
                try:
                    mes=await self.bot.wait_for("message", timeout=30, check=check)
                except asyncio.TimeoutError:
                    await ctx.send(f"Time is over! The word was '{word}'.")
                    playing=False
                    break
                char=mes.content.lower()
                if char=="ff":
                    await ctx.send("You forfeited.")
                    playing=False
                    break
                elif (len(char)>1) or (char not in "abcdefghijklmnopqrstuvwxyz") or (char in wrong):
                    continue
                correct=False
                for p, l in enumerate(word):
                    if l==char:
                        mask=mask[0:2*p+1]+l+mask[2*p+2:]
                        correct=True
                if "_" not in mask:
                    await ctx.send(mask)
                    await ctx.send(f"Congratulations! You won! The correct word was {word}.")
                    playing=False
                    break
                elif correct==False and turn==6:
                    await ctx.send(f"You lost! The correct word was {word}.")
                    playing=False
                    break
                else:
                    if correct:
                        await ctx.send("Correct!")
                    else:
                        await ctx.send("Incorrect!")
                        wrong+=f"{char} "
                        turn+=1