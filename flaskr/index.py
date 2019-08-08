from flask import Flask
from flask import render_template
from .runner import project_playoff

app = Flask(__name__)

# TODO: Create HTML template to display results
@app.route('/')
def index():
    teams = project_playoff()
    return render_template('index.html', teams=teams)
