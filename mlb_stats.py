# This uses the MLB-StatsAPI Python wrapper by github.com/toddrob99
import statsapi
import csv
import tweepy
from data import teams, uppercase, pitching_stats, boring_values, positions, pitching_positions
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

# TODO: make this not a random image but correspond stadium images to the correct teams
def rand_img():
    img = f'assets\{randint(1, 17)}.jpg'
    return img
            
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
    
    
    # fixes the formatting of the stats from the player object, ex: onBasePlusSlugging --> on base plus slugging
    # some stat names don't work out, like avg, slg, obs, etc.
    # TODO: make a dictionary in data.py that contains the names I actually want for for all the possible stats
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
        
        # check to see if the returned twitter handle exists or not, returns a blank space if no handle was found
        twitter_handle = get_twitter_handle()
        if twitter_handle != None:
            twitter_handle = f' ({twitter_handle})'
        else:
            twitter_handle = ''
        
        # most players have multiple stat dictionaries, so this will grab one randomly
        p = player['stats'][i]
        
        # if the random player is a pitcher we only want to grab their pitching stats (also same for two-way players)
        if player['position'] in pitching_positions and p['group'] == 'pitching':
            
            # checks to see if the randomly chosen stat is 0, 1, or an empty value and picks a different one if it is
            # 0 and 1 are boring stats anyway, who cares about a single stolen base?
            while boring:
                stat, value = choice(list(p['stats'].items()))
                if value not in boring_values and stat not in pitching_stats:
                    boring = False
                    # formats the returned stat into a string to be posted on twitter
                    return (f'{first} {last}{twitter_handle} is a {position} for the {current_team} ({team}). He has {value} {fix_formatting(stat)} this season. ⚾\n{hashtag} \n#MLB')
                elif value not in boring_values and stat in pitching_stats:
                    boring = False
                    # this is specifically for pitching stats "against" the pitcher, ex: batting average against a given pitcher
                    return (f'{first} {last}{twitter_handle} is a {position} for the {current_team} ({team}). He has {value} {fix_formatting(stat)} against this season. ⚾\n{hashtag} \n#MLB')
        
        # if the player is not a pitcher then we only care about their hitting stats, so we'll grab a hitting stat dictionary
        elif p['group'] == 'hitting':
            while boring:
                stat, value = choice(list(p['stats'].items()))
                if value not in boring_values:
                    boring = False
                    # TODO: need to exclude "number of pitches" from the possible stats for hitters as it's not a very relevant stat
                    return (f'{first} {last}{twitter_handle} is a {position} for the {current_team} ({team}). He has {value} {fix_formatting(stat)} this season. ⚾\n{hashtag} \n#MLB')
                 