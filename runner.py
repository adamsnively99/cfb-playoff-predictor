import ProjectionsLoader
import ScheduleLoader
import SeasonSimulator
import PlayoffPredictor
import numpy

def calc_stdev_ratings(teams):
    ratings = []
    for team in teams:
        ratings.append(teams.get(team).get('overall_rating'))
    return numpy.std(ratings)

playoff_counts = {}
for i in range(1000):
    teams = ProjectionsLoader.load_projections()
    schedule = ScheduleLoader.load_schedule(teams)
    SeasonSimulator.simulate_season(teams, schedule)
    #print('RUNNER')
    #print(teams)
    playoff = PlayoffPredictor.predict_playoff(teams)
    for team in playoff:
        print('playoff ' + str(i) + ' contains: ' + team)
        if team not in playoff_counts:
            playoff_counts.update({team : 1})
        else:
            playoff_counts.update({team : playoff_counts.get(team) + 1})

for team in playoff_counts:
    print(team + " made the playoff " + str(playoff_counts.get(team)) + ' times')