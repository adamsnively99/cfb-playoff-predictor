import Constants
import Settings
from scipy import stats
import random
import numpy
from team import Team

# TODO: Refactor dictionary into object for team
def calc_avg_top_team(teams):
    ratings = []
    for team_name in teams:
        if team_name != Settings.fcs:
            ratings.append(teams.get(team_name).rating)
    ratings.sort()
    return (ratings[len(teams) - 2] + ratings[len(teams) - 3] + 
            ratings[len(teams) - 4] + ratings[len(teams) - 5] + 
            ratings[len(teams) - 6]) / 5


# Calculates standard deviation of team ratings
def calc_stdev_ratings(teams):
    ratings = []
    for team_name in teams:
        if team_name != Settings.fcs:
            ratings.append(teams.get(team_name).rating)
    return numpy.std(ratings)


# TODO: Add option to simulate season with one or more games predetermined
# Simulates all games in a season, updates records, conference standings accord
#ingly
def simulate_season(teams, schedule):
    rating_stdev = calc_stdev_ratings(teams)
    avg_top_team = calc_avg_top_team(teams)
    for game in schedule:
        home_team_name = game.get('home_team')
        away_team_name = game.get('visiting_team')
        home_team = teams.get(home_team_name)
        away_team = teams.get(away_team_name)
        is_neutral_site = game.get('neutral_site')
        simulate_game(home_team, away_team, is_neutral_site, rating_stdev, avg_top_team)
        teams.update({home_team_name: home_team})
        teams.update({away_team_name: away_team})
    simulate_conference_champs(teams, rating_stdev, avg_top_team)


# Simulates a game between home_team and away_team and updates records accordingly
def simulate_game(home_team, away_team, is_neutral_site, rating_stdev, avg_top_team):
    home_field_advantage = 0 if is_neutral_site else Constants.HOME_FIELD_ADVANTAGE

    home_team_odds = stats.norm.cdf(
        (float(home_team.rating)
         - float(away_team.rating) + home_field_advantage) / rating_stdev)

    top_team_odds_home = stats.norm.cdf(
        (avg_top_team - float(away_team.rating) + home_field_advantage) / rating_stdev)

    top_team_odds_away = stats.norm.cdf(
        (avg_top_team - float(home_team.rating) - home_field_advantage) / rating_stdev)
    odds = random.random()
    if home_team_odds > odds:  # Home team wins in simulation
        update_after_game(home_team, away_team, top_team_odds_home, top_team_odds_away)
    else:  # Home Team loses
        update_after_game(away_team, home_team, top_team_odds_away, top_team_odds_home)


# Projects conference championship game according to conference standings, updates records accordingly
def simulate_conference_champs(teams, rating_stdev, avg_top_team):
    for conference in Constants.CONFERENCES:
        division_a = conference
        division_b = Constants.CONFERENCES.get(division_a)
        team_a_name = get_best_conference_record(teams, division_a, '')
        team_b_name = get_best_conference_record(teams, division_b, team_a_name)
        team_a = teams.get(team_a_name)
        team_b = teams.get(team_b_name)
        simulate_game(team_a, team_b, True, rating_stdev, avg_top_team)
        teams.update({team_a_name: team_a})
        teams.update({team_b_name: team_b})


# Updates team stats after a simulated game
def update_after_game(winning_team, losing_team, top_team_odds_winner, top_team_odds_loser):
    winning_team.update_record(losing_team, top_team_odds_winner, True)
    losing_team.update_record(winning_team, top_team_odds_loser, False)


# Returns name of team with best conference record up through head-to-head tiebreakers
def get_best_conference_record(teams, division, exclusion_team):
    wins = -1
    best_team = ''
    for team_name in division:
        team = teams.get(team_name)
        team_wins = team.conf_wins
        if team_name != exclusion_team:
            if team_wins > wins:
                wins = team_wins
                best_team = team_name
            elif team_wins == wins:
                if team_name not in teams.get(best_team).wins_over:
                    best_team = team_name
    return best_team


