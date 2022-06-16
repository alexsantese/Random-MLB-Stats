from mlb_stats import get_rand_player, get_rand_stat, rand_img, api
import time       

# the main function that pulls a tweet to post
def post_tweet():
    tweet = get_rand_stat(get_rand_player())      
    api.update_status_with_media(tweet, rand_img())
         
# wait an hour in between posts
while True:
    post_tweet()
    time.sleep(3600)