# Twitter Web Services
from config_file_stamates import *
import requests
import tweepy
from pprint import pprint
import re
consumer_key = TWITTER_CONSUMER_KEY
consumer_secret = TWITTER_CONSUMER_SECRET
access_token = TWITTER_ACCESS_TOKEN
access_secret = TWITTER_ACCESS_SECRET

hp_url = "https://api.havenondemand.com/1/api/sync/ocrdocument/v1?apikey=" + HPE_HAVEN_API_KEY + "&url="

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
tweets = api.search(q='#periscope')
# display results to screen
for t in tweets:
    # url = t._json['entities']['urls'][0]['expanded_url'] # extended periscope url
    tokenID = re.sub(r'.+[/w/]/', '', t._json['entities']['urls'][0]['expanded_url']) # get tokenID
    api_source = 'https://api.periscope.tv/api/v2/getAccessPublic?token=' + tokenID
    item = requests.get(api_source).json()
    import pdb; pdb.set_trace()
    url = item['hls_url']
    response = requests.get(hp_url)
    print t.created_at, re.sub(r'[^\x00-\x7F]+',' ', t.text), "\n"
