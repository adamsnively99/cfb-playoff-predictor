import Settings

# TODO: Organize project into folders according to Python standards
# TODO: Extract string reformatting out of this class
# Returns dictionary of teams loaded from S&P+ projections CSV file specified by season in Settings.py
def load_projections():
    teams = {}
    # TODO: Take hardcoded filepaths out and put into settings.py
    with open('cfb-playoff-predictor/data/' + Settings.simulate_season + 'Projections.csv', 'r') as proj_file:
        lines = proj_file.readlines()
        for line in lines:
            team = line.split(',')
            name = team[0]
            for c in "()":
                name = name.replace(c, '')
            teams.update({name: {'overall_rating': float(team[1]), 'offensive_rating': float(team[3]),
                                    'defensive_rating': float(team[5]), 'name': name,
                                    'wins': 0, 'losses': 0, 'SOR': 1, 'conf wins': 0,
                                    'conf losses': 0, 'wins-over': [], 'losses-to': []}})

    with open ('cfb-playoff-predictor/data/' + 'conferences.csv', 'r') as conf_file:
        lines = conf_file.readlines()
        for input in lines:
            line = input.split(',')
            name = line[0]
            for c in "()1234560789":
                name = name.replace(c, '')
            name = name.strip()
            team = teams.get(name)
            team.update({'conf': line[1]})
            teams.update({name: team})
    return teams
