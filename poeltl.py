import random
from enum import Enum

from player import Position
from player import player_list
from player import get_player_prefix_matches

class Guess_Proximity(Enum):
    CORRECT = "Correct"
    CLOSE = "Close"
    CLOSE_BUT_HIGH = "Close But High"
    CLOSE_BUT_LOW = "Close But Low"
    HIGH = "High"
    LOW = "Low"
    INCORRECT = "Incorrect"

class Conference(Enum):
    EAST = "Eastern Conference"
    WEST = "Western Conference"

class Division(Enum):
    ATLANTIC = "Atlantic Division"
    CENTRAL = "Central Division"
    SOUTHEAST = "Southeast Division"
    NORTHWEST = "Northwest Division"
    PACIFIC = "Pacific Division"
    SOUTHWEST = "Southwest Division"

def poeltl(show_instructions):
    print("New Poetl game started.")
    random_num = random.randint(0, len(player_list) - 1)
    mystery_player = player_list[random_num]
    general_positions = get_general_positions(mystery_player.positions)
    if show_instructions:
        instructions = """HOW TO PLAY:
    The goal of the game is to guess the mystery NBA player, randomly selected each game.
    For each \"guess\", you may do one of the following:
        1. Enter the full name of a player to make a guess.
        2. Enter the start of a player\'s name to list players whose names start with the same letters.
        3. Type \'hint\' to reveal a letter of the mystery player's name.
    Once you have guessed a player, their attributes will be listed.
    If an attribute is not highlighted, it is incorrect.
    If it is highlighted green, it is correct.
    If it is highlighted yellow, it is close to the correct attribute.
    Attributes may also have an arrow beside them.
    If there is an arrow pointing up, then the corresponding mystery attribute is slightly higher than what was guessed.
    If there is an arrow pointing down, the corresponding mystery attribute is slightly lower than what was guessed."""
        print(instructions)
    guess_player(mystery_player, general_positions, 1, [], 0, True, "", "")

def reveal_hint(mystery_player, general_positions, cur_guess_count, prev_guessed_players, cur_hint_count, reveal_first_name, first_so_far, last_so_far):
    if (first_so_far == mystery_player.first_name) and (last_so_far == mystery_player.last_name):
        print(f"Revealed all possible letters, the mystery player is {first_so_far} {last_so_far}")
    else:
        if reveal_first_name:
            reveal_first_name = False
            if first_so_far != mystery_player.first_name:
                next_char = mystery_player.first_name[len(first_so_far)]
                next_addition = next_char
                if ((next_char == " ") or (next_char == "\'") or (next_char == ".") or (next_char == "-")) and (len(first_so_far) < len(mystery_player.first_name) - 1):
                    next_addition = next_addition + mystery_player.first_name[len(first_so_far) + 1]
                first_so_far = first_so_far + next_addition
                print(f"First name: {first_so_far} Last name: {last_so_far}")
                guess_player(mystery_player, general_positions, cur_guess_count, prev_guessed_players, cur_hint_count + 1, reveal_first_name, first_so_far, last_so_far)
            else:
                reveal_hint(mystery_player, general_positions, cur_guess_count, prev_guessed_players, cur_hint_count, reveal_first_name, first_so_far, last_so_far)
        else:
            reveal_first_name = True
            if last_so_far != mystery_player.last_name:
                next_char = mystery_player.last_name[len(last_so_far)]
                next_addition = next_char
                if ((next_char == " ") or (next_char == "\'") or (next_char == ".") or (next_char == "-")) and (len(last_so_far) < len(mystery_player.last_name) - 1):
                    next_addition = next_addition + mystery_player.last_name[len(last_so_far) + 1]
                last_so_far = last_so_far + next_addition
                print(f"First name: {first_so_far} Last name: {last_so_far}")
                guess_player(mystery_player, general_positions, cur_guess_count, prev_guessed_players, cur_hint_count + 1, reveal_first_name, first_so_far, last_so_far)
            else:
                reveal_hint(mystery_player, general_positions, cur_guess_count, prev_guessed_players, cur_hint_count, reveal_first_name, first_so_far, last_so_far)

