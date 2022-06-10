import gspread
from mlb_stats import get_rand_player, get_rand_stat, rand_img
import tweepy
import time
from twitter_credentials import twitter_api_key, twitter_api_key_secret, access_token, access_token_secret

authenticator = tweepy.OAuthHandler(twitter_api_key, twitter_api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

# api.update_status("I'm testing this bot.")

sa = gspread.service_account()
sh = sa.open('Random MLB Stats Sheet')

wks = sh.worksheet('Sheet1')

def get_stats():
    for i in range(1, 21):
        data = get_rand_stat(get_rand_player())
        if data != None:
            wks.update('A'+str(i), data)
        

def post_tweet():
    
    next_tweet = wks.acell('A1').value
    
    tweeting = True
    
    while tweeting:
        if next_tweet == None:
            wks.delete_row(1)
        tweeting = False
        
    next_tweet = wks.acell('A1').value
            
    api.update_status_with_media(next_tweet, rand_img())
    wks.delete_row(1)
         
post_tweet()