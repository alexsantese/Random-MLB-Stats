from mlb_stats import get_rand_player, get_rand_stat, rand_img, api
import time       

def post_tweet():
    
    tweet = get_rand_stat(get_rand_player())
            
    api.update_status_with_media(tweet, rand_img())
         
post_tweet()
# time.sleep(3600)