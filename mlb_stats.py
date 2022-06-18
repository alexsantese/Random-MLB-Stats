# This uses the MLB-StatsAPI Python wrapper by github.com/toddrob99
import statsapi
import csv
import tweepy
import time
from data import *
from random import randint, choice
from twitter_credentials import *

authenticator = tweepy.OAuthHandler(twitter_api_key, twitter_api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

# create a list of players to randomly pull from
players = []
with open('players.csv', 'r', encoding='utf8') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        players.append(row)
    
# get a random player and check if they are a current player on an major league team and if they have viable stats
def get_rand_player():
    
    viable = False
    
    while not viable:
        player = statsapi.player_stat_data(players[randint(0, len(players))][2])
        if player['current_team'] in teams and player['active'] != False and player['stats'] != []:
            viable = True
    # returns a player object from statsapi that we can pull information from
    return player
            
# gets a random stat for the player returned by the get_rand_player function        
def get_rand_stat(player):
    
    # pull a bunch of info from the player object
    first = player['first_name']
    last = player['last_name']
    position = positions.get(player['position'])
    
    # checks with the lists in the data.py file to get twitter handles and hashtags for the player's current team
    current_team = player['current_team']
    team = teams.get(player['current_team'])[0]
    hashtag = teams.get(player['current_team'])[1]
    
    # get the player's twitter handle (if it exists)
    # TODO: sometimes returns "parody" accounts instead of the real player's twitter handle, so let's fix this, lol
    def get_twitter_handle():
        search = f'{first} {last} {current_team}'
        users = api.search_users(search)
        if users != []:
            for user in users:
                return f'@{user.screen_name}'
    
    # check to see if the returned twitter handle exists or not, returns a blank space if no handle was found
    twitter_handle = get_twitter_handle()
    if twitter_handle != None:
        twitter_handle = f' ({twitter_handle})'
    else:
        twitter_handle = ''

    # gives us the basic player info we'll use for every version of our tweets
    player_info = f'{first} {last}{twitter_handle} is {position} for the {current_team} ({team}).'
    hashtags = f'\n{hashtag} \n#MLB'
    
    boring = True
    
    for i in range(len(player['stats'])):
        
        # most players have multiple stat dictionaries, so this will grab one randomly
        p = player['stats'][i]
        
        # if the random player is a pitcher we only want to grab their pitching stats (also same for two-way players)
        if player['position'] in pitching_positions and p['group'] == 'pitching':
            
            # checks to see if the randomly chosen stat is 0, 1, or an empty value and picks a different one if it is
            # 0 and 1 are boring stats anyway, who cares about a single stolen base?
            while boring:
                stat, value = choice(list(p['stats'].items()))
                if value not in boring_values:
                    if stat in pitcher_stats:
                        boring = False
                        return f'{player_info} He has {value} {pitcher_stats.get(stat)} this season. ⚾{hashtags}'
                    
                    elif stat in givenup_stats:
                        boring = False
                        return f'{player_info} He has given up {value} {givenup_stats.get(stat)} this season. ⚾{hashtags}'
                    
                    elif stat in against_stats:
                        boring = False
                        return f'{player_info} He has {value} {against_stats.get(stat)} against him this season. ⚾{hashtags}'
                    
                    elif stat in recorded_stats:
                        boring = False
                        return f'{player_info} He has recorded {value} {recorded_stats.get(stat)} this season. ⚾{hashtags}'
                    
                    elif stat in games_stats:
                        boring = False
                        return f'{player_info} He has {games_stats.get(stat)} {value} games this season. ⚾{hashtags}'
                    
                    elif stat in stat_first_pitching:
                        boring = False
                        return f'{player_info} He has {stat_first_pitching.get(stat)} {value} times this season. ⚾{hashtags}'
                    
                    elif stat in ratio_stats:
                        boring = False
                        return f'{player_info} He has a ratio of {value} {ratio_stats.get(stat)} this season. ⚾{hashtags}'
                    
                    elif stat in per9_stats:
                        boring = False
                        return f'{player_info} He has averaged {value} {per9_stats.get(stat)} per 9 innings this season. ⚾{hashtags}'
        
        # if the player is not a pitcher then we only care about their hitting stats, so we'll grab a hitting stat dictionary
        elif p['group'] == 'hitting':
            while boring:
                stat, value = choice(list(p['stats'].items()))
                if value not in boring_values:
                    if stat in ratio_stats:
                        boring = False
                        return f'{player_info} He has a ratio of {value} {ratio_stats.get(stat)} per 9 innings this season. ⚾{hashtags}'

                    elif stat in per9_stats:
                        boring = False
                        return f'{player_info} He has averaged {value} {per9_stats.get(stat)} per 9 innings this season. ⚾{hashtags}'
                    
                    elif stat in value_first_stats:
                        boring = False
                        return f'{player_info} He has {value} {value_first_stats.get(stat)} this season. ⚾{hashtags}'
                    
                    elif stat in stat_first_stats:
                        boring = False
                        return f'{player_info} He has {stat_first_stats.get(stat)} {value} times this season. ⚾{hashtags}' 