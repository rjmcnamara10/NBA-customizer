from user_commands.new_command import new_team_user_input
from user_commands.new_command import new_player_user_input
from user_commands.list_command import list_user_input
from user_commands.delete_command import delete_team_user_input
from user_commands.delete_command import delete_player_user_input
from user_commands.change_command import change_team_user_input
from user_commands.change_command import change_num_user_input
from poeltl import poeltl
from team_player_init import team_player_init
from team_player_init_espn import team_player_init_espn
from team_file import delete_all_teams

help_message = """Valid commands:
    help: shows this message
    new (--team/--player): create a new team or player
    list:
        --team: list all the teams created (sorted alphabetically by team name)
        --player: list all the players created (sorted alphabetically by last name)
        --roster: list the players on a specific team
        --all-rosters: list all the players created, grouped by team
    delete (--team/--player/--all): delete a team, player, or all created teams and players
    change (--team/--number): change the team that a player is a member of or the number a player is assigned
    load (--custom/--espn): load a pre-defined set of teams and players to be added to any existing teams and players
    poeltl: play an NBA player guessing game with the players that have been created
    exit: exits the program\n"""
    
def next_command():
    user_input = input("Please enter a command: ")
    user_input_lowercase = user_input.lower()
    if user_input_lowercase == "help":
        print(help_message)
    elif user_input_lowercase == "exit":
        return
    elif user_input_lowercase[:3] == "new":
        if user_input_lowercase[4:] == "--team":
            new_team_user_input()
        elif user_input_lowercase[4:] == "--player":
            new_player_user_input()
        else:
            invalid_flags()
    elif user_input_lowercase[:4] == "list":
        list_user_input(user_input_lowercase[5:])
    elif user_input_lowercase[:6] == "delete":
        if user_input_lowercase[7:] == "--team":
            delete_team_user_input()
        elif user_input_lowercase[7:] == "--player":
            delete_player_user_input()
        elif user_input_lowercase[7:] == "--all":
            delete_all_teams()
        else:
            print("Please also add the --team, --player, or --all flag to this command.")
    elif user_input_lowercase[:6] == "change":
        if user_input_lowercase[7:] == "--team":
            change_team_user_input()
        elif user_input_lowercase[7:] == "--number":
            change_num_user_input()
        else:
            print("Please also add the --team or --number flag to this command.")
    elif user_input_lowercase == "poeltl":
        poeltl(True)
    elif user_input_lowercase[:4] == "load":
        if user_input_lowercase[5:] == "--custom":
            team_player_init()
        elif user_input_lowercase[5:] == "--espn":
            team_player_init_espn()
        else:
            print("Please also add the --custom or --espn flag to this command.")
    elif user_input_lowercase == "":
        pass
    else:
        unrecognized_command()
    next_command()
        
def unrecognized_command():
    print("Unrecognized command. Type \'help\' to see a list of valid commands.")
    
def invalid_flags():
    print("Please also add the --team or --player flag to this command.")

def main():
    print("Welcome to the NBA Customization Tool! For a list of valid commands, type \'help\', or type \'exit\' to exit.")
    next_command()

main()