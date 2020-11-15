import datetime, discord, asyncio
from discord.ext import commands


def setup(bot):
    bot.add_cog(newAOO(bot))


class newAOO(commands.Cog, name='newAOO'):
    def __init__(self, bot):
        self.bot = bot

    # class variables for aoo
    # Preparing "empty" strings for embed, set count of votes/participants to 0, create header embed, deactivate loop
    ann: discord.Message
    listsat, listsun = "Placeholder\n", "Placeholder\n"
    votesat, votesun, partsat, partsun = 0, 0, 0, 0
    embed_ann = discord.Embed(
        colour=discord.Colour.gold(),
        title="Ark Of Osiris Announcement"
    )
    loop_active = False
    error_count = 0
    farm = 0

    # Cleaning the Aoo-registration-channel
    @commands.command(name="cleanaoo", help="cleans 200 #aoo-registration messages")
    @commands.has_any_role('Discord King', 'Leader', 'Officer', "Wormanager")
    async def cleanaoo(self, ctx):
        if ctx.guild.id != 530157406349688862:
            await ctx.send("This command is only usable in WgD for now :(")
        else:
            clean = self.bot.get_channel(651033088943587328)
            await clean.purge(limit=200)
            await ctx.send(f"{ctx.author.mention} {clean.mention} cleaned.")

    @commands.command(name="aoo", help="new aoo registration system")
    @commands.has_any_role('Discord King', 'Leader', "Officer", "Wormanager")
    async def aooreaction(self, ctx, date, time_sat=20, time_sun=20):
        if ctx.guild.id != 530157406349688862:
            await ctx.send("This command is only usable in WgD for now :(")
        else:
            if date is None:
                ctx.send(f"{ctx.author.mention} Don't forget the date! ;)")
            else:
                try:
                    _ = int(date)
                except:
                    await ctx.send(
                        f"{ctx.author.mention} Please check the command again. An error occoured and I caught it so you don't wreck the channel like Woody did once.")
                date2 = str(int(date) + 1)
                # sorting months into 2 groups
                m30 = ["04", "06", "09", "11"]
                m31 = ["01", "03", "05", "07", "08", "10", "12"]
                # checking changing month mid-event
                if int(date) > 31 or int(date) <= 0:
                    await ctx.send(f"{ctx.author.mention} Please insert a valid day.")
                else:
                    if date == "28":
                        if datetime.datetime.now().strftime("%m") == "02":
                            date2 = "1" if int(datetime.datetime.now().strftime("%Y")) % 4 != 0 else date2
                    elif date == "29":
                        if datetime.datetime.now().strftime("%m") == "02":
                            date2 = "1" if int(datetime.datetime.now().strftime("%Y")) % 4 == 0 else date2
                    elif date == "30":
                        for x in m30:
                            date2 = "1" if x == datetime.datetime.now().strftime("%m") else date2
                    elif date == "31":
                        for x in m31:
                            date2 = '1' if x == datetime.datetime.now().strftime("%m") else date2
                    # correcting the ending
                    if int(date) == 1:
                        date = date + "st"
                    elif int(date) == 2:
                        date = date + "nd"
                    elif int(date) == 3:
                        date = date + "rd"
                    else:
                        date = date + "th"
                    if int(date2) == 1:
                        date2 = date2 + "st"
                    elif int(date2) == 2:
                        date2 = date2 + "nd"
                    elif int(date2) == 3:
                        date2 = date2 + "rd"
                    else:
                        date2 = date2 + "th"

                    self.embed_ann = discord.Embed(
                        colour=discord.Colour.gold(),
                        title=f"Ark Of Osiris {date}/{date2} Announcement"
                    )
                    self.loop_active = True
                    self.embed_ann.add_field(name="Announcement",
                                             value=f":loudspeaker: **It's AOO Voting time!**\n\n**Please use the shown reaction to register!**\n\n**FOR WgDF**\n1️⃣ - Only Sat, {date}, {time_sat}:00 UTC\n2️⃣ - Only Sun, {date2}, {time_sun}:00 UTC\n3️⃣ - Can do both, vote for/prefer saturday\n4️⃣ - Can do both, vote for/prefer sunday\n\nWormi will update this message every 3s. **Please confirm your name appears!**\nOnly your latest reaction will taken into account. New votes will be voided if 25 participants are reached for the selected day.\n\n:taco: **25 slots, 5 reserved**, First Come First Serve system\n\n:hamburger: Start voting now, end on Thursday or when full.\n:pie: You can void all registrations and your vote by deselecting your reaction.\n\n:carrot: If you encounter an error, please hit up any R4 right away.",
                                             inline=False)
                    self.embed_ann.add_field(name="Votes",
                                             value=f"Votes for Saturday: {self.votesat}\n Votes for Sunday: {self.votesun}",
                                             inline=False)
                    self.embed_ann.add_field(name=f"Participants for Saturday: {self.partsat}", value=self.listsat,
                                             inline=False)
                    self.embed_ann.add_field(name=f"Participants for Sunday: {self.partsun}", value=self.listsun,
                                             inline=False)
                    self.ann = await ctx.send("@everyone", embed=self.embed_ann)
                    for x in ("1️⃣", "2️⃣", "3️⃣", "4️⃣"):
                        await self.ann.add_reaction(x)
                    await asyncio.sleep(1)
                    self.ann = await ctx.fetch_message(self.ann.id)
                    await ctx.send(f"Message ID: {self.ann.id}")
                    await self.ann.pin()
                    ann_id = self.ann.id

                    if ctx.channel.id == 651033088943587328:
                        # enabling writing/reading/history for members for feedback
                        role = ctx.guild.get_role(530162542148976661)
                        await ctx.channel.set_permissions(role, read_messages=True, send_messages=True,
                                                          view_channel=True, read_message_history=True)

                    while self.loop_active:
                        await asyncio.sleep(4.5)
                        try:
                            listreact = self.ann.reactions
                            # counting reactions
                            self.votesat_new = listreact[0].count + listreact[2].count - 2
                            self.votesun_new = listreact[1].count + listreact[3].count - 2
                            # if change in recent reactions //DOESNT COVER CHANGED PLAYERS IF VOTE REMAINS CONSTANT
                            # if (self.votesat_new!=self.votesat) or (self.votesun_new!=self.votesun):
                            # updating votes
                            self.votesat = self.votesat_new
                            self.votesun = self.votesun_new
                            # getting users, flatten list
                            flatsat = await listreact[0].users().flatten() + await listreact[2].users().flatten() + await listreact[3].users().flatten()
                            flatsun = await listreact[1].users().flatten() + await listreact[2].users().flatten() + await listreact[3].users().flatten()
                            # adding players to displayed lists
                            self.listsat, self.listsun = "", ""
                            for user in flatsat:
                                if user.bot:
                                    continue
                                elif user.display_name not in self.listsat:
                                    self.listsat += f"{user.display_name}\n"
                            for user in flatsun:
                                if user.bot:
                                    continue
                                elif user.display_name not in self.listsun:
                                    self.listsun += f"{user.display_name}\n"
                            # no list remains empty
                            if self.listsat == "":
                                self.listsat = "Placeholder\n"
                            if self.listsun == "":
                                self.listsun = "Placeholder\n"
                            # counting players for both days
                            self.partsat = listreact[0].count + listreact[2].count + listreact[3].count - 3
                            self.partsun = listreact[1].count + listreact[2].count + listreact[3].count - 3
                            # delete vote/participants saturday/participants sunday fields in embed
                            ea = self.embed_ann
                            for _ in range(3):
                                ea.remove_field(1)
                            # adding fields with updated values
                            ea.add_field(name="Votes",
                                         value=f"Votes for Saturday: {self.votesat}\n Votes for Sunday: {self.votesun}",
                                         inline=False)
                            ea.add_field(name=f"Participants for Saturday: {self.partsat}", value=self.listsat,
                                         inline=False)
                            ea.add_field(name=f"Participants for Sunday: {self.partsun}", value=self.listsun,
                                         inline=False)
                            # editing message
                            await self.ann.edit(content="@everyone", embed=ea)
                            # little delay to ensure message is there to be fetched
                            await asyncio.sleep(0.5)
                            self.ann = await ctx.fetch_message(ann_id)
                            # reseting error counter after succesfull update
                            self.error_count = 0
                        except:
                            try:
                                await ctx.send("Error in aoo loop. Retrying in 20s")
                                self.error_count += 1
                                if self.error_count > 6:
                                    await ctx.send(
                                        f"To many errors. I am stopping the loop, please consider restarting it.\n<@228476917861449738>, check this out!")
                                    self.loop_active = False
                                else:
                                    await asyncio.sleep(15.5)
                            except:
                                await asyncio.sleep(5.5)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, pl):
        if pl.guild_id == 530157406349688862:  # WgD
            try:
                ann = await self.ann.channel.fetch_message(self.ann.id)
            except:
                pass
            try:
                if pl.member.bot:
                    pass
                elif pl.message_id == self.ann.id:
                    listreact = ann.reactions
                    self.votesat = listreact[0].count + listreact[2].count - 2
                    self.votesun = listreact[1].count + listreact[3].count - 2
                    self.partsat = listreact[0].count + listreact[2].count + listreact[3].count - 3
                    self.partsun = listreact[1].count + listreact[2].count + listreact[3].count - 3
                    if self.partsat == 26 or self.partsun == 26:
                        for reaction in ann.reactions:
                            if reaction.emoji == str(pl.emoji):
                                await reaction.remove(pl.member)
                    else:
                        if pl.emoji.name == "1️⃣":
                            for i in (1, 2, 3):
                                await ann.reactions[i].remove(pl.member)
                        elif pl.emoji.name == "2️⃣":
                            for i in (0, 2, 3):
                                await ann.reactions[i].remove(pl.member)
                        elif pl.emoji.name == "3️⃣":
                            for i in (0, 1, 3):
                                await ann.reactions[i].remove(pl.member)
                        elif pl.emoji.name == "4️⃣":
                            for i in (0, 1, 2):
                                await ann.reactions[i].remove(pl.member)
                        else:
                            for reaction in ann.reactions:
                                if reaction.emoji == str(pl.emoji):
                                    await reaction.clear()
                else:
                    pass
            except AttributeError:
                pass

    @commands.command(name="endaoo", help="end new aoo registration system")
    @commands.has_any_role('Discord King', 'Leader', 'Officer', "Wormanager")
    async def endaooreaction(self, ctx):
        if ctx.guild.id == 530157406349688862:
            self.loop_active = False
            await ctx.send(f"@everyone \nThe registration finished! Thanks for your participation!")
            if ctx.channel.id == 651033088943587328:
                # disabling writing for members
                role = ctx.guild.get_role(530162542148976661)
                await ctx.channel.set_permissions(role, read_messages=True, send_messages=False, view_channel=True,
                                                  read_message_history=True)
            # let last update circle run out
            await asyncio.sleep(5)
            await self.ann.clear_reactions()
            # resetting class variables
            self.listsat, self.listsun = "Placeholder\n", "Placeholder\n"
            self.votesat, self.votesun, self.partsat, self.partsun = 0, 0, 0, 0
            self.embed_ann = discord.Embed(
                colour=discord.Colour.gold(),
                title="Ark Of Osiris Announcement"
            )
        else:
            await ctx.send("This command is only usable in WgD for now :(")

    @commands.command(name="restartaoo", help="restarts aoo loop to display votes")
    @commands.has_any_role('Discord King', 'Leader', 'Officer', "Wormanager")
    async def resetaoo(self, ctx, mess_id):
        if ctx.guild.id == 530157406349688862:
            try:
                if int(mess_id) == self.ann.id:
                    await ctx.send(f"{ctx.author.mention} AOO restart initiated. Disabling original loop.")
                else:
                    await ctx.send(f"{ctx.author.mention} AOO registartion rebooting on given message")
                    self.ann = await ctx.fetch_message(mess_id)
            except:
                await ctx.send(
                    f"{ctx.author.mention} No original announcement found. AOO registration rebooting on given message")
                self.ann = await ctx.fetch_message(mess_id)
            self.loop_active = False
            await asyncio.sleep(5)
            await ctx.send(f"{ctx.author.mention} Starting loop in this command.")
            self.loop_active = True
            while self.loop_active:
                await asyncio.sleep(1.5)
                try:
                    listreact = self.ann.reactions
                    self.votesat_new = listreact[0].count + listreact[2].count - 2
                    self.votesun_new = listreact[1].count + listreact[3].count - 2
                    if (self.votesat_new != self.votesat) or (self.votesun_new != self.votesun):
                        self.votesat = self.votesat_new
                        self.votesun = self.votesun_new
                        flatsat = await listreact[0].users().flatten() + await listreact[2].users().flatten() + await \
                        listreact[3].users().flatten()
                        flatsun = await listreact[1].users().flatten() + await listreact[2].users().flatten() + await \
                        listreact[3].users().flatten()
                        self.listsat, self.listsun = "", ""
                        for user in flatsat:
                            if user.bot:
                                continue
                            elif user.display_name not in self.listsat:
                                self.listsat += f"{user.display_name}\n"
                        for user in flatsun:
                            if user.bot:
                                continue
                            elif user.display_name not in self.listsun:
                                self.listsun += f"{user.display_name}\n"
                        if self.listsat == "":
                            self.listsat = "Placeholder\n"
                        if self.listsun == "":
                            self.listsun = "Placeholder\n"
                        self.votesat_new = listreact[0].count + listreact[2].count - 2
                        self.votesun_new = listreact[1].count + listreact[3].count - 2
                        self.partsat = listreact[0].count + listreact[2].count + listreact[3].count - 3
                        self.partsun = listreact[1].count + listreact[2].count + listreact[3].count - 3
                        ea = self.embed_ann
                        for _ in range(3):
                            ea.remove_field(1)
                        ea.add_field(name="Votes",
                                     value=f"Votes for Saturday: {self.votesat}\n Votes for Sunday: {self.votesun}",
                                     inline=False)
                        ea.add_field(name=f"Participants for Saturday: {self.partsat}", value=self.listsat,
                                     inline=False)
                        ea.add_field(name=f"Participants for Sunday: {self.partsun}", value=self.listsun, inline=False)
                        await asyncio.sleep(1)
                        await self.ann.edit(content="@everyone", embed=ea)
                        await asyncio.sleep(0.5)
                        self.ann = await ctx.fetch_message(ann_id)
                        self.error_count = 0
                except:
                    try:
                        await ctx.send("Error in aoo loop. Retrying in 20s")
                        self.error_count += 1
                        if self.error_count > 6:
                            await ctx.send(
                                f"To many errors. I am stopping the loop, please consider restarting it.\n<@228476917861449738>, check this out!")
                            self.loop_active = False
                        else:
                            await asyncio.sleep(18.5)
                    except:
                        await asyncio.sleep(3.5)
        else:
            await ctx.send("This command is only usable in WgD for now :(")
