#!/usr/bin/env python3
import tweepy

#import twitter apps configaration file from config.py file
from config import *

#Authentication using keys & accesstoken
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.update_status(status="This is a sample tweet using Tweepy with python")
