#!/usr/bin/python3
""" Create a Flask web application """
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
"""
Define a route for the root URL ('/')
and disable strict slashes """


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ Return main HBnB filters HTML page """
    path = '10-hbnb_filters.html'
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(path, states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """ Remove current SQAlchemy session """
    storage.close()


if __name__ == "__main__":
    """ Start the Flask development server on 0.0.0.0:5000 """
    app.run(host='0.0.0.0', port=5000)
