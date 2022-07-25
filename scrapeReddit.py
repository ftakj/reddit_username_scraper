import praw
import random
import requests
import datetime
import json

userAgent = "FTA"
clientId = ''
clientSecret = ""

reddit = praw.Reddit(user_agent=userAgent,
                     client_id=clientId, client_secret=clientSecret)
submission = reddit.submission(id='pek3xy')
submission.comments.replace_more(limit=None)

users = []

previousWinners = []

for top_level_comment in submission.comments:
    if top_level_comment.author is None:
        continue
    original_username = "/u/" + top_level_comment.author.name
    username = original_username.lower()

    if username not in users and username not in previousWinners and username != '/u/ftakj':
        users.append(username)

winners = []

limit = 100
while len(winners) < limit:
    chosen = random.choice(users)
    if chosen not in winners:
        winners.append(chosen)
    if len(winners) == len(users):
        limit = 0

winners.sort()

for username in winners:
    print(username)

print(len(winners), ' winners selected')

dt = datetime.datetime.today()
year = dt.year
month = dt.month
day = dt.day

filestring = 'Winners: ' + str(month) + '-' + \
    str(day) + '-' + str(year) + '.json'
with open(filestring, 'w') as outfile:
    json.dump(winners, outfile)

for jsonData in previousWinners:
    with open(jsonData, 'r') as f:
        winnerNames = json.load(f)
        for prevWinner in winnerNames:
            winners.append(prevWinner)

print(len(winners), 'WITH PREVIOUS ATTACHED')
dataToSend = {"id": "ftakj", "winners": winners}

isDev = False
if (isDev):
    requests.post('http://localhost:3000/api/reddit/nfl/reddit-winners',
                  json=dataToSend)
else:
    requests.post('https://fantasyteamadvice.com/api/reddit/nfl/reddit-winners',
                  json=dataToSend)
