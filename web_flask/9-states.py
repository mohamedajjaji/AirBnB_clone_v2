#!/usr/bin/python3
""" Create a Flask web application """
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
"""
Define a route for the root URL ('/')
and disable strict slashes """


@app.route("/states", strict_slashes=False)
def states_list():
    """
    Return HTML page with list of states and relevant cities
    States/cities sorted by name """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ Return HTML page with infor on <id> if it exists """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """ Remove current SQAlchemy session """
    storage.close()


if __name__ == "__main__":
    """ Start the Flask development server on 0.0.0.0:5000 """
    app.run(host='0.0.0.0', port=5000)
