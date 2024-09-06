# NBA-customizer

NBA-customizer is a basketball league customization program and player guessing game. It includes a web scraper to collect current NBA player data from ESPN, allowing users to test their knowledge of NBA players.

## Usage

To start the program:
```
python main.py
```

Command guide:
- `help`: shows a help message
- `new (--team/--player)`: create a new team or player
- `list`:
  - `--team`: list all the teams created (sorted alphabetically by team name)
  - `--player`: list all the players created (sorted alphabetically by last name)
  - `--roster`: list the players on a specific team
  - `--all-rosters`: list all the players created, grouped by team
- `delete (--team/--player/--all)`: delete a team, player, or all created teams and players
- `change (--team/--number)`: change the team that a player is a member of or the number a player is assigned
- `load (--custom/--espn)`: load a pre-defined set of teams and players to be added to any existing teams and players
- `poeltl`: play an NBA player guessing game with the players that have been created
- `exit`: exits the program


To import data for current NBA players from ESPN:

```
pip install scrapy
cd nba_scraper/nba_scraper/spiders
scrapy runspider espn.py
```

This will generate a file `player_list.csv` which contains data that can be loaded into the program using `load --espn`.
