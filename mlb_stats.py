from random import randint, choice
from data import teams, pitchers, uppercase, pitching_stats, bad_values
import statsapi
import csv

players = []
with open('Intermediate Projects\MLB Stats\players.csv', 'r', encoding='utf8') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        players.append(row)
    
def get_rand_player():
    
    milb = True
    
    while milb:
        player = statsapi.player_stat_data(players[randint(0, len(players))][2])
        if player['current_team'] in teams:
            milb = False
    return player

def rand_img():
    img = f'assets\{randint(1, 17)}.jpg'
    return img
            
        
def get_rand_stat(player):
    
    pos = player['position']
    
    if pos == 'P':
        position = 'pitcher'
    elif pos == 'C':
        position = 'catcher'
    elif pos == '1B':
        position = 'first baseman'
    elif pos == '2B':
        position = 'second baseman'
    elif pos == '3B':
        position = 'third baseman'
    elif pos == 'SS':
        position = 'shortstop'
    elif pos == 'LF':
        position = 'left fielder'
    elif pos == 'RF':
        position = 'right fielder'
    elif pos == 'CF':
        position = 'center fielder'
    elif pos == 'DH':
        position = 'designated hitter'
    
    first = player['first_name']
    last = player['last_name']
    team = player['current_team']
    
    boring = True
    
    def fix_formatting(string):

        new = ''
        for i in range(len(string)):
            if string[i] in uppercase:
                new += ' '
                new += string[i].lower()
            else:
                new += string[i]
        return new
    
    for i in range(len(player['stats'])):
        
        p = player['stats'][i]
        
        if pos == 'P' and p['group'] == 'pitching':
            while boring:
                stat, value = choice(list(p['stats'].items()))
                if value not in bad_values and stat not in pitching_stats:
                    boring = False
                    return (f'{first} {last} is a {position} for the {team}. He has {value} {fix_formatting(stat)} this season. ⚾')
                elif value not in bad_values and stat in pitching_stats:
                    boring = False
                    return (f'{first} {last} is a {position} for the {team}. He has {value} {fix_formatting(stat)} against this season. ⚾')
        
        elif p['group'] == 'hitting':
            while boring:
                stat, value = choice(list(p['stats'].items()))
                if value not in bad_values:
                    boring = False
                    return (f'{first} {last} is a {position} for the {team}. He has {value} {fix_formatting(stat)} this season. ⚾')
