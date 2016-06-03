# Twitter Web Services
from config_file_stamates import *
import tweepy
from pprint import pprint
import re
consumer_key = TWITTER_CONSUMER_KEY
consumer_secret = TWITTER_CONSUMER_SECRET
access_token = TWITTER_ACCESS_TOKEN
access_secret = TWITTER_ACCESS_SECRET

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
tweets = api.search(q='#python')
# import pdb; pdb.set_trace()
# display results to screen
for t in tweets:
    print t.created_at, re.sub(r'[^\x00-\x7F]+',' ', t.text), "\n"
