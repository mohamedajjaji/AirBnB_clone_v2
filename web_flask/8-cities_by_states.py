#!/usr/bin/python3
""" Create a Flask web application """
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
"""
Define a route for the root URL ('/')
and disable strict slashes """


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """
    Return HTML page with list of states and relevant cities
    States/cities sorted by name """
    states = storage.all("State")
    path = '8-cities_by_states.html'
    return render_template(path, states=states)


@app.teardown_appcontext
def teardown(exc):
    """ Remove current SQAlchemy session """
    storage.close()


if __name__ == "__main__":
    """ Start the Flask development server on 0.0.0.0:5000 """
    app.run(host='0.0.0.0', port=5000)
