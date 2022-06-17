# a lil dictionary that has all the team names and their associated @'s and #'s
teams = {'Arizona Diamondbacks': ['@Dbacks', '#Dbacks', 'assets/dbacks.jpg'], 'Atlanta Braves': ['@Braves', '#FortheA', 'assets/braves.jpg'], 'Baltimore Orioles': ['@Orioles', '#Birdland', 'assets/orioles.jpg'], 'Boston Red Sox': ['@RedSox', '#DirtyWater', 'assets/redsox.jpg'], 
         'Chicago Cubs': ['@Cubs', '#ItsDifferentHere', 'assets/cubs.jpg'], 'Chicago White Sox': ['@whitesox', '#ChangeTheGame', 'assets/whitesox.jpg'], 'Cincinnati Reds': ['@Reds', '#ATOBTTR', 'assets/reds.jpg'], 'Cleveland Guardians': ['@CleGuardians', '#ForTheLand', 'assets/cle.jpg'],
         'Colorado Rockies': ['@Rockies', '#Rockies', 'assets/coors.jpg'], 'Detroit Tigers': ['@tigers', '#DetroitRoots', 'assets/tigers.jpg'], 'Houston Astros': ['@astros', '#LevelUP', 'assets/astros.jpg'], 'Los Angeles Angels': ['@Angels', '#GoHalos', 'assets/angels.jpg'], 
         'Los Angeles Dodgers': ['@Dodgers', '#AlwaysLA', 'assets/dodgers.jpg'], 'Miami Marlins': ['@Marlins', '#MakeItMiami', 'assets/marlins.jpg'], 'Milwaukee Brewers': ['@Brewers', '#ThisIsMyCrew', 'assets/brewers.jpg'], 'Minnesota Twins': ['@Twins', '#MNTwins', 'assets/twins.jpg'], 
         'New York Mets': ['@Mets', '#LGM', 'assets/mets.jpg'], 'New York Yankees': ['@Yankees', '#RepBX', 'assets/yankees.jpg'], 'Oakland Athletics': ['@Athletics', '#DrumTogether', 'assets/athletics.jpg'], 'Philadelphia Phillies': ['@Phillies', '#Ring the Bell', 'assets/phillies.jpg'], 
         'Pittsburgh Pirates': ['@Pirates', '#LetsGoBucs', 'assets/pirates.jpg'], 'San Diego Padres': ['@Padres', '#TimeToShine', 'assets/padres.jpg'], 'Seattle Mariners': ['@Mariners', '#SeaUsRise', 'assets/mariners.jpg'], 'San Francisco Giants': ['@SFGiants', '#SFGameUp', 'assets/giants.jpg'], 
         'St. Louis Cardinals': ['@Cardinals', '#STLCards', 'assets/cards.jpg'], 'Tampa Bay Rays': ['@RaysBaseball', '#RaysUp', 'assets/rays.jpg'], 'Texas Rangers': ['@Rangers', '#StraightUpTX', 'assets/rangers.jpg'], 
         'Toronto Blue Jays': ['@BlueJays', '#NextLevel', 'assets/bluejays.jpg'], 'Washington Nationals': ['@Nationals', '#NATITUDE', 'assets/nats.jpg'], 'Kansas City Royals': ['@Royals', '#TogetherRoyal', 'assets/kc.jpg']}


# stats only for pitchers --> 2.39 ERA
# used for pitchers
pitcher_stats = {'numberOfPitches': 'total pitches', 'era': 'ERA', 'winPercentage': 'win percentage',  
                 'inningsPitched': 'innings pitched','holds': 'holds', 'balks': 'balks', 'whip': 'WHIP', 'strikePercentage': 'strike percentage', 'winPercentage': 'win percentage', 
                 'pitchesPerInning': 'pitches per inning', 'inheritedRunners': 'inherited runners'}

# stats formatted with "given up" --> given up 13 runs
# used for pitchers
givenup_stats = {'runs': 'runs', 'doubles': 'doubles', 'triples': 'triples', 'homeRuns': 'home runs', 'hits': 'hits', 'totalBases': 'bases', 'earnedRuns': 'earned runs'}


