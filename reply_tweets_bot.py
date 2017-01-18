import tweepy

#import twitter apps configaration file from config.py file
from config import *

#Authentication using keys & accesstoken
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

twt = api.search(q="Hello World")

#list of strings that we want to check from tweets
txt = ['Hello world!',
    'Hello World!',
    'Hello World!!!',
    'Hello world!!!',
    'Hello, world!',
    'Hello, World!']

#Its can take many time
for st in twt:
	for s in txt:
		if s == st.text:
			usr = st.user.screen_name
			msg = ("@%s Hello!" %(usr))
			st = api.update_status(msg, st.id)
