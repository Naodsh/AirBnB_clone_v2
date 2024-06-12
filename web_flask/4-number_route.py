#!/usr/bin/python3
"""
simple Flask web application that displays 'Hello HBNB!', 'HBNB', 'C <text>',
'Python <text>', and '<n> is a number' at respective routes.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler that returns the string 'Hello HBNB!'
    """

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler that returns the string 'HBNB'
    """

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route handler returns 'C ' followed by the value of the text variable.
    Replaces underscores in the text with spaces.
    """

    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route handler returns 'Python ' followed by the value of the text variable
    Replaces underscores in the text with spaces. Default text is 'is cool'.
    """

    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route handler that returns '<n> is a number' only if n is an integer.
    """

    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
