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


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Return the desired message """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ Return 'C' followed by the value of <text> """
    return 'C ' + text.replace('_', ' ')


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_with_text(text='is cool'):
    """
    Return 'Python' then the value of <text>
    Replaces underscores in <text> with spaces """
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Return 'n is a number' only if 'n' is integer """
    return '{} is a number'.format(n)


if __name__ == "__main__":
    """ Start the Flask development server on 0.0.0.0:5000 """
    app.run(host='0.0.0.0', port=5000)