# stats to be formatted with "against" --> .297 batting average against him
# used for pitchers
against_stats = {'avg': 'batting average', 'obp': 'OBP', 'slg': 'SLG', 'ops': 'OPS', 'stolenBases': 'stolen bases', 'sacBunts': 'sac bunts', 'sacFlies': 'sac flies', 
                 'stolenBasePercentage': 'stolen base percentage'}

# mainly meant for pitchers formatted as --> recorded 25 outs
# used for pitchers
recorded_stats = {'outs': 'outs', 'strikeOuts': 'strike outs', 'wildPitches': 'wild pitches', 'shutouts': 'shut outs', 'completeGames': 'complete games', 'strikes': 'strikes', 'pickoffs': 'pickoffs'}

# stats about how many games played or started --> started 10 games
# used for pitchers
games_stats = {'gamesPlayed': 'played', 'gamesStarted': 'started', 'gamesPitched': 'pitched', 'blownSaves': 'blown the save of', 'saveOpportunities': 'had the opportunity to save', 
               'finishedGames': 'finished', 'wins': 'won', 'losses': 'lost', 'saves': 'saved'}

# pitching stats where I want the name first --> hit a batter 8 times
# used for pitchers
stat_first_pitching = {'hitBatsmen': 'hit a batter', 'inheritedRunnersScored': 'let inherited runners score', 'battersFaced': 'faced a batter', 'groundIntoDoublePlay': 'forced a grounder into a double play',
                       'catchersInterference': 'had a catcher interfere'}

# ratio stats --> a ratio of 1.19 ground outs to air outs
# used for pitchers and hitters
ratio_stats = {'groundOutsToAirOuts': 'ground outs to air outs', 'strikeoutWalkRatio': 'strike outs to walks', 'atBatsPerHomeRun': 'at bats per home run'}

# stats that give per 9 inning avg --> averaged 1.3 walks per 9 innings
# used for pitchers and hitters
per9_stats = {'walksPer9Inn': 'walks', 'hitsPer9Inn': 'hits', 'runsScoredPer9': 'runs', 'homeRunsPer9': 'home runs', 'strikeOutsPer9Inn': 'strike outs'}

# stats where I want the value first --> .397 batting average
# used for hitters
value_first_stats = {'avg': 'batting average', 'atBats': 'at bats', 'obp': 'OBP', 'slg': 'SLG', 'ops': 'OPS', 'groundOuts': 'ground outs', 'airOuts': 'air outs', 'runs': 'runs', 
                     'doubles': 'doubles', 'triples': 'triples', 'baseOnBalls': 'walks', 'hits': 'hits', 'stolenBases': 'stolen bases', 'sacBunts': 'sac bunts', 'sacFlies': 'sac flies',
                     'plateAppearances': 'plate appearances', 'totalBases': 'total bases', 'rbi': 'RBIs', 'babip': 'BABIP', 'stolenBasePercentage': 'SB%'}

# stats where I want the stat name first --> homered 12 times
# used for hitters
stat_first_stats = {'homeRuns': 'homered', 'groundIntoDoublePlay': 'grounded into a double play', 'numberOfPitches': 'thrown the ball', 'catchersInterference': 'had a catcher interfere',
                    'intentionalWalks': 'been intentionally walked', 'hitByPitch': 'been hit by a pitch', 'caughtStealing': 'been caught stealing', 'leftOnBase': 'been left on base', 
                    'strikeOuts': 'been struck out'}

# TODO: decide if fielding stats are worth bothering with since most of them are boring, lol
# fielding_stats = ['assists', 'putOuts', 'errors', 'chances', 'fielding', 'rangeFactorPerGame', 'rangeFactorPer9Inn', 'innings', 'games', 'gamesStarted', 'doublePlays', 'triplePlays', 'throwingErrors']

# yuck
boring_values = [0, 0.00, 0.0, .000, .00,  1, 1.0, 1.00, 1.000, '0.00', '.---', '-.--']

# dictionary of all the positions and the value I actually want to display them as 
positions = {'P': 'a pitcher', 'C': 'a catcher', '1B': 'a first baseman', '2B': 'a second baseman', '3B': 'a third baseman', 'SS': 'a shortstop', 'LF': 'a left fielder', 'RF': 'a right fielder', 
             'CF': 'a center fielder', 'DH': 'a designated hitter', 'OF': 'an outfielder', 'IF': 'an infielder', 'TWP': 'a two-way player'}

pitching_positions = {'P': 'pitcher', 'TWP': 'two-way player'}
