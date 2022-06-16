# a lil dictionary that has all the team names and their associated @'s and #'s
teams = {'Arizona Diamondbacks': ['@Dbacks', '#RattleOn'], 'Atlanta Braves': ['@Braves', '#FortheA'], 'Baltimore Orioles': ['@Orioles', '#Birdland'], 'Boston Red Sox': ['@RedSox', '#DirtyWater'], 
         'Chicago Cubs': ['@Cubs', '#ItsDifferentHere'], 'Chicago White Sox': ['@whitesox', '#ChangeTheGame'], 'Cincinnati Reds': ['@Reds', '#ATOBTTR'], 'Cleveland Guardians': ['@CleGuardians', '#ForTheLand'],
         'Colorado Rockies': ['@Rockies', '#Rockies'], 'Detroit Tigers': ['@tigers', '#DetroitRoots'], 'Houston Astros': ['@astros', '#LevelUP'], 'Los Angeles Angels': ['@Angels', '#GoHalos'], 
         'Los Angeles Dodgers': ['@Dodgers', '#AlwaysLA'], 'Miami Marlins': ['@Marlins', '#MakeItMiami'], 'Milwaukee Brewers': ['@Brewers', '#ThisIsMyCrew'], 'Minnesota Twins': ['@Twins', '#MNTwins'], 
         'New York Mets': ['@Mets', '#LGM'], 'New York Yankees': ['@Yankees', '#RepBX'], 'Oakland Athletics': ['@Athletics', '#DrumTogether'], 'Philadelphia Phillies': ['@Phillies', '#Ring the Bell'], 
         'Pittsburgh Pirates': ['@Pirates', '#LetsGoBucs'], 'San Diego Padres': ['@Padres', '#TimeToShine'], 'Seattle Mariners': ['@Mariners', '#SeaUsRise'], 'San Francisco Giants': ['@SFGiants', '#SFGameUp'], 
         'St. Louis Cardinals': ['@Cardinals', '#STLCards'], 'Tampa Bay Rays': ['@RaysBaseball', '#RaysUp'], 'Texas Rangers': ['@Rangers', '#StraightUpTX'], 
         'Toronto Blue Jays': ['@BlueJays', '#NextLevel'], 'Washington Nationals': ['@Nationals', '#NATITUDE'], 'Kansas City Royals': ['@Royals', '#TogetherRoyal']}

# TODO: replace with another dictionary of stat types and the corresponding formatted versions
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

pitching_stats = ['runs', 'doubles', 'triples', 'homeRuns', 'hits', 'avg', 'obp', 'slg', 'ops', 'stolenBases', 'totalBases', 'sacBunts', 'sacFlies', 'atBats', 'stolenBasePercentage']

# yuck
boring_values = [0, 0.00, 1, '.---', '-.--']

positions = {'P': 'pitcher', 'C': 'catcher', '1B': 'first baseman', '2B': 'second baseman', '3B': 'third baseman', 'SS': 'shortstop', 'LF': 'left fielder', 'RF': 'right fielder', 
             'CF': 'center fielder', 'DH': 'designated hitter', 'OF': 'outfielder', 'IF': 'infielder', 'TWP': 'two-way player'}

pitching_positions = {'P': 'pitcher', 'TWP': 'two-way player'}
