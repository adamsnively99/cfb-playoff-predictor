from flask import Flask
from flask import render_template
from .runner import project_playoff

app = Flask(__name__)

@app.route('/')
def index():
    count = 100
    teams = project_playoff(count)
    return render_template('index.html', teams=teams, sim_count=count)
