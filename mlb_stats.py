# This uses the MLB-StatsAPI Python wrapper by github.com/toddrob99
import statsapi
import csv
from data import *
from random import randint, choice

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

player = get_rand_player()

def get_player_info(player):
    # pull a bunch of info from the player object
    first_name = player['first_name']
    last_name = player['last_name']
    position = positions.get(player['position'])
    
    # checks with the lists in the data.py file to get twitter handles and hashtags for the player's current team
    current_team = player['current_team']
    team_hashtag = teams.get(player['current_team'])[1]
    stadium = teams.get(player['current_team'])[2]

    # gives us the basic player info we'll use for every version of our tweets
    player_info = f'{first_name} {last_name} is {position} for the {current_team}\n'
    hashtags = f'\n{team_hashtag} \n#MLB'
    
    return player_info, hashtags, stadium

player_info, hashtags, stadium = get_player_info(player)
            
# gets a random stat for the player returned by the get_rand_player function        
def get_rand_stat(player):
    
    boring = True
    
    for i in range(len(player['stats'])):
        
        # most players have multiple stat dictionaries, so this will grab one randomly
        random_stat = player['stats'][i]
        
        # if the random player is a pitcher we only want to grab their pitching stats (also same for two-way players)
        if player['position'] in pitching_positions and random_stat['group'] == 'pitching':
            
            # checks to see if the randomly chosen stat is 0, 1, or an empty value and picks a different one if it is
            # 0 and 1 are boring stats anyway, who cares about a single stolen base?
            while boring:
                stat, value = choice(list(random_stat['stats'].items()))
                if value not in boring_values:
                    if stat in pitcher_stats:
                        boring = False
                        tweet_meat = f'{value} {pitcher_stats.get(stat)}'
                    
                    elif stat in givenup_stats:
                        boring = False
                        tweet_meat = f'given up {value} {givenup_stats.get(stat)}'
                    
                    elif stat in against_stats:
                        boring = False
                        tweet_meat =  f'{value} {against_stats.get(stat)} against him'
                    
                    elif stat in recorded_stats:
                        boring = False
                        tweet_meat =  f'recorded {value} {recorded_stats.get(stat)}'
                
                    elif stat in games_stats:
                        boring = False
                        tweet_meat = f'{games_stats.get(stat)} {value} games'
                    
                    elif stat in stat_first_pitching:
                        boring = False
                        tweet_meat = f'{stat_first_pitching.get(stat)} {value} times'
                    
                    elif stat in ratio_stats:
                        boring = False
                        tweet_meat = f'a ratio of {value} {ratio_stats.get(stat)}'
                    
                    elif stat in per9_stats:
                        boring = False
                        tweet_meat = f'averaged {value} {per9_stats.get(stat)} per 9 innings'
        
        # if the player is not a pitcher then we only care about their hitting stats, so we'll grab a hitting stat dictionary
        elif random_stat['group'] == 'hitting':
            while boring:
                stat, value = choice(list(random_stat['stats'].items()))
                if value not in boring_values:
                    if stat in ratio_stats:
                        boring = False
                        tweet_meat = f'a ratio of {value} {ratio_stats.get(stat)}'

                    elif stat in per9_stats:
                        boring = False
                        tweet_meat = f'averaged {value} {per9_stats.get(stat)} per 9 innings'
                    
                    elif stat in value_first_stats:
                        boring = False
                        tweet_meat = f'{value} {value_first_stats.get(stat)}'
                    
                    elif stat in stat_first_stats:
                        boring = False
                        tweet_meat = f'{stat_first_stats.get(stat)} {value} times' 
                    
    return tweet_meat

tweet_meat = get_rand_stat(player)

def make_tweet():
    return f'{player_info}He has {get_rand_stat(player)}, has {get_rand_stat(player)}, and has {get_rand_stat(player)} this season ⚾{hashtags}'