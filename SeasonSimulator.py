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
    simulate_conference_champs(teams)


def simulate_game(home_team, away_team, is_neutral_site):
    home_field_advantage = 0 if is_neutral_site else Constants.HOME_FIELD_ADVANTAGE
    home_team_odds = stats.norm.cdf(
        (float(home_team.get('overall_rating')) - float(away_team.get('overall_rating')) + home_field_advantage) / 12.756862429816136)
    average_team_odds = 1 - stats.norm.cdf((home_field_advantage - float(away_team.get('overall_rating'))) / 12.756862429816136)
    odds = random.random()
    if home_team_odds > odds:  #Home team wins in simulation
        #print('home team won')
        home_team.get('wins-over').append(away_team.get('name'))
        away_team.get('losses-to').append(home_team.get('name'))
        home_team.update({'wins': home_team.get('wins') + 1})
        away_team.update({'losses': away_team.get('losses') + 1})
        home_team.update({"SOR": home_team.get('SOR') * average_team_odds})
        away_team.update({"SOR": away_team.get('SOR') / (1 - average_team_odds)})
        if home_team.get('conf') == away_team.get('conf'):
            home_team.update({'conf wins': home_team.get('conf wins') + 1})
            away_team.update({'conf losses': away_team.get('conf losses') + 1})
    else:  #Home Team loses
        home_team.get('losses-to').append(away_team.get('name'))
        away_team.get('wins-over').append(home_team.get('name'))
        home_team.update({'losses': home_team.get('losses') + 1})
        away_team.update({'wins': away_team.get('wins') + 1})
        home_team.update({"SOR": home_team.get('SOR') / average_team_odds})
        away_team.update({"SOR": away_team.get('SOR') * (1 - average_team_odds)})
        if home_team.get('conf') == away_team.get('conf'):
            home_team.update({'conf losses': home_team.get('conf losses') + 1})
            away_team.update({'conf wins': away_team.get('conf wins') + 1})


def simulate_conference_champs(teams):
    for conference in Constants.CONFERENCES:
        division_a = conference
        division_b = Constants.CONFERENCES.get(division_a)
        team_a_name = get_best_record(teams, division_a, '')
        team_a = teams.get(team_a_name)
        team_b = teams.get(get_best_record(teams, division_b, team_a_name))
        simulate_game(team_a, team_b, True)


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