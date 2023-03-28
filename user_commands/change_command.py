from team_file import get_team
from player import change_team
from player import change_num
from string_formatters import team_name_modifier
from string_formatters import player_name_modifier

def change_team_user_input():
    first_name = input("Enter the first name of the player whose team you would like to change: ")
    last_name = input("Enter the last name of the player whose team you would like to change: ")
    formatted_first_name = player_name_modifier(first_name)
    formatted_last_name = player_name_modifier(last_name)
    formatted_full_name = formatted_first_name + " " + formatted_last_name
    new_team = get_team_loop()
    try:
        change_team(formatted_full_name, new_team)
    except ValueError as e:
        if str(e) == f"Player named \'{formatted_full_name}\' does not exist, or does not exist with the given specifications (team and/or number).":
            print(f"Player named \'{formatted_full_name}\' does not exist.")
        elif str(e)[:13] == "Unable to add":
            print(e)
            change_team_provide_new_number(formatted_full_name, new_team)
        elif str(e) == f"Multiple players named \'{formatted_full_name}\' found. Please specify which team you would like to move \'{formatted_full_name}\' from.":
            print(e)
            change_team_provide_team(formatted_full_name, new_team)
        else:
            print(e)
            
def get_team_loop():
    city_name = input("Enter the name of the city where the player\'s new team is located: ")
    team_name = input("Enter the name of the player\'s new team: ")
    full_team_name = city_name + " " + team_name
    try:
        team = get_team(full_team_name)
        return team
    except ValueError as e:
        print(e)
        return get_team_loop()
        
def change_team_provide_new_number(formatted_full_name, new_team, old_team=None, number=None):
    new_number = input(f"Enter a new number for {formatted_full_name}: ")
    try:
        change_team(formatted_full_name, new_team, old_team, number, new_number)
    except ValueError as e:
        if str(e)[:13] == "Unable to add":
            print(e)
            change_team_provide_new_number(formatted_full_name, new_team, old_team, number)
        else:
            print(e)
        
def change_team_provide_team(formatted_full_name, new_team):
    city_name = input(f"Enter the name of the city where {formatted_full_name}\'s current team is located: ")
    team_name = input(f"Enter the name of {formatted_full_name}\'s current team: ")
    full_team_name = city_name + " " + team_name
    formatted_team_name = team_name_modifier(full_team_name)
    try:
        old_team = get_team(formatted_team_name)
        change_team(formatted_full_name, new_team, old_team)
    except ValueError as e:
        if str(e) == f"Team named \'{formatted_team_name}\' does not exist.":
            print(f"{e} Please reenter which team you would like to move \'{formatted_full_name}\' from.")
            change_team_provide_team(formatted_full_name, new_team)
        elif str(e) == f"Player named \'{formatted_full_name}\' does not exist, or does not exist with the given specifications (team and/or number).":
            print(f"Player named \'{formatted_full_name}\' does not exist on the {formatted_team_name}. Please reenter which team you would like to move \'{formatted_full_name}\' from.")
            change_team_provide_team(formatted_full_name, new_team)
        elif str(e)[:13] == "Unable to add":
            print(e)
            change_team_provide_new_number(formatted_full_name, new_team, old_team)
        elif str(e) == f"Multiple players named \'{formatted_full_name}\' found on the {formatted_team_name}. Please specify the number of which \'{formatted_full_name}\' you would like to move.":
            print(e)
            change_team_provide_number(formatted_full_name, new_team, old_team)
        else:
            print(e)
            
def change_team_provide_number(formatted_full_name, new_team, old_team):
    number = input(f"Enter the number of which \'{formatted_full_name}\' you would like to move: ")
    try:
        change_team(formatted_full_name, new_team, old_team, number)
    except ValueError as e:
        if str(e) == f"Player named \'{formatted_full_name}\' does not exist, or does not exist with the given specifications (team and/or number).":
            print(f"Player named \'{formatted_full_name}\' does not exist on the {old_team.city} {old_team.name} with the number {number}. Please reenter the number of the player you would like to delete.")
            change_team_provide_number(formatted_full_name, new_team, old_team)
        elif str(e)[:13] == "Unable to add":
            print(e)
            change_team_provide_new_number(formatted_full_name, new_team, old_team, number)
        else:
            print(e)