def guess_player(mystery_player, general_positions, cur_guess_count, prev_guessed_players, cur_hint_count, reveal_first_name, first_so_far, last_so_far):
    user_input = input("Make a guess: ")
    if len(user_input) < 3:
        print("Input must be at least 3 characters long.")
        guess_player(mystery_player, general_positions, cur_guess_count, prev_guessed_players, cur_hint_count, reveal_first_name, first_so_far, last_so_far)
    elif user_input.lower() == "hint":
        reveal_hint(mystery_player, general_positions, cur_guess_count, prev_guessed_players, cur_hint_count, reveal_first_name, first_so_far, last_so_far)
    else:
        match_dict = get_player_prefix_matches(user_input)
        if len(match_dict) == 0:
            print(f"No player matches found for the input \'{user_input}\', please try again.")
            guess_player(mystery_player, general_positions, cur_guess_count, prev_guessed_players, cur_hint_count, reveal_first_name, first_so_far, last_so_far)
        elif (len(match_dict) > 1) or not (list(match_dict.values())[0]):
            match_list = list(match_dict.keys())
            print_player_names(match_list)
            guess_player(mystery_player, general_positions, cur_guess_count, prev_guessed_players, cur_hint_count, reveal_first_name, first_so_far, last_so_far)
        else:
            cur_guess = list(match_dict.keys())[0]
            if cur_guess in prev_guessed_players:
                print(f"{cur_guess.first_name} {cur_guess.last_name} has already been guessed. Please guess again.")
                guess_player(mystery_player, general_positions, cur_guess_count, prev_guessed_players, cur_hint_count, reveal_first_name, first_so_far, last_so_far)
            else:
                if cur_guess == mystery_player:
                    correct_guess(mystery_player, general_positions, cur_guess_count, cur_hint_count)
                elif cur_guess != None:
                    incorrect_guess(mystery_player, general_positions, cur_guess, cur_guess_count, prev_guessed_players, cur_hint_count, reveal_first_name, first_so_far, last_so_far)

def print_player_names(match_list):
    max_names_shown = 6
    num_names_left = max_names_shown
    all_names = ""
    while len(match_list) > 0 and (num_names_left > 0):
        cur_list = []
        while (len(match_list) > 0) and (num_names_left > 0) and (len(cur_list) < 3):
            cur_list.append(match_list.pop(0))
            num_names_left -= 1
        names_string = ""
        for player in cur_list:
            full_name = player.first_name + " " + player.last_name
            num_spaces = 25 - len(full_name)
            space_string = ""
            while num_spaces > 0:
                space_string = space_string + " "
                num_spaces = num_spaces - 1
            names_string = names_string + full_name + space_string
        all_names = all_names + names_string + "\n"
    print("Matching players:")
    if (num_names_left == 0) and (len(match_list) > 0):
        print(f"Maximum number of names ({max_names_shown}) displayed, the list shown is not complete.")
    print(all_names[:-1])

def correct_guess(mystery_player, general_positions, cur_guess_count, cur_hint_count):
    if (cur_guess_count != 1) and (cur_hint_count != 1):
        print(f"You win! You guessed the mystery player in {cur_guess_count} guesses and used {cur_hint_count} hints!")
    elif cur_guess_count != 1:
        print(f"You win! You guessed the mystery player in {cur_guess_count} guesses and used 1 hint!")
    elif cur_hint_count != 1:
        print(f"You win! You guessed the mystery player in 1 guess and used {cur_hint_count} hints!")
    else:
        print("You win! You guessed the mystery player in 1 guess and used 1 hint!")
    print(f"Guess #{cur_guess_count} - " + convert_text_proximity(f"{mystery_player.first_name} {mystery_player.last_name}", Guess_Proximity.CORRECT) + ":")
    convert_text_proximity(general_positions_to_string(general_positions), Guess_Proximity.CORRECT)
    print("    Team: " + convert_text_proximity(f"{mystery_player.team.city} {mystery_player.team.name}", Guess_Proximity.CORRECT))
    print("    Conference: " + convert_text_proximity(get_team_conference(mystery_player.team).value, Guess_Proximity.CORRECT))
    print("    Division: " + convert_text_proximity(get_team_division(mystery_player.team).value, Guess_Proximity.CORRECT))
    print("    Number: " + convert_text_proximity(mystery_player.number, Guess_Proximity.CORRECT))
    print("    Height: " + convert_text_proximity(f"{mystery_player.height_feet}\'{mystery_player.height_inches}\"", Guess_Proximity.CORRECT))
    print("    Position: " + convert_text_proximity(general_positions_to_string(general_positions), Guess_Proximity.CORRECT))
    print("    Age: " + convert_text_proximity(str(mystery_player.age), Guess_Proximity.CORRECT))
    response = input("Enter \'Y\' to play again, enter any other key to exit the game: ")
    if response.upper() == "Y":
        poeltl(False)

