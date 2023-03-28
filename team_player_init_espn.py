import csv
from team_file import Team
from team_file import get_team
from player import Player
from player import Position

def espn_position_converter(espn_pos):
    formatted_pos_list = []
    if espn_pos == "PG":
        formatted_pos_list.append(Position.POINT_GUARD)
    elif espn_pos == "SG":
        formatted_pos_list.append(Position.SHOOTING_GUARD)
    elif espn_pos == "SF":
        formatted_pos_list.append(Position.SMALL_FORWARD)
    elif espn_pos == "PF":
        formatted_pos_list.append(Position.POWER_FORWARD)
    elif espn_pos == "C":
        formatted_pos_list.append(Position.CENTER)
    elif espn_pos == "G":
        formatted_pos_list.append(Position.POINT_GUARD)
        formatted_pos_list.append(Position.SHOOTING_GUARD)
    elif espn_pos == "F":
        formatted_pos_list.append(Position.SMALL_FORWARD)
        formatted_pos_list.append(Position.POWER_FORWARD)
    else:
        raise ValueError(f"Invalid position: ({espn_pos})")
    return formatted_pos_list

def team_player_init_espn():
    with open("nba_scraper/nba_scraper/spiders/player_list.csv") as player_list:
        heading = next(player_list)
        reader = csv.reader(player_list)
        for row in reader:
            try:
                team = get_team(row[2] + " " + row[3])
                Player(row[0], row[1], team, row[4], row[5], row[6], espn_position_converter(row[8]), row[9])
            except ValueError:
                Player(row[0], row[1], Team(row[2], row[3]), row[4], row[5], row[6], espn_position_converter(row[8]), row[9])
