def load_projections():
    teams = {}
    with open('2019Projections.csv', 'r') as proj_file:
        lines = proj_file.readlines()
        for line in lines:
            team = line.split(',')
            teams.update({team[0]: {'overall_rating': float(team[1]), 'offensive_rating': float(team[3]),
                                    'defensive_rating': float(team[5]), 'name': team[0],
                                    'wins': 0, 'losses': 0, 'SOR': 1, 'conf': team[7], 'conf wins': 0,
                                    'conf losses': 0, 'wins-over': [], 'losses-to': []}})
    return teams
