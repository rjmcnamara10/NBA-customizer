from team_file import Team
from team_file import team_exists
from team_file import get_team
from player import Player
from player import Position
from player import valid_number
from player import valid_num_range
from string_formatters import team_name_modifier
from string_formatters import valid_name

def new_team_user_input():
    city = name_helper("Enter the city where the team is located: ", "City name")
    team_name = name_helper("Enter the name of the team: ", "Team name")
    full_team_name = f"{city} {team_name}"
    if team_exists(full_team_name):
        print(f"Team with the name \'{team_name_modifier(full_team_name)}\' already exists")
    else:
        Team(city, team_name)

def new_player_user_input():
    first_name = name_helper("Enter the player\'s first name: ", "First name")
    last_name = name_helper("Enter the player\'s last name: ", "Last name")
    team = set_player_team_user_input()
    number = player_jersey_number_helper()
    height_feet = height_helper("feet")
    height_inches = height_helper("inches")
    list_of_positions = player_positions_helper()
    converted_positions = position_converter(list_of_positions)
    age = age_helper()
    Player(first_name, last_name, team, number, height_feet, height_inches, converted_positions, age)
    
def name_helper(input_message, name_type):
    name = input(input_message)
    try:
        valid_name(name, name_type)
        return name
    except ValueError as e:
        print(e)
        return name_helper(input_message, name_type)
        
def set_player_team_user_input():
    city = name_helper("Enter the city where the player\'s team is located: ", "City name")
    team_name = name_helper("Enter the name of the player\'s team: ", "Team name")
    full_team_name = city + " " + team_name
    try:
        get_team(full_team_name)
    except ValueError:
        Team(city, team_name)
    try:
        team = get_team(full_team_name)
        return team
    except ValueError:
        return set_player_team_user_input()
    
def player_jersey_number_helper():
    num_as_string = input("Enter the player\'s number: ")
    try:
        valid_number(num_as_string)
        return num_as_string
    except ValueError as e:
        print(f"Invalid number: {e}")
        return player_jersey_number_helper()

def height_helper(height_type):
    height = input("Enter how many " + height_type + " tall the player is: ")
    try:
        valid_num_range(height, "height", 0, 11)
        height_int = int(height)
        return height_int
    except ValueError as e:
        print(e)
        return height_helper(height_type)

def age_helper():
    age = input("Enter how many years old the player is: ")
    try:
        valid_num_range(age, "age", 18, 50)
        age_int = int(age)
        return age_int
    except ValueError as e:
        print(e)
        return age_helper()
    
def player_positions_helper():
    print("Players must have at least one position and can have at most 5.")
    print("Valid positions: PG SG SF PF C")
    print("Enter \'DONE\' or click enter when you have added all of the player\'s positions.")
    return prompt_for_first_pos()
    
def valid_position(uppercase_position, cur_pos_list):
    full_pos_list = ["PG", "SG", "SF", "PF", "C"]
    in_cur_list = uppercase_position in cur_pos_list
    in_full_list = uppercase_position in full_pos_list
    return (not (in_cur_list)) and in_full_list
    
def prompt_for_first_pos():
    pos1 = input("Enter the player\'s primary position: ")
    pos1_uppercase = pos1.upper()
    cur_pos_list = []
    if valid_position(pos1_uppercase, cur_pos_list):
        cur_pos_list.append(pos1_uppercase)
        print(f"Position {pos1_uppercase} added.")
        return prompt_for_next_pos(cur_pos_list)
    elif (pos1_uppercase == "DONE") or (pos1_uppercase == ""):
        print("Players must have at least one position.")
        return prompt_for_first_pos()
    else:
        print("Invalid position. Valid positions are limited to: PG SG SF PF C")
        return prompt_for_first_pos()
    
def prompt_for_next_pos(cur_pos_list):
    pos = input("Enter the player\'s next position: ")
    pos_uppercase = pos.upper()
    if (pos_uppercase == "DONE") or (pos_uppercase == ""):
        return cur_pos_list
    elif valid_position(pos_uppercase, cur_pos_list):
        cur_pos_list.append(pos_uppercase)
        print(f"Position {pos_uppercase} added.")
        return prompt_for_next_pos(cur_pos_list)
    else:
        print("Invalid position or position has already been added. Valid positions are limited to: PG SG SF PF C")
        print("Enter \'DONE\' or click enter if you are finished adding positions.")
        print(f"Current position list: {cur_pos_list}")
        return prompt_for_next_pos(cur_pos_list)
        
def position_converter(list_of_positions):
    formatted_pos_list = []
    for pos in list_of_positions:
        if pos == "PG":
            formatted_pos_list.append(Position.POINT_GUARD)
        elif pos == "SG":
            formatted_pos_list.append(Position.SHOOTING_GUARD)
        elif pos == "SF":
            formatted_pos_list.append(Position.SMALL_FORWARD)
        elif pos == "PF":
            formatted_pos_list.append(Position.POWER_FORWARD)
        elif pos == "C":
            formatted_pos_list.append(Position.CENTER)
        else:
            raise ValueError(f"Invalid position: ({pos})")
    return formatted_pos_list