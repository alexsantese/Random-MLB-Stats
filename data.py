
teams = ['Arizona Diamondbacks', 'Atlanta Brazes', 'Baltimore Orioles', 'Boston Red Sox', 'Chicago Cubs', 'Chicago White Sox', 
         'Cincinnati Reds', 'Cleveland Guardians', 'Colorado Rockies', 'Detroit Tigers', 'Houston Astros', 'Los Angeles Angels', 
         'Los Angeles Dodgers', 'Miami Marlins', 'Milwaukee Brewers', 'Minnesota Twins', 'New York Mets', 'New York Yankees', 
         'Oakland Athletics', 'Philadelphia Phillies', 'Pittsburgh Pirates', 'San Diego Padres', 'Seattle Mariners', 'San Francisco Giants', 
         'St. Louis Cardinals', 'Tampa Bay Rays', 'Texas Rangers', 'Toronto Blue Jays', 'Washington Nationals']

pitchers = ['P', 'SP', 'CP', 'MRP', 'LRP']

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

pitching_stats = ['runs', 'doubles', 'triples', 'homeRuns', 'hits', 'avg', 'obp', 'slg', 'ops', 'stolenBases', 'totalBases', 'sacBunts', 'sacFlies', 'atBats', 'stolenBasePercentage']

bad_values = [0, '.---', '-.--']


# player = {'id': 666211, 'first_name': 'Taylor', 'last_name': 'Trammell', 'active': True, 'current_team': 'Seattle Mariners', 'position': 'CF', 'nickname': None, 'last_played': None, 'mlb_debut': '2021-04-01', 'bat_side': 'Left', 'pitch_hand': 'Left', 
 
 
#  'stats': [{'type': 'season', 'group': 'fielding', 'season': '2022', 
#                 'stats': {'assists': 0, 'putOuts': 1, 'errors': 0, 'chances': 1, 'fielding': '1.000', 'position': {'code': '8', 'name': 'Outfielder', 'type': 'Outfielder', 'abbreviation': 'CF'}, 
#                           'rangeFactorPerGame': '1.00', 'rangeFactorPer9Inn': '4.50', 'innings': '2.0', 'games': 1, 'gamesStarted': 0, 'doublePlays': 0, 'triplePlays': 0, 'throwingErrors': 0}}, 
           
           
#            {'type': 'season', 'group': 'fielding', 'season': '2022', 
#                 'stats': {'assists': 1, 'putOuts': 22, 'errors': 0, 'chances': 23, 'fielding': '1.000', 'position': {'code': '9', 'name': 'Outfielder', 'type': 'Outfielder', 'abbreviation': 'RF'}, 
#                           'rangeFactorPerGame': '1.77', 'rangeFactorPer9Inn': '2.25', 'innings': '92.0', 'games': 13, 'gamesStarted': 12, 'doublePlays': 0, 'triplePlays': 0, 'throwingErrors': 0}}, 
           
           
#            {'type': 'season', 'group': 'fielding', 'season': '2022', 
#                 'stats': {'assists': 0, 'putOuts': 0, 'errors': 0, 'chances': 0, 'fielding': '.000', 'position': {'code': '10', 'name': 'Designated Hitter', 'type': 'Hitter', 'abbreviation': 'DH'}, 
#                           'rangeFactorPerGame': '0.00', 'rangeFactorPer9Inn': '-.--', 'innings': '0.0', 'games': 1, 'gamesStarted': 1, 'doublePlays': 0, 'triplePlays': 0, 'throwingErrors': 0}}, 
           
           
#            {'type': 'season', 'group': 'hitting', 'season': '2022', 
#                 'stats': {'gamesPlayed': 14, 'groundOuts': 7, 'airOuts': 9, 'runs': 7, 'doubles': 5, 'triples': 0, 'homeRuns': 1, 'strikeOuts': 11, 'baseOnBalls': 5, 'intentionalWalks': 0, 'hits': 9, 
#                           'hitByPitch': 0, 'avg': '.265', 'atBats': 34, 'obp': '.350', 'slg': '.500', 'ops': '.850', 'caughtStealing': 1, 'stolenBases': 0, 'stolenBasePercentage': '.000', 
#                           'groundIntoDoublePlay': 0, 'numberOfPitches': 144, 'plateAppearances': 41, 'totalBases': 17, 'rbi': 5, 'leftOnBase': 14, 'sacBunts': 1, 'sacFlies': 1, 'babip': '.348', 
#                           'groundOutsToAirouts': '0.78', 'catchersInterference': 0, 'atBatsPerHomeRun': '34.00'}}]}

# pitcher = {'id': 671345, 'first_name': 'Jason', 'last_name': 'Foley', 'active': True, 'current_team': 'Detroit Tigers', 'position': 'P', 'nickname': None, 'last_played': None, 'mlb_debut': '2021-06-06', 'bat_side': 'Right', 'pitch_hand': 'Right', 
 
 
#  'stats': [{'type': 'season', 'group': 'pitching', 'season': '2022', 
#             'stats': {'gamesPlayed': 14, 'gamesStarted': 0, 'groundOuts': 26, 'airOuts': 13, 'runs': 5, 'doubles': 4, 'triples': 1, 'homeRuns': 0, 'strikeOuts': 8, 'baseOnBalls': 2, 
#                       'intentionalWalks': 0, 'hits': 17, 'hitByPitch': 0, 'avg': '.270', 'atBats': 63, 'obp': '.292', 'slg': '.365', 'ops': '.657', 'caughtStealing': 0, 'stolenBases': 2, 
#                       'stolenBasePercentage': '1.000', 'groundIntoDoublePlay': 2, 'numberOfPitches': 229, 'era': '2.70', 'inningsPitched': '16.2', 'wins': 0, 'losses': 0, 'saves': 0, 
#                       'saveOpportunities': 0, 'holds': 1, 'blownSaves': 0, 'earnedRuns': 5, 'whip': '1.14', 'battersFaced': 66, 'outs': 50, 'gamesPitched': 14, 'completeGames': 0, 'shutouts': 0, 
#                       'strikes': 161, 'strikePercentage': '.700', 'hitBatsmen': 0, 'balks': 0, 'wildPitches': 0, 'pickoffs': 0, 'totalBases': 23, 'groundOutsToAirouts': '2.00', 'winPercentage': '.---', 
#                       'pitchesPerInning': '13.74', 'gamesFinished': 4, 'strikeoutWalkRatio': '4.00', 'strikeoutsPer9Inn': '4.32', 'walksPer9Inn': '1.08', 'hitsPer9Inn': '9.18', 'runsScoredPer9': '2.70', 
#                       'homeRunsPer9': '0.00', 'inheritedRunners': 6, 'inheritedRunnersScored': 3, 'catchersInterference': 0, 'sacBunts': 1, 'sacFlies': 0}}, 
           
#            {'type': 'season', 'group': 'fielding', 'season': '2022', 
#             'stats': {'assists': 4, 'putOuts': 1, 'errors': 0, 'chances': 5, 'fielding': '1.000', 'position': {'code': '1', 'name': 'Pitcher', 'type': 'Pitcher', 'abbreviation': 'P'}, 
#                       'rangeFactorPerGame': '0.36', 'rangeFactorPer9Inn': '2.81', 'innings': '16.2', 'games': 14, 'gamesStarted': 0, 'doublePlays': 1, 'triplePlays': 0, 'throwingErrors': 0}}]}


# for i in player['stats']:
#     if player['stats'][i]['group'] != 'hitting':
#         continue
     


        