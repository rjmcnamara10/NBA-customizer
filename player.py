from enum import Enum
import team_file
from string_formatters import player_name_modifier
from string_formatters import valid_name
from string_formatters import check_for_numbers

player_list = []

class Player:
    def __init__(self, first_name, last_name, team, number, height_feet, height_inches, positions, age):
        try:
            formatted_first_name = player_name_modifier(first_name)
            formatted_last_name = player_name_modifier(last_name)
            valid_name(first_name, "First name")
            check_for_numbers(first_name, "First name")
            valid_name(last_name, "Last name")
            check_for_numbers(last_name, "Last name")
            attempt_number_add_to_team(team, number)
            valid_number(number)
            valid_num_range(height_feet, "height", 0, 11)
            valid_num_range(height_inches, "height", 0, 11)
            valid_num_range(age, "age", 18, 50)
            actual_team = team_file.get_team(f"{team.city} {team.name}")
            self.first_name = formatted_first_name
            self.last_name = formatted_last_name
            self.team = actual_team
            self.number = number
            self.height_feet = int(height_feet)
            self.height_inches = int(height_inches)
            self.positions = positions
            self.age = int(age)
            player_list.append(self)
            player_list.sort(key=lambda player: player.last_name)
            actual_team.roster.append(self)
            actual_team.roster.sort(key=lambda player: player.last_name)
            print(f"{formatted_first_name} {formatted_last_name} (#{self.number}, {self.height_feet}\'{self.height_inches}\", {positions_to_string(positions)}, {self.age} years old) successfully created and added to the {team.city} {team.name}.")
        except ValueError as e:
            print(f"Unable to create {formatted_first_name} {formatted_last_name}: {e}")

class Position(Enum):
    POINT_GUARD = 1
    SHOOTING_GUARD = 2
    SMALL_FORWARD = 3
    POWER_FORWARD = 4
    CENTER = 5
    
def positions_to_string(positions):
    string = ""
    for position in positions:
        if position == Position.POINT_GUARD:
            string = string + "PG/"
        elif position == Position.SHOOTING_GUARD:
            string = string + "SG/"
        elif position == Position.SMALL_FORWARD:
            string = string + "SF/"
        elif position == Position.POWER_FORWARD:
            string = string + "PF/"
        elif position == Position.CENTER:
            string = string + "C/"
        else:
            raise ValueError(f"Given position ({position}) not supported")
    remove_final_slash = string[:len(string)-1]
    return remove_final_slash

def attempt_number_add_to_team(team, number):
    for player in team.roster:
        if player.number == number:
            raise ValueError(f"Player ({player.first_name} {player.last_name}) already exists with the number {number} on the {team.city} {team.name}.")

def valid_number(num_as_string):
    if not isinstance(num_as_string, str):
        raise ValueError("The player\'s number must be entered in String format.")
    too_high_or_low = False
    try:
        num = int(num_as_string)
        too_high_or_low = (num < 0) or (num > 99)
    except ValueError:
        raise ValueError(f"Player\'s number must be an integer. The value entered was \'{num_as_string}\'.")
    if too_high_or_low:
        raise ValueError("A player\'s number must be between 0 and 99 (00 is accepted).")
    if " " in num_as_string:
        raise ValueError("Spaces are not allowed to be included in the player\'s number.")
    if len(num_as_string) == 2:
        if (num_as_string[0] == "0") and (num_as_string[1] != "0"):
            raise ValueError("Single digit numbers cannot start with 0 (ex. \'01\' must be written as \'1\').")
    if len(num_as_string) > 2:
        raise ValueError("Player\'s number cannot be more than 2 digits long.")

def valid_num_range(num, num_type, lower_bound, upper_bound):
    invalid_num = False
    try:
        integer_num = int(num)
        invalid_num = (integer_num < lower_bound or integer_num > upper_bound)
    except ValueError:
        raise ValueError(f"{num_type.title()} value must be an integer. You entered \'{num}\'.")
    if invalid_num:
        raise ValueError(f"Value entered to represent a player\'s {num_type} must be between {lower_bound} and {upper_bound}.")

def get_player_prefix_matches(name_prefix):
    player_matches = {}
    formatted_prefix = player_name_modifier(name_prefix)
    for player in player_list:
        player_added = False
        if (player.first_name + " " + player.last_name) == formatted_prefix:
            player_matches[player] = True
            player_added = True
        if (not player_added) and (len(player.first_name) >= len(formatted_prefix)):
            shortened_first_name = player.first_name[:len(formatted_prefix)]
            if (shortened_first_name == formatted_prefix) or (shortened_first_name == name_prefix):
                player_matches[player] = False
                player_added = True
        if (not player_added) and (len(player.last_name) >= len(formatted_prefix)):
            shortened_last_name = player.last_name[:len(formatted_prefix)]
            if (shortened_last_name == formatted_prefix) or (shortened_last_name == name_prefix):
                player_matches[player] = False
                player_added = True
        if (not player_added) and (len(f"{player.first_name} {player.last_name}") >= len(formatted_prefix)):
            full_name = f"{player.first_name} {player.last_name}"
            shortened_full_name = full_name[:len(formatted_prefix)]
            if (shortened_full_name == formatted_prefix) or (shortened_full_name == name_prefix):
                player_matches[player] = False
    return player_matches
    
def get_player_matches(full_name, team=None, number=None):
    player_matches = []
    for player in player_list:
        match_found = False
        cur_player_name = player.first_name + " " + player.last_name
        if full_name == cur_player_name:
            if team == None:
                match_found = True
            else:
                if number == None:
                    match_found = team == player.team
                else:
                    cur_player_number = player.number
                    match_found = (team == player.team) and (number == cur_player_number)
            if match_found:
                player_matches.append(player)
                print(f"Player match found: {player.first_name} {player.last_name} (#{player.number}, {player.height_feet}\'{player.height_inches}\", {positions_to_string(player.positions)}, {player.age} years old) on the {player.team.city} {player.team.name}")
    return player_matches

