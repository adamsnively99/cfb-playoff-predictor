import ProjectionsLoader
import ScheduleLoader
import SeasonSimulator
import PlayoffPredictor
import Settings


def get_most_playoff(playoff_counts):
    most_playoffs = 0
    most_team = ''
    for team in playoff_counts:
        if playoff_counts.get(team) > most_playoffs:
            most_team = team
            most_playoffs = playoff_counts.get(team)
    playoff_counts.pop(most_team)
    return [most_team, most_playoffs]


# TODO: Factor all code in runner.py into methods
playoff_counts = {}
playoff_fields = {}
teams = ProjectionsLoader.load_projections()
schedule = ScheduleLoader.load_schedule(teams)

for i in range(Settings.simulation_count):
    print(i)
    SeasonSimulator.simulate_season(teams, schedule)
    playoff = PlayoffPredictor.get_best_records(teams, 4)
    for team in playoff:
        if team not in playoff_counts:
            playoff_counts.update({team: 1})
        else:
            playoff_counts.update({team: playoff_counts.get(team) + 1})

    playoff_field = str(playoff)

    if str(playoff_field) not in playoff_fields:
        playoff_fields.update({str(playoff_field): 1})
    else:
        playoff_fields.update({str(playoff_field): playoff_fields.get(str(playoff_field)) + 1})

    for team_name in teams:
        teams.get(team_name).reset()


while len(playoff_counts) > 0:
    team = get_most_playoff(playoff_counts)
    print(team[0] + " made the playoff " + str(team[1]) + ' times')

# Todo: Sort Playoff fields by occurrences
for playoff in playoff_fields:
    print(str(playoff) + ": " + str(playoff_fields.get(playoff)))

