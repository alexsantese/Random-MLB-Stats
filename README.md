# Random-MLB-Stats

### Twitter handle for bot: 
**[@RandomMLBStats_](https://twitter.com/RandomMLBStats_)** 

This is a Twitter bot which uses MLB-StatsAPI Python wrapper to get random stats for random players and post them to Twitter. 
The players.csv file is used to get the players' id numbers and then use that as an argument for statsapi.get_player_stats_data to 
get a player dictionary object from. The dictionary is then referenced to get the name and position which is then used to check
for a random stat from a nested 'stats' dictionary. 

To keep the function from randomly returning stats that have a 0, or no value, the program checks if the stat is "boring" and 
chooses a different stat if it is. 


