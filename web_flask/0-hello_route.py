#!/usr/bin/python3
""" Create a Flask web application """
from flask import Flask

app = Flask(__name__)
"""
Define a route for the root URL ('/')
and disable strict slashes """


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Return the desired message """
    return "Hello HBNB!"


if __name__ == "__main__":
    """ Start the Flask development server on 0.0.0.0:5000 """
    app.run(host='0.0.0.0', port=5000)
