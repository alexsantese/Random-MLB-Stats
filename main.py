from mlb_stats import get_rand_player, get_rand_stat, api
from data import teams
import time       

# the main function that pulls a tweet to post
def post_tweet():
    player = get_rand_player()
    stadium = teams.get(player['current_team'])[2]
    
    tweet = get_rand_stat(player)      
    api.update_status_with_media(tweet, stadium)
         
# wait an hour in between posts
while True:
    post_tweet()
    time.sleep(3600)