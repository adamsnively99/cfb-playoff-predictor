def predict_playoff(teams):
    return [get_highest_SOR(teams), get_highest_SOR(teams), get_highest_SOR(teams), get_highest_SOR(teams)]


def get_first_two_out(teams):
    return [get_highest_SOR(teams), get_highest_SOR(teams)]


def get_highest_SOR(teams):
    #for team in teams:
        #print(team)
        #print(teams.get(team))
    highest_SOR = 100000
    highest_team = 'NONE'
    for team in teams:
        if teams.get(team).get('SOR') < highest_SOR:
            highest_SOR = teams.get(team).get('SOR')
            highest_team = team
    print(teams.get(highest_team))
    teams.pop(highest_team)
    return highest_team
