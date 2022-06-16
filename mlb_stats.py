# 
import statsapi
import csv
import tweepy
from data import teams, uppercase, pitching_stats, bad_values, positions, pitching_positions
from random import randint, choice
from twitter_credentials import *

authenticator = tweepy.OAuthHandler(twitter_api_key, twitter_api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

players = []
with open('Intermediate Projects\MLB Stats\players.csv', 'r', encoding='utf8') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        players.append(row)
    
def get_rand_player():
    
    invalid = True
    
    while invalid:
        player = statsapi.player_stat_data(players[randint(0, len(players))][2])
        if player['current_team'] in teams and player['active'] != False and player['stats'] != []:
            invalid = False
    return player

def rand_img():
    img = f'assets\{randint(1, 17)}.jpg'
    return img
            
        
def get_rand_stat(player):
    
    first = player['first_name']
    last = player['last_name']
    position = positions.get(player['position'])
    current_team = player['current_team']
    team = teams.get(player['current_team'])[0]
    hashtag = teams.get(player['current_team'])[1]
        
    def get_twitter_handle():
        search = f'{first} {last} {current_team}'
        users = api.search_users(search)
        if users != []:
            for user in users:
                return f'@{user.screen_name}'
    
    
    def fix_formatting(string):

        new = ''
        for i in range(len(string)):
            if string[i] in uppercase:
                new += ' '
                new += string[i].lower()
            else:
                new += string[i]
        return new
    
    boring = True
    
    for i in range(len(player['stats'])):
        
        p = player['stats'][i]
        twitter_handle = get_twitter_handle()
        if twitter_handle != None:
            twitter_handle = f' ({twitter_handle})'
        else:
            twitter_handle = ''
        
        if player['position'] in pitching_positions and p['group'] == 'pitching':
            while boring:
                stat, value = choice(list(p['stats'].items()))
                if value not in bad_values and stat not in pitching_stats:
                    boring = False
                    return (f'{first} {last}{twitter_handle} is a {position} for the {current_team} ({team}). He has {value} {fix_formatting(stat)} this season. ⚾\n{hashtag} \n#MLB')
                elif value not in bad_values and stat in pitching_stats:
                    boring = False
                    return (f'{first} {last}{twitter_handle} is a {position} for the {current_team} ({team}). He has {value} {fix_formatting(stat)} against this season. ⚾\n{hashtag} \n#MLB')
        
        elif p['group'] == 'hitting':
            while boring:
                stat, value = choice(list(p['stats'].items()))
                if value not in bad_values:
                    boring = False
                    return (f'{first} {last}{twitter_handle} is a {position} for the {current_team} ({team}). He has {value} {fix_formatting(stat)} this season. ⚾\n{hashtag} \n#MLB')
                 