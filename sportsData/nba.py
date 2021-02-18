"""
Gets NBA team data by scraping basketball-reference.com
standings

@Title: nba.py
@Author: Ty, Declan, Jack, Mphatso

"""

from scraper import *


def _set_nba_data(url):
    tables = get_tables(url)
    list = []
    for conference in tables:
        for idx in range(len(conference) - 1):
            team_dict = {"team": conference[0][idx + 1],
                         "record": conference[1][idx + 1] + "-" + conference[2][idx + 1]}
            list.append(team_dict)

    dict = {"Eastern Conference": list[0:15],
            "Western Conference": list[15:30]}
    return dict


def get_nba_data(year=2021):
    url = "https://www.basketball-reference.com/leagues/NBA_{}_standings.html".format(year)
    return _set_nba_data(url)


print(get_nba_data())
