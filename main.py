import gspread
from mlb_stats import get_rand_player, get_rand_stat

sa = gspread.service_account()
sh = sa.open('Random MLB Stats Sheet')

wks = sh.worksheet('Sheet1')

for i in range(1, 11):
    wks.update('A'+str(i), get_rand_stat(get_rand_player()))