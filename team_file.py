from player import delete_player
from player import positions_to_string
from string_formatters import team_name_modifier
from string_formatters import valid_name
from string_formatters import check_for_numbers

team_list = []

class Team:
    def __init__(self, city, name):
        try:
            formatted_city = team_name_modifier(city)
            formatted_name = team_name_modifier(name)
            valid_name(city, "City name")
            check_for_numbers(city, "City name")
            valid_name(name, "Team name")
            full_team_name = formatted_city + " " + formatted_name
            if team_exists(full_team_name):
                print(f"Unable to create the {formatted_city} {formatted_name}: Team named the {formatted_city} {formatted_name} already exists.")
            else:
                self.city = formatted_city
                self.name = formatted_name
                self.roster = []
                team_list.append(self)
                team_list.sort(key=lambda team: team.name)
                print(f"New team created: {full_team_name}")
        except ValueError as e:
            print(f"Unable to create the {formatted_city} {formatted_name}: {e}")

def team_exists(full_team_name):
    formatted_team_name = team_name_modifier(full_team_name)
    for team in team_list:
        cur_team_name = f"{team.city} {team.name}"
        if cur_team_name == formatted_team_name:
            return True
    return False

def get_team(full_team_name):
    formatted_team_name = team_name_modifier(full_team_name)
    if team_exists(formatted_team_name):
        for team in team_list:
            cur_team_name = team.city + " " + team.name
            if cur_team_name == formatted_team_name:
                return team
    else:
        raise ValueError(f"Team named \'{formatted_team_name}\' does not exist.")

def list_roster(team):
    roster = team.roster
    if len(roster) == 0:
        print(f"The roster of the {team.city} {team.name} is currently empty. Type \'new --player\' to add players to this roster.")
    else:
        print(f"{team.city} {team.name} team roster:")
        for player in roster:
            print(f"    {player.first_name} {player.last_name}: #{player.number}, {player.height_feet}\'{player.height_inches}\", {positions_to_string(player.positions)}, {player.age} years old")
        print("\n")

def delete_team(team):
    team_name = team.city + " " + team.name
    try:
        players_to_delete = []
        for player in team.roster:
            players_to_delete.append(player)
        for teammate in players_to_delete:
            delete_player(f"{teammate.first_name} {teammate.last_name}", team, teammate.number)
        team_list.remove(team)
        print(f"Team successfully deleted: {team_name}")
    except ValueError as e:
        print(f"Unable to delete team named \'{team_name}\': {e}")

def delete_all_teams():
    while len(team_list) > 0:
        delete_team(team_list[0])