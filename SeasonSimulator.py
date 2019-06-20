import Constants
from scipy import stats
import random


def simulate_season(teams, schedule):
    for game in schedule:
        home_team_name = game.get('home_team')
        away_team_name = game.get('visiting_team')
        #print(home_team_name)
        #print(away_team_name)
        home_team = teams.get(home_team_name)
        away_team = teams.get(away_team_name)
        is_neutral_site = game.get('neutral_site')
        simulate_game(home_team, away_team, is_neutral_site)
        teams.update({home_team_name: home_team})
        teams.update({away_team_name: away_team})


def simulate_game(home_team, away_team, is_neutral_site):
    #print(home_team)
    #print(away_team)
    home_field_advantage = 0 if is_neutral_site else Constants.HOME_FIELD_ADVANTAGE
    home_team_odds = stats.norm.cdf(
        (float(home_team.get('overall_rating')) - float(away_team.get('overall_rating')) + home_field_advantage) / 12.756862429816136)
    average_team_odds = 1 - stats.norm.cdf((home_field_advantage - float(away_team.get('overall_rating'))) / 12.756862429816136)
    odds = random.random()
    #print(odds)
    #print(home_team_odds)
    if home_team_odds > odds:  #Home team wins in simulation
        #print('home team won')
        home_team.update({'wins': home_team.get('wins') + 1})
        away_team.update({'losses': away_team.get('losses') + 1})
        home_team.update({"SOR": home_team.get('SOR') * average_team_odds})
        away_team.update({"SOR": away_team.get('SOR') / (1 - average_team_odds)})
    else:  #Home Team loses
        #print('home team lost')
        home_team.update({'losses': home_team.get('losses') + 1})
        away_team.update({'wins': away_team.get('wins') + 1})
        home_team.update({"SOR": home_team.get('SOR') / average_team_odds})
        away_team.update({"SOR": away_team.get('SOR') * (1 - average_team_odds)})