def get_player(full_player_name, team=None, number=None):
    player_matches = get_player_matches(full_player_name, team, number)
    if len(player_matches) == 0:
        raise ValueError(f"Player named \'{full_player_name}\' does not exist, or does not exist with the given specifications (team and/or number).")
    elif len(player_matches) == 1:
        return player_matches[0]
    elif team == None:
        raise ValueError(f"Multiple players named \'{full_player_name}\' found. Please specify the team of \'{full_player_name}\'.")
    elif number == None:
        raise ValueError(f"Multiple players named \'{full_player_name}\' found on the {team.city} {team.name}. Please specify the number of \'{full_player_name}\'.")
    else:
        raise ValueError(f"Multiple players named \'{full_player_name}\' found on the {team.city} {team.name} with number {number}. This should not be possible!!!")

def delete_player(full_player_name, team=None, number=None):
    try:
        player = get_player(full_player_name, team, number)
        player.team.roster.remove(player)
        player_list.remove(player)
        print(f"Player successfully deleted: {full_player_name} (#{player.number}, {player.height_feet}\'{player.height_inches}\", {positions_to_string(player.positions)}, {player.age} years old) on the {player.team.city} {player.team.name}.")
    except ValueError as e:
        if str(e) == f"Multiple players named \'{full_player_name}\' found. Please specify the team of \'{full_player_name}\'.":
            raise ValueError(f"Multiple players named \'{full_player_name}\' found. Please specify which team you would like to delete \'{full_player_name}\' from.")
        elif (team != None) and (str(e) == f"Multiple players named \'{full_player_name}\' found on the {team.city} {team.name}. Please specify the number of \'{full_player_name}\'."):
            raise ValueError(f"Multiple players named \'{full_player_name}\' found on the {team.city} {team.name}. Please specify the number of which \'{full_player_name}\' you would like to delete.")
        else:
            raise e

def change_team(full_player_name, new_team, cur_team = None, cur_number=None, new_number=None):
    try:
        player = get_player(full_player_name, cur_team, cur_number)
        attempt_change_team(player, new_team, new_number)
    except ValueError as e:
        if str(e) == f"Multiple players named \'{full_player_name}\' found. Please specify the team of \'{full_player_name}\'.":
            raise ValueError(f"Multiple players named \'{full_player_name}\' found. Please specify which team you would like to move \'{full_player_name}\' from.")
        elif (cur_team != None) and (str(e) == f"Multiple players named \'{full_player_name}\' found on the {cur_team.city} {cur_team.name}. Please specify the number of \'{full_player_name}\'."):
            raise ValueError(f"Multiple players named \'{full_player_name}\' found on the {cur_team.city} {cur_team.name}. Please specify the number of which \'{full_player_name}\' you would like to move.")
        else:
            raise e

def attempt_change_team(player, new_team, new_number):
    formatted_full_name = player.first_name + " " + player.last_name
    cur_team = player.team
    if new_team == cur_team:
        raise ValueError(f"Team change unsuccessful: {formatted_full_name} is already on the {new_team.city} {new_team.name}.")
    if new_number == None:
        new_number = player.number
    try:
        valid_number(new_number)
        attempt_number_add_to_team(new_team, new_number)
    except ValueError as e:
        raise ValueError(f"Unable to add {formatted_full_name} to the {new_team.city} {new_team.name}: {e} Please specify a different number for {formatted_full_name}.")
    cur_team.roster.remove(player)
    player.number = new_number
    player.team = new_team
    new_team.roster.append(player)
    new_team.roster.sort(key=lambda player: player.last_name)
    print(f"{formatted_full_name} (#{player.number}, {player.height_feet}\'{player.height_inches}\", {positions_to_string(player.positions)}, {player.age} years old) successfully changed teams from the {cur_team.city} {cur_team.name} to the {player.team.city} {player.team.name}.")

def change_num(full_player_name, new_num, team=None, cur_num=None):
    formatted_full_name = player_name_modifier(full_player_name)
    try:
        player = get_player(full_player_name, team, cur_num)
        if player.number != new_num:
            try:
                valid_number(new_num)
                attempt_number_add_to_team(player.team, new_num)
                player.number = new_num
                print(f"{formatted_full_name} ({player.height_feet}\'{player.height_inches}\", #{positions_to_string(player.positions)}) on the {player.team.city} {player.team.name} successfully assigned #{new_num}.")
            except ValueError as e:
                raise ValueError(f"Unable to assign {formatted_full_name} the number {new_num}: {e} Please specify a different number for {formatted_full_name}.")
        else:
            print(f"Unable to assign #{new_num} to {formatted_full_name} because they are already #{player.number}.")
    except ValueError as e:
        if str(e) == f"Multiple players named \'{formatted_full_name}\' found. Please specify the team of \'{formatted_full_name}\'.":
            raise ValueError(f"Multiple players named \'{formatted_full_name}\' found. Please specify which team the \'{formatted_full_name}\' whose number you would like to change is on.")
        elif (team != None) and (str(e) == f"Multiple players named \'{formatted_full_name}\' found on the {team.city} {team.name}. Please specify the number of \'{formatted_full_name}\'."):
            raise ValueError(f"Multiple players named \'{formatted_full_name}\' found on the {team.city} {team.name}. Please specify the current number of which \'{formatted_full_name}\' you would like to change.")
        else:
            raise e