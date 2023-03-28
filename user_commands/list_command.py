from team_file import team_list
from team_file import get_team
from team_file import list_roster
from player import player_list
from player import positions_to_string

def list_user_input(flag):
    if flag == "--team":
        if len(team_list) == 0:
            print("There are currently no teams created. Type \'new --team\' to create a team or use a \'load\' command to import an existing player set.")
        else:
            for team in team_list:
                print(f"{team.city} {team.name}")
            print("\n")
    elif flag == "--player":
        if len(player_list) == 0:
            print("There are currently no players created. Type \'new --player\' to create a player.")
        else:
            for player in player_list:
                print(f"{player.first_name} {player.last_name}: {player.team.city} {player.team.name}, #{player.number}, {player.height_feet}\' {player.height_inches}\", {positions_to_string(player.positions)}, {player.age} years old")
            print("\n")
    elif flag == "--roster":
        list_roster_user_input()
    elif flag == "--all-rosters":
        if len(team_list) == 0:
            print("There are currently no teams created. Type \'new --team\' to create a team or use a \'load\' command to import an existing player set.")
        else:
            for team in team_list:
                list_roster(team)
    else:
        print("Please also add the --team, --player, --roster, or --all-rosters flag to this command.")
    
def list_roster_user_input():
    city_name = input("Enter the city name of the team whose roster you would like to view: ")
    team_name = input("Enter the name of the team whose roster you would like to view: ")
    full_team_name = city_name + " " + team_name
    try:
        team = get_team(full_team_name)
        list_roster(team)
    except ValueError as e:
        print(e)