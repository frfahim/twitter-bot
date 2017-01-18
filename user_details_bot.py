import tweepy

#import twitter apps configaration file from config.py file
from config import *

#Authentication using keys & accesstoken
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Donal Trump Twitter account
user = api.get_user('realDonaldTrump')

print("Name:", user.name)
print("User id: ", user.id_str)
print("Description: ", user.description)
print("Location:",user.location)
print("Time zone: ", user.time_zone)
print("Number of Following:",user.friends_count)
print("Number of Followers:",user.followers_count)
print("Number of tweets: ", str(user.statuses_count))

