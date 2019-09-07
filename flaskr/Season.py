import Settings
import numpy
from scipy import stats
import Constants
from game import Game


class Season:

    def __init__(self, teams, schedule, avg_top_team, rating_stdev):
        self.schedule = schedule
        self.teams = teams
        self.avg_top_team = avg_top_team
        self.rating_stdev = rating_stdev

    def simulate_season(self):
        for game in self.schedule:
            home_team_name = game.home_team_name
            away_team_name = game.away_team_name
            home_team = self.teams.get(home_team_name)
            away_team = self.teams.get(away_team_name)
            is_neutral_site = game.is_neutral_site
            self.__simulate_game(home_team, away_team, is_neutral_site, self.rating_stdev, self.avg_top_team, game)
            self.teams.update({home_team_name: home_team})
            self.teams.update({away_team_name: away_team})
        self.__simulate_conference_champs(self.rating_stdev, self.avg_top_team)

    def __simulate_game(self, home_team, away_team, is_neutral_site, rating_stdev, avg_top_team, game):
        home_field_advantage = 0 if is_neutral_site else Constants.HOME_FIELD_ADVANTAGE
        home_team_odds = stats.norm.cdf(
            (float(home_team.rating)
            - float(away_team.rating) + home_field_advantage) / rating_stdev)

        top_team_odds_home = stats.norm.cdf(
            (avg_top_team - float(away_team.rating) + home_field_advantage) / rating_stdev)

        top_team_odds_away = stats.norm.cdf(
            (avg_top_team - float(home_team.rating) - home_field_advantage) / rating_stdev)
        if home_team.name == game.simulate_winner(home_team_odds):  # Home team wins in simulation
            self.__update_after_game(home_team, away_team, top_team_odds_home, top_team_odds_away)
            return home_team
        else:  # Home Team loses
            self.__update_after_game(away_team, home_team, top_team_odds_away, top_team_odds_home)
            return away_team

    def __update_after_game(self, winning_team, losing_team, top_team_odds_winner, top_team_odds_loser):
        winning_team.update_record(losing_team, top_team_odds_winner, True)
        losing_team.update_record(winning_team, top_team_odds_loser, False)

    def __simulate_conference_champs(self, rating_stdev, avg_top_team):
        for conference in Constants.CONFERENCES:
            division_a = conference
            division_b = Constants.CONFERENCES.get(division_a)
            team_a_name = self.__get_best_conference_record(division_a, '')
            team_b_name = self.__get_best_conference_record(division_b, team_a_name)
            team_a = self.teams.get(team_a_name)
            team_b = self.teams.get(team_b_name)
            champion = self.__simulate_game(team_a, team_b, True, rating_stdev, avg_top_team,
                                     Game(team_a.name, team_b.name, True))
            champion.conf_titles += 1
            self.teams.update({champion.name: champion})
            self.teams.update({team_b_name: team_b})

    def __get_best_conference_record(self, division, exclusion_team):
        wins = -1
        for team_name in division:
            team = self.teams.get(team_name)
            team_wins = team.conf_wins
            if team_name != exclusion_team:
                if team_wins > wins:
                    wins = team_wins
                    best_team = team_name
                elif team_wins == wins:
                    if team_name not in self.teams.get(best_team).wins_over:
                        best_team = team_name
        return best_team