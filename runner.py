import ProjectionsLoader
import ScheduleLoader
import SeasonSimulator
import PlayoffPredictor


playoff_counts = {}
for i in range(5000):
    teams = ProjectionsLoader.load_projections()
    schedule = ScheduleLoader.load_schedule(teams)
    SeasonSimulator.simulate_season(teams, schedule)

    playoff = PlayoffPredictor.get_best_records(teams, 4)
    out = PlayoffPredictor.get_best_records(teams, 4)
    for team in playoff:
        print('playoff ' + str(i) + ' contains: ' + team)
        if team not in playoff_counts:
            playoff_counts.update({team: 1})
        else:
            playoff_counts.update({team: playoff_counts.get(team) + 1})

    for team in out:
        print('playoff ' + str(i) + ' leave: ' + team + ' out')

for team in playoff_counts:
    print(team + " made the playoff " + str(playoff_counts.get(team)) + ' times')
