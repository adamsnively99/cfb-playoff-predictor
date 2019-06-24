def get_best_records(teams, n):
    best_records = []
    for i in range(n):
        best_records.append(get_highest_SOR(teams))
    return best_records


def get_highest_SOR(teams):
    highest_SOR = 100000
    highest_team = 'NONE'
    for team in teams:
        if teams.get(team).get('SOR') < highest_SOR:
            highest_SOR = teams.get(team).get('SOR')
            highest_team = team
    print(teams.get(highest_team))
    teams.pop(highest_team)
    return highest_team