def incorrect_guess(mystery_player, general_positions, cur_guess, cur_guess_count, prev_guessed_players, cur_hint_count, reveal_first_name, first_so_far, last_so_far):
    prev_guessed_players.append(cur_guess)
    print(f"Guess #{cur_guess_count} - {cur_guess.first_name} {cur_guess.last_name}:")
    teams = eval_teams(cur_guess.team, mystery_player.team)
    print("    Team: " + convert_text_proximity(f"{cur_guess.team.city} {cur_guess.team.name}", teams))
    conferences = eval_conferences_divisions(get_team_conference(cur_guess.team), get_team_conference(mystery_player.team))
    print("    Conference: " + convert_text_proximity(get_team_conference(cur_guess.team).value, conferences))
    divisions = eval_conferences_divisions(get_team_division(cur_guess.team), get_team_division(mystery_player.team))
    print("    Division: " + convert_text_proximity(get_team_division(cur_guess.team).value, divisions))
    numbers = eval_numbers(int(cur_guess.number), int(mystery_player.number))
    print("    Number: " + convert_text_proximity(cur_guess.number, numbers))
    heights = eval_numbers((cur_guess.height_feet * 12) + cur_guess.height_inches, (mystery_player.height_feet * 12) + mystery_player.height_inches)
    print("    Height: " + convert_text_proximity(f"{cur_guess.height_feet}\'{cur_guess.height_inches}\"", heights))
    guessed_general_positions = get_general_positions(cur_guess.positions)
    positions = eval_positions(guessed_general_positions, general_positions)
    print("    Position: " + convert_text_proximity(general_positions_to_string(guessed_general_positions), positions))
    ages = eval_numbers(cur_guess.age, mystery_player.age)
    print("    Age: " + convert_text_proximity(str(cur_guess.age), ages))
    guess_player(mystery_player, general_positions, cur_guess_count + 1, prev_guessed_players, cur_hint_count, reveal_first_name, first_so_far, last_so_far)

def eval_teams(guessed_team, actual_team):
    if guessed_team == actual_team:
        return Guess_Proximity.CORRECT
    else:
        return Guess_Proximity.INCORRECT

def eval_conferences_divisions(guessed_conference_division, actual_conference_division):
    if guessed_conference_division == actual_conference_division:
        return Guess_Proximity.CORRECT
    else:
        return Guess_Proximity.INCORRECT

def eval_numbers(guessed_number, actual_number):
    if guessed_number == actual_number:
        return Guess_Proximity.CORRECT
    elif actual_number > guessed_number:
        if actual_number - 3 < guessed_number:
            return Guess_Proximity.CLOSE_BUT_LOW
        else:
            return Guess_Proximity.LOW
    elif actual_number + 3 > guessed_number:
        return Guess_Proximity.CLOSE_BUT_HIGH
    else:
        return Guess_Proximity.HIGH

def eval_positions(guessed_general_positions, actual_general_positions):
    if guessed_general_positions == actual_general_positions:
        return Guess_Proximity.CORRECT
    else:
        for gen_position in guessed_general_positions:
            if gen_position in actual_general_positions:
                return Guess_Proximity.CLOSE
        return Guess_Proximity.INCORRECT

