import Constants
from scipy import stats
import random
import numpy

def calc_stdev_ratings(teams):
    ratings = []
    for team in teams:
        if team != 'FCS':
            ratings.append(teams.get(team).get('overall_rating'))
    return numpy.std(ratings)

def simulate_season(teams, schedule):
    rating_stdev = calc_stdev_ratings(teams)
    for game in schedule:
        home_team_name = game.get('home_team')
        away_team_name = game.get('visiting_team')
        home_team = teams.get(home_team_name)
        away_team = teams.get(away_team_name)
        is_neutral_site = game.get('neutral_site')
        simulate_game(home_team, away_team, is_neutral_site, rating_stdev)
        teams.update({home_team_name: home_team})
        teams.update({away_team_name: away_team})
    simulate_conference_champs(teams)


def simulate_game(home_team, away_team, is_neutral_site, rating_stdev):
    home_field_advantage = 0 if is_neutral_site else Constants.HOME_FIELD_ADVANTAGE
    home_team_odds = stats.norm.cdf(
        (float(home_team.get('overall_rating')) - float(away_team.get('overall_rating')) + home_field_advantage) / rating_stdev)
    average_team_odds = 1 - stats.norm.cdf((home_field_advantage - float(away_team.get('overall_rating'))) / rating_stdev)
    odds = random.random()
    if home_team_odds > odds:  #Home team wins in simulation
        #print('home team won')
        update_after_game(home_team, away_team, average_team_odds)
    else:  #Home Team loses
        update_after_game(away_team, home_team, 1 - average_team_odds)


def simulate_conference_champs(teams):
    for conference in Constants.CONFERENCES:
        division_a = conference
        division_b = Constants.CONFERENCES.get(division_a)
        team_a_name = get_best_record(teams, division_a, '')
        team_a = teams.get(team_a_name)
        team_b = teams.get(get_best_record(teams, division_b, team_a_name))
        simulate_game(team_a, team_b, True)

def update_after_game(winning_team, losing_team, average_team_odds):
    winning_team.get('wins-over').append(losing_team.get('name'))
    losing_team.get('losses-to').append(winning_team.get('name'))
    winning_team.update({'wins': winning_team.get('wins') + 1})
    losing_team.update({'losses': losing_team.get('losses') + 1})

    winning_team.update({"SOR": winning_team.get('SOR') * average_team_odds})
    losing_team.update({"SOR": losing_team.get('SOR') / (1 - average_team_odds) +
                               losing_team.get('SOR') / (1 - average_team_odds)})
    if winning_team.get('conf') == losing_team.get('conf'):
        winning_team.update({'conf wins': winning_team.get('conf wins') + 1})
        losing_team.update({'conf losses': losing_team.get('conf losses') + 1})


def get_best_record(teams, division, exclusion_team):
    wins = -1
    best_team = ''
    for team_name in division:
        team = teams.get(team_name)
        team_wins = team.get('conf wins')
        if team_name != exclusion_team:
            if team_wins > wins:
                wins = team_wins
                best_team = team_name
            elif team_wins == wins:
                if team_name not in teams.get(best_team).get('wins-over'):
                    best_team = team_name
    return best_team