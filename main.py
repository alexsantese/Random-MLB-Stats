from mlb_stats import make_tweet, stadium
import time
from twitter_credentials import *

authenticator = tweepy.OAuthHandler(twitter_api_key, twitter_api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)       

# the main function that pulls a tweet to post
def post_tweet():
    tweet, stadium = make_tweet()
    api.update_status_with_media(tweet, stadium)
         
# wait an hour in between posts
while True:
    post_tweet()
    time.sleep(3600)