def get_general_positions(position_list):
    general_positions = []
    if (Position.POINT_GUARD in position_list) or (Position.SHOOTING_GUARD in position_list):
        general_positions.append("G")
    if (Position.SMALL_FORWARD in position_list) or (Position.POWER_FORWARD in position_list):
        general_positions.append("F")
    if (Position.CENTER in position_list):
        general_positions.append("C")
    return general_positions

def general_positions_to_string(general_positions):
    string = ""
    for gen_pos in general_positions:
        string = string + gen_pos + ", "
    remove_comma = string[:len(string) - 2]
    return remove_comma

conferences_and_divisions = {"76ers":[Conference.EAST, Division.ATLANTIC], "Celtics":[Conference.EAST, Division.ATLANTIC],
"Knicks":[Conference.EAST, Division.ATLANTIC], "Nets":[Conference.EAST, Division.ATLANTIC],
"Raptors":[Conference.EAST, Division.ATLANTIC], "Bucks":[Conference.EAST, Division.CENTRAL],
"Bulls":[Conference.EAST, Division.CENTRAL], "Cavaliers":[Conference.EAST, Division.CENTRAL],
"Pacers":[Conference.EAST, Division.CENTRAL], "Pistons":[Conference.EAST, Division.CENTRAL],
"Hawks":[Conference.EAST, Division.SOUTHEAST], "Heat":[Conference.EAST, Division.SOUTHEAST], 
"Hornets":[Conference.EAST, Division.SOUTHEAST], "Magic":[Conference.EAST, Division.SOUTHEAST], 
"Wizards":[Conference.EAST, Division.SOUTHEAST], "Jazz":[Conference.WEST, Division.NORTHWEST],
"Nuggets":[Conference.WEST, Division.NORTHWEST], "Thunder":[Conference.WEST, Division.NORTHWEST],
"Timberwolves":[Conference.WEST, Division.NORTHWEST], "Trail Blazers":[Conference.WEST, Division.NORTHWEST],
"Clippers":[Conference.WEST, Division.PACIFIC], "Kings":[Conference.WEST, Division.PACIFIC],
"Lakers":[Conference.WEST, Division.PACIFIC], "Suns":[Conference.WEST, Division.PACIFIC],
"Warriors":[Conference.WEST, Division.PACIFIC], "Grizzlies":[Conference.WEST, Division.SOUTHWEST],
"Mavericks":[Conference.WEST, Division.SOUTHWEST], "Pelicans":[Conference.WEST, Division.SOUTHWEST],
"Rockets":[Conference.WEST, Division.SOUTHWEST], "Spurs":[Conference.WEST, Division.SOUTHWEST]}

def get_team_conference(team):
    try:
        conference = conferences_and_divisions[team.name][0]
        return conference
    except KeyError:
        raise ValueError(f"Given team ({team.city} {team.name}) not in the list of NBA teams.")

def get_team_division(team):
    try:
        division = conferences_and_divisions[team.name][1]
        return division
    except KeyError:
        raise ValueError(f"Given team ({team.city} {team.name}) not in the list of NBA teams.")

def convert_text_proximity(input_text, guess_proximity):
    if guess_proximity == Guess_Proximity.CORRECT:
        return "\033[30;42m" + input_text + "\033[0m"
    elif guess_proximity == Guess_Proximity.CLOSE:
        return "\033[30;43m" + input_text + "\033[0m"
    elif guess_proximity == Guess_Proximity.CLOSE_BUT_HIGH:
        return "\033[30;43m" + input_text + u" \u2193" + "\033[0m"
    elif guess_proximity == Guess_Proximity.CLOSE_BUT_LOW:
        return "\033[30;43m" + input_text + u" \u2191" + "\033[0m"
    elif guess_proximity == Guess_Proximity.HIGH:
        return input_text + u" \u2193"
    elif guess_proximity == Guess_Proximity.LOW:
        return input_text + u" \u2191"
    elif guess_proximity == Guess_Proximity.INCORRECT:
        return input_text
    else:
        raise ValueError(f"Guess proximity ({guess_proximity}) not supported.")