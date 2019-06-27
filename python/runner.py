import ProjectionsLoader
import ScheduleLoader
import SeasonSimulator
import PlayoffPredictor
import Settings

#TODO: Count unique playoff fields
def get_most_playoff(teams):
    most_playoffs = 0
    most_team = ''
    for team in teams:
        if teams.get(team) > most_playoffs:
            most_team = team
            most_playoffs = teams.get(team)
    teams.pop(most_team)
    return [most_team, most_playoffs]


# TODO: Allow teams and schedule to be reset to they only have to be read in once
playoff_counts = {}
for i in range(Settings.simulation_count):
    print(i)
    teams = ProjectionsLoader.load_projections()
    schedule = ScheduleLoader.load_schedule(teams)
    SeasonSimulator.simulate_season(teams, schedule)
    playoff = PlayoffPredictor.get_best_records(teams, 4)
    for team in playoff:
        if team not in playoff_counts:
            playoff_counts.update({team: 1})
        else:
            playoff_counts.update({team: playoff_counts.get(team) + 1})


while len(playoff_counts) > 0:
    team = get_most_playoff(playoff_counts)
    print(team[0] + " made the playoff " + str(team[1]) + ' times')

