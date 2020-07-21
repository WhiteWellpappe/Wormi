# Wormi
The official [WgD] and [VpS] Discord Bot under development by White Worm



This reposition is to gain experience with Git/GitHub functions and to protocol changes.



v2.0

With introducing a new AOO registration system some time ago and accessing the [VpS] server it's time to get to version 2.0 

CHANGES:
- experiemental loop for aoo to reduce API calls and increase stability, requires further testing
- commands adapted to work in 2 different servers, including .json management

NEW:
- new aoo registration using reactions
- several new requested commands
- very simple automated check for updates
- !restart - restarting Wormi for faster testing
- !google - showing first google search result for given keywords



v1.3

CHANGES:
- added permission changes to !aoo and new try/except check (thanks woody!)

NEW:
- !hangman - play a nice round of hangman with Wormi, alone or with friends



v1.2

CHANGES:
- custom !help command
- improved search algorithm for !burn using a json file and regular expressions
- fixed typos

NEW:
- !updatejson - updating member.json to match current users
- !tp to provide some toilet paper in these harsh times



v1.1

CHANGES:
- !burn - mentioning not longer needed
- absolute filepaths changed into relative path for more flexibility
- some if-statements changed into one-liners
- now using tuble unpacking

NEW:
- !checkinactive - checks for inactive, roleless members
- !kickinactive - kicks all inactive, roleless members
- !cleanaoo - purging 1000 messages in #aoo-registration
- !sendaoo - sending the current aoo.xlsx file
- !sysexit - shutting down Wormi for faster testing
