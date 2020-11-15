import asyncio
import datetime
import os.path
import pickle
import datefinder
import discord
from discord.ext import commands
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def setup(bot):
    bot.add_cog(calendar(bot))


class calendar(commands.Cog, name='Calendar'):
    def __init__(self, bot):
        self.bot = bot
    
    async def calender_daily(self, timer):
        while True:
            now = datetime.datetime.utcnow()
            if now.time() < timer:
                date = now.date()
            else:
                date = now.date() + datetime.timedelta(days=1)
            then = datetime.datetime.combine(date, timer)
            await discord.utils.sleep_until(then)
            await asyncio.sleep(1)

            # for comments please look up the calendar24 command below
            ch = self.bot.get_channel(736628131359752214)
            scopes = ['https://www.googleapis.com/auth/calendar']
            creds = None
            if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'google_credentials.json', scopes)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)
            service = build('calendar', 'v3', credentials=creds)
            c_start = datetime.datetime.utcnow()
            c_end = c_start + datetime.timedelta(1)
            c_start = c_start.isoformat() + "Z"
            c_end = c_end.isoformat() + "Z"
            events_result = service.events().list(calendarId='primary', timeMin=c_start,
                                                  timeMax=c_end, singleEvents=True,
                                                  orderBy='startTime').execute()
            events = events_result.get('items', [])
            if not events:
                ch.send("No events today.")
            embed = discord.Embed(title="Events", description=f"Today's events", color=discord.Colour.gold())
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                embed.add_field(name="Event", value=f"{start}, {event['summary']}", inline=False)
            await ch.send(embed=embed)

    async def calender_weekly(self, timer):
        while True:
            now = datetime.datetime.utcnow()
            if now.time() < timer:
                date = now.date()
            else:
                date = now.date() + datetime.timedelta(days=7)
            then = datetime.datetime.combine(date, timer)
            await discord.utils.sleep_until(then)
            await asyncio.sleep(1)

            # for comments please look up the calendar24 command below
            ch = self.bot.get_channel(736628131359752214)
            scopes = ['https://www.googleapis.com/auth/calendar']
            creds = None
            if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'google_credentials.json', scopes)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)
            service = build('calendar', 'v3', credentials=creds)
            c_start = datetime.datetime.utcnow()
            c_end = c_start + datetime.timedelta(7)
            c_start = c_start.isoformat() + "Z"
            c_end = c_end.isoformat() + "Z"
            events_result = service.events().list(calendarId='primary', timeMin=c_start,
                                                  timeMax=c_end, singleEvents=True,
                                                  orderBy='startTime').execute()
            events = events_result.get('items', [])
            if not events:
                ch.send("No events this week.")
            embed = discord.Embed(title="Events", description=f"This Week's events", color=discord.Colour.gold())
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                embed.add_field(name="Event", value=f"{start}, {event['summary']}", inline=False)
            await ch.send(embed=embed)

    # errors in tasks raise silently normally so lets make them speak up
    def exception_catching_callback(self, task):
        if task.exception():
            task.print_stack()

    @commands.command(name="calendardaily", help="starts daily calendar coroutine")
    @commands.has_any_role("Discord King", "Officer", "Leader", "Wormanager")
    async def ca_daily_start(self, ctx):
        timer1 = datetime.time(hour=0)  # UTC
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_running_loop()
        loop.create_task(self.calender_daily(timer1))

    @commands.command(name="calendarweekly", help="starts weekly calendar coroutine")
    @commands.has_any_role("Discord King", "Officer", "Leader", "Wormanager")
    async def ca_weekly_start(self, ctx):
        timer1 = datetime.time(hour=0)  # UTC
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop = asyncio.get_running_loop()
        loop.create_task(self.calender_weekly(timer1))

    @commands.command(name="calendarevent", help="adds test appointment to calendar")
    @commands.has_any_role("Discord King", "Officer", "Leader", "Wormanager")
    async def ca_event(self, ctx, start_time_str, *, summary, description=None):
        # If modifying these scopes, delete the file token.pickle.
        scopes = [r'https://www.googleapis.com/auth/calendar']

        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'google_credentials.json', scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        matches = list(datefinder.find_dates(start_time_str))
        if len(matches):
            start_time = matches[0]
            end_time = start_time

        event = {
            'summary': str(summary),
            'location': None,
            'description': description,
            'start': {
                'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': "UTC",
            },
            'end': {
                'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': "UTC",
            },
            'attendees': [
                {'email': "wormiwormageddon@gmail.com"},
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        event = service.events().insert(calendarId='primary', body=event, sendNotifications=True).execute()
        await ctx.send(f"{ctx.author.mention} 'Event created: {event.get('htmlLink')}")

    @commands.command(name="calendar24", help="shows events in the next 24h")
    @commands.has_any_role("Discord King", "Officer", "Leader", "Wormanager")
    async def ca_test(self, ctx):
        ch = self.bot.get_channel(736628131359752214)
        scopes = ['https://www.googleapis.com/auth/calendar']
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'google_credentials.json', scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        # Building Time in ISO format first
        c_start = datetime.datetime.utcnow()
        c_end = c_start + datetime.timedelta(1)
        c_start = c_start.isoformat() + "Z"
        c_end = c_end.isoformat() + "Z"
        events_result = service.events().list(calendarId='primary', timeMin=c_start,
                                              timeMax=c_end, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            ch.send("No events today.")
        embed = discord.Embed(title="Events", description=f"Today's events", color=discord.Colour.gold())
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            embed.add_field(name="Event", value=f"{start}, {event['summary']}", inline=False)
        await ch.send(embed=embed)
