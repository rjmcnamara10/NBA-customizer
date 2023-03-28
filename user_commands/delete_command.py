from team_file import get_team
from team_file import delete_team
from player import delete_player
from string_formatters import team_name_modifier
from string_formatters import player_name_modifier

def delete_team_user_input():
    city_name = input("Enter the city name of where the team you would like to delete is located: ")
    team_name = input("Enter the name of the team you would like to delete: ")
    full_team_name = city_name + " " + team_name
    formatted_team_name = team_name_modifier(full_team_name)
    cancel_deletion = False
    try:
        team = get_team(formatted_team_name)
        if len(team.roster) != 0:
            print(f"This action will also delete all players on the {formatted_team_name}. Are you sure you want to continue?")
            response = input("Enter \'Y\' to delete this team and all of its players, enter any other key to cancel: ")
            if response != "Y" and response != "y":
                cancel_deletion = True
                print(f"Deletion of the {formatted_team_name} cancelled.")
        if not cancel_deletion:
            delete_team(team)
    except ValueError as e:
        print(e)
    
def delete_player_user_input():
    first_name = input("Enter the first name of the player you would like to delete: ")
    last_name = input("Enter the last name of the player you would like to delete: ")
    formatted_first_name = player_name_modifier(first_name)
    formatted_last_name = player_name_modifier(last_name)
    formatted_full_name = formatted_first_name + " " + formatted_last_name
    try:
        delete_player(formatted_full_name)
    except ValueError as e:
        if str(e) == f"Player named \'{formatted_full_name}\' does not exist, or does not exist with the given specifications (team and/or number).":
            print(f"Player named \'{formatted_full_name}\' does not exist.")
        elif str(e) == f"Multiple players named \'{formatted_full_name}\' found. Please specify which team you would like to delete \'{formatted_full_name}\' from.":
            print(e)
            delete_player_provide_team(formatted_full_name)
        else:
            print(e)
    
def delete_player_provide_team(formatted_full_name):
    city_name = input("Enter the name of the city where this team is located: ")
    team_name = input("Enter the name of this team: ")
    full_team_name = city_name + " " + team_name
    formatted_team_name = team_name_modifier(full_team_name)
    try:
        team = get_team(formatted_team_name)
        delete_player(formatted_full_name, team)
    except ValueError as e:
        if str(e) == f"Team named \'{formatted_team_name}\' does not exist.":
            print(f"{e} Please reenter which team you would like to delete \'{formatted_full_name}\' from.")
            delete_player_provide_team(formatted_full_name)
        elif str(e) == f"Player named \'{formatted_full_name}\' does not exist, or does not exist with the given specifications (team and/or number).":
            print(f"Player named \'{formatted_full_name}\' does not exist on the {formatted_team_name}. Please reenter which team you would like to delete \'{formatted_full_name}\' from.")
            delete_player_provide_team(formatted_full_name)
        elif str(e) == f"Multiple players named \'{formatted_full_name}\' found on the {formatted_team_name}. Please specify the number of which \'{formatted_full_name}\' you would like to delete.":
            print(e)
            delete_player_provide_number(formatted_full_name, team)
        else:
            print(e)

def delete_player_provide_number(formatted_full_name, team):
    number = input("Enter the number of the player you would like to delete: ")
    try:
        delete_player(formatted_full_name, team, number)
    except ValueError as e:
        if str(e) == f"Player named \'{formatted_full_name}\' does not exist, or does not exist with the given specifications (team and/or number).":
            print(f"Player named \'{formatted_full_name}\' does not exist on the {team.city} {team.name} with the number {number}. Please reenter the number of the player you would like to delete.")
            delete_player_provide_number(formatted_full_name, team)
        else:
            print(e)