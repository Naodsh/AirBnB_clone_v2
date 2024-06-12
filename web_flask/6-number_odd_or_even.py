#!/usr/bin/python3
"""
simple Flask web application that displays various messages and templates.
"""


from flask import Flask, render_template

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
    Route handler that returns 'C ' followed by the value of the text variable
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

    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route handler that returns an HTML page with the number n in an H1 tag.
    Only if n is an integer.
    """

    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route handler that returns an HTML page indicating if the number
    n is even or odd. Only if n is an integer.
    """

    return render_template(
            '6-number_odd_or_even.html',
            number=n,
            parity="even" if n % 2 == 0 else "odd"
            )

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
