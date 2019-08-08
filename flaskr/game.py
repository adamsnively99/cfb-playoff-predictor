import random


class Game:
    def __init__(self, home_team, away_team, is_neutral_site):
        self.home_team_name = home_team
        self.away_team_name = away_team
        self.is_neutral_site = is_neutral_site
        self.winning_team_name = 'Game Not Played'
        self.losing_team_name = 'Game Not Played'

    def set_outcome(self, winning_team, losing_team):
        print('setting outcome: ' + winning_team + ', ' + losing_team)
        self.winning_team_name = winning_team
        self.losing_team_name = losing_team

    def simulate_winner(self, home_team_odds):
        if self.winning_team_name != 'Game Not Played':
            return self.winning_team_name

        return self.home_team_name if home_team_odds > random.random() else self.away_team_name

    def print_game(self):
        print('Home Team: ' + self.home_team_name)
        print('Away Team: ' + self.away_team_name)
        print('Is Neutral Site: ' + str(self.is_neutral_site))
        print('Winning Team: ' + self.winning_team_name)
        print('Losing Team: ' + self.losing_team_name)