import praw
import random


userAgent = "FTA"
clientId = ''
clientSecret = ""


reddit = praw.Reddit(user_agent=userAgent, client_id=clientId, client_secret=clientSecret)
submission = reddit.submission(id='io74ie')
submission.comments.replace_more(limit=None)

users = []

for top_level_comment in submission.comments:
  if top_level_comment.author is None: continue
  original_username = "/u/" + top_level_comment.author.name
  username = original_username.lower()

  if username not in users and username != '/u/ftakj':
      users.append(username)

winners = []

while len(winners) < 50:
  chosen = random.choice(users)
  if chosen not in winners:
    winners.append(chosen)

winners.sort()

for username in winners:
  print(username)

print (len(winners), ' winners selected')
