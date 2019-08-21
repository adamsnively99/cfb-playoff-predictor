README

This project seeks to use S&P+ college football projections of team strength to 
project the most likely postseason matchups for a given season. This is achieved
by performing a Monte Carlo experiment by simulating a given season 1,000+ 
times.

This project allows users to display the program results in a Flask webapp, 
still in progress.

<h4>To Run</h4>

Clone this project with the command: 
<code> git clone https://github.com/adamsnively99/cfb-playoff-predictor.git </code>

Then, navigate to the <code>cfb-playoff-predictor/flaskr</code> directory
 of this project and install the necessary dependencies with <code>pip 
 install -r requirements.txt</code>
 
 Run the project through the command line with <code>python runner.py</code>
 
 Run the project through the webapp by setting the <code>FLASK_APP</code> environment variable with <code>export FLASK_APP=index.py</code>, 
 running the webapp with <code>flask run</code>, and viewing the results by visiting <code>http://127.0.0.1:5000/</code>.