def change_num_user_input():
    first_name = input("Enter the first name of the player whose number you would like to change: ")
    last_name = input("Enter the last name of the player whose number you would like to change: ")
    formatted_first_name = player_name_modifier(first_name)
    formatted_last_name = player_name_modifier(last_name)
    formatted_full_name = formatted_first_name + " " + formatted_last_name
    new_num = input("Enter the new number to be assigned to this player: ")
    try:
        change_num(formatted_full_name, new_num)
    except ValueError as e:
        if str(e) == f"Player named \'{formatted_full_name}\' does not exist, or does not exist with the given specifications (team and/or number).":
            print(f"Player named \'{formatted_full_name}\' does not exist.")
        elif str(e)[:16] == "Unable to assign":
            print(e)
            change_num_provide_new_number(formatted_full_name)
        elif str(e) == f"Multiple players named \'{formatted_full_name}\' found. Please specify which team the \'{formatted_full_name}\' whose number you would like to change is on.":
            print(e)
            change_num_provide_team(formatted_full_name, new_num)
        else:
            print(e)

def change_num_provide_new_number(formatted_full_name, team=None, cur_num=None):
    new_num = input("Enter the new number to be assigned to this player: ")
    try:
        change_num(formatted_full_name, new_num, team, cur_num)
    except ValueError as e:
        if str(e)[:16] == "Unable to assign":
            print(e)
            change_num_provide_new_number(formatted_full_name, team, cur_num)
        else:
            print(e)

def change_num_provide_team(formatted_full_name, new_num):
    city_name = input(f"Enter the city where {formatted_full_name}\'s team is located: ")
    team_name = input(f"Enter the name of {formatted_full_name}\'s team: ")
    full_team_name = city_name + " " + team_name
    formatted_team_name = team_name_modifier(full_team_name)
    try:
        team = get_team(formatted_team_name)
        change_num(formatted_full_name, new_num, team)
    except ValueError as e:
        if str(e) == f"Team named \'{formatted_team_name}\' does not exist.":
            print(f"{e} Please reenter which team you would like to move \'{formatted_full_name}\' from.")
            change_num_provide_team(formatted_full_name, new_num)
        elif str(e) == f"Player named \'{formatted_full_name}\' does not exist, or does not exist with the given specifications (team and/or number).":
            print(f"Player named \'{formatted_full_name}\' does not exist on the {formatted_team_name}. Please reenter which team you would like to move \'{formatted_full_name}\' from.")
            change_num_provide_team(formatted_full_name, new_num)
        elif str(e)[:16] == "Unable to assign":
            print(e)
            change_num_provide_new_number(formatted_full_name, team)
        elif str(e) == f"Multiple players named \'{formatted_full_name}\' found on the {formatted_team_name}. Please specify the current number of which \'{formatted_full_name}\' you would like to change.":
            print(e)
            change_num_provide_number(formatted_full_name, new_num, team)
        else:
            print(e)

def change_num_provide_number(formatted_full_name, new_num, team):
    cur_num = input(f"Enter the number of which \'{formatted_full_name}\' whose number you would like to change: ")
    try:
        change_num(formatted_full_name, new_num, team, cur_num)
    except ValueError as e:
        if str(e) == f"Player named \'{formatted_full_name}\' does not exist, or does not exist with the given specifications (team and/or number).":
            print(f"Player named \'{formatted_full_name}\' does not exist on the {team.city} {team.name} with the number {cur_num}. Please reenter the number of the player you would like to delete.")
            change_num_provide_number(formatted_full_name, new_num, team)
        elif str(e)[:16] == "Unable to assign":
            print(e)
            change_num_provide_new_number(formatted_full_name, team, cur_num)
        else:
            print(e)