import Settings
import string_formatter
from game import Game


# Returns schedule of FBS games in season
def load_schedule(teams):
    schedule = []
    with open(Settings.data_folder_path + Settings.simulate_season + Settings.schedule_file_ending, 'r') as schedule_file:
        lines = schedule_file.readlines()
        for line in lines:
            game_input = line.split(',')
            add_game_to_schedule(teams, game_input, schedule)

    return schedule


def add_game_to_schedule(teams, game_input, schedule):
    team_a = string_formatter.format_team_name(game_input[8], "()1234560789")
    team_b = string_formatter.format_team_name(game_input[5], "()1234560789")
    slate = configure_home_away_teams(teams, game_input, team_a, team_b)
    home_team = slate[0]
    away_team = slate[1]
    game = Game(home_team, away_team, is_neutral_site(game_input))
    if len(game_input[6]) > 0 and len(game_input[9]) > 0 and Settings.use_played_games:
        game.set_outcome(team_b, team_a)
    print(team_a)
    print(team_b)
    schedule.append(game)


def is_neutral_site(game):
    return len(game[11]) > 0 and game[11] != '\n'


def configure_home_away_teams(teams, game, away, home):
    if len(game[7]) > 0:
        temp = away
        away = home
        home = temp

    if away not in teams:
        away = Settings.fcs
    elif home not in teams:
        home = Settings.fcs
    return [home, away]
