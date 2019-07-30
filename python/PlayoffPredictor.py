from team import Team
def get_best_records(teams, n):
    best_records = []
    for i in range(n):
        get_highest_SOR(teams, best_records)
    best_records.sort()
    return best_records


def get_highest_SOR(teams, best_records):
    highest_SOR = 100000
    highest_team = 'NONE'
    for team in teams:
        if teams.get(team).strength_of_record < highest_SOR and team not in best_records:
            highest_SOR = teams.get(team).strength_of_record
            highest_team = team
    best_records.append(highest_team)
