import ProjectionsLoader
import ScheduleLoader
import PlayoffPredictor
from Season import Season
import numpy
import Settings
import heapq


def calc_rating_standard_dev(teams):
    ratings = []
    for team_name in teams:
        if team_name != Settings.fcs:
            ratings.append(teams.get(team_name).rating)
    return numpy.std(ratings)


def calc_average_top_team(teams):
    ratings = []
    for team_name in teams:
        if team_name != Settings.fcs:
            ratings.append(teams.get(team_name).rating)
    ratings.sort()
    return (ratings[len(teams) - 2] + ratings[len(teams) - 3] +
            ratings[len(teams) - 4] + ratings[len(teams) - 5]) / 4

def reset_teams(teams):
    for team_name in teams:
        teams.get(team_name).reset()


class Simulation:
    def __init__(self, year, run_count):
        self.year = year
        self.run_count = run_count
        self.playoff_berths = {}

    def run(self):
        teams = ProjectionsLoader.load_projections()
        schedule = ScheduleLoader.load_schedule(teams)
        rating_stdev = calc_rating_standard_dev(teams)
        avg_top_team = calc_average_top_team(teams)
        for i in range(self.run_count):
            print(i)
            season = Season(teams, schedule, avg_top_team, rating_stdev)
            season.simulate_season()
            best_records = PlayoffPredictor.get_best_records(teams, 4)
            for team in best_records:
                teams.get(team).playoff_berths += 1
            best_records.sort()
            field = str(best_records)
            if field not in self.playoff_berths:
                self.playoff_berths.update({field: 1})
            else:
                self.playoff_berths.update({field: self.playoff_berths.get(field) + 1})
            reset_teams(teams)
        return {'teams': teams, 'playoff_counts': self.__get_most_likely_playoff_fields()}

    def __get_most_likely_playoff_fields(self):
        fields = []
        for field in self.playoff_berths:
            count = self.playoff_berths[field]
            fields.append((count, field))
        heapq.heapify(fields)
        return heapq.nlargest(100, fields)

        