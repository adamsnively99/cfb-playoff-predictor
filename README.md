README

This project seeks to use S&P+ college football projections of team 
strength to project the most likely postseason matchups for a given 
season. This is achieved by performing a Monte Carlo experiment by 
simulating a given season 1,000+ times.

This project allows users to display the program results in a Flask 
webapp, still in progress.

<h4>How It Works</h4>

This project uses Bill Connelly's S&P+ college football projections to 
make its projections. You can read more about S&P+ 
<a href="https://www.sbnation.com/college-football/2017/10/13/16457830/college-football-advanced-stats-analytics-rankings">here</a>,
but what you need to know is that it is a metric of overall team 
strength that is calculated from a teams' efficiency on offense, 
defense, and special teams, and adjusts for strength of schedule. 

This metric presents itself in a number that represents how much better 
or worse a team is than average. For example, in 2018, Texas A&M 
finished with a rating of 21.4, meaning they were 21.4 points per game 
better than the average FBS team. San Jose State, however, finished with
a rating of -17.1, meaning they were 17.1 points per game worse than 
average.

These ratings can be used to assign win probabilities to games. For any 
game between two teams A and B, I took the difference of the ratings of 
A and B. If A and B were not playing at a neutral site, I added 2.5 to 
the rating of the home team to account for home field advantage. Then, 
I divided by the standard deviation of all of the ratings of teams, and 
treated this value as a z-score for a normal distribution, and treated 
the cumulative percentile for that z-score as the probability that Team 
A would win.

This project then simulates each season using these win probabilities. 
For each season, it projects which teams would make the college football
playoff by calculating a strength of record metric for each team.

<h4>To Run</h4>

Clone this project with the command: 
<code> git clone https://github.com/adamsnively99/cfb-playoff-predictor.git </code>

Then, navigate to the <code>cfb-playoff-predictor/flaskr</code> directory
 of this project and install the necessary dependencies with <code>pip 
 install -r requirements.txt</code>
  
 Run the project through the webapp by setting the <code>FLASK_APP</code> environment variable with <code>export FLASK_APP=index.py</code>, 
 running the webapp with <code>flask run</code>, and viewing the results by visiting <code>http://127.0.0.1:5000/</code>.
 