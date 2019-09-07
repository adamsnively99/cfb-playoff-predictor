from flask import Flask
from flask import render_template
from .runner import project_playoff
import Settings
app = Flask(__name__)

#TODO: Improve UI, let users pick results of games
@app.route('/')
def index():
    count = Settings.simulation_count
    simuulation = project_playoff(count)
    teams = simuulation['teams']
    playoff_fields = simuulation['playoff_counts']
    return render_template('index.html', teams=teams, playoff_fields=playoff_fields, sim_count=count)
