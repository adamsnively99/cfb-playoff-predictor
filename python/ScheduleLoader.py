import Settings
import string_formatter


# Returns schedule of FBS games in season
def load_schedule(teams):
    schedule = []
    with open(Settings.data_folder_path + Settings.simulate_season + Settings.schedule_file_ending, 'r') \
            as schedule_file:
        lines = schedule_file.readlines()
        for line in lines:
            game = line.split(',')
            add_game_to_schedule(teams, game, schedule)

    return schedule


def add_game_to_schedule(teams, game, schedule):
    team_a = string_formatter.format_team_name(game[8], "()1234560789")
    team_b = string_formatter.format_team_name(game[5], "()1234560789")
    slate = configure_home_away_teams(teams, game, team_a, team_b)
    home_team = slate[0]
    away_team = slate[1]
    schedule.append({'home_team': home_team, 'visiting_team': away_team, 'week': game[1],
                         'neutral_site': is_neutral_site(game)})


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
