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


def update_playoff_appearance_counts(playoff_counts, playoff, teams):
    for team in playoff:
        teams.get(team).update_playoff_berths()
        if team not in playoff_counts:
            playoff_counts.update({team: 1})
        else:
            playoff_counts.update({team: playoff_counts.get(team) + 1})


def update_playoff_field_counts(playoff_fields, playoff):
    playoff_field = str(playoff)
    if str(playoff_field) not in playoff_fields:
        playoff_fields.update({str(playoff_field): 1})
    else:
        playoff_fields.update({str(playoff_field): playoff_fields.get(str(playoff_field)) + 1})


def reset_teams(teams):
    for team_name in teams:
        teams.get(team_name).reset()


# TODO: Multithread these simulations
team_playoff_appearances = {}
playoff_field_counts = {}
teams = ProjectionsLoader.load_projections()
schedule = ScheduleLoader.load_schedule(teams)
stdev_ratings = SeasonSimulator.calc_stdev_ratings(teams)
avg_top_team = SeasonSimulator.calc_avg_top_team(teams)

for i in range(Settings.simulation_count):
    print(i)
    SeasonSimulator.simulate_season(teams, schedule, stdev_ratings, avg_top_team)
    playoff = PlayoffPredictor.get_best_records(teams, 4)
    update_playoff_appearance_counts(team_playoff_appearances, playoff, teams)
    update_playoff_field_counts(playoff_field_counts, playoff)
    reset_teams(teams)


while len(team_playoff_appearances) > 0:
    team = get_most_playoff(team_playoff_appearances)
    print(team[0] + " made the playoff " + str(team[1]) + ' times')

# Todo: Sort Playoff fields by occurrences
for playoff in playoff_field_counts:
    print(str(playoff) + ": " + str(playoff_field_counts.get(playoff)))

