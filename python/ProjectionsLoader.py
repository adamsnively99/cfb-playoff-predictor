import Settings
from string_formatter import format_team_name
from team import Team

# TODO: Organize project into folders according to Python standards
# Returns dictionary of teams loaded from S&P+ projections CSV file specified by season in Settings.py
def load_projections():
    teams = {}
    with open(Settings.data_folder_path + Settings.simulate_season + Settings.projections_file_ending, 'r') as proj_file:
        lines = proj_file.readlines()
        for line in lines:
            team = line.split(',')
            name = format_team_name(team[0], '()')
            teams.update({name: Team(name, float(team[1]))})

    load_conferences(teams)
    return teams


def load_conferences(teams):
    with open(Settings.data_folder_path + Settings.conferences_file_ending, 'r') as conf_file:
        lines = conf_file.readlines()
        for line in lines:
            pair = line.split(',')
            name = format_team_name(pair[0], '()')
            team = teams.get(name)
            team.conference = pair[1]
            teams.update({name: team})
    return teams
