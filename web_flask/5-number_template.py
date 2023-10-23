#!/usr/bin/python3
""" starts a Flask web application  """

from flask import Flask, request, render_template


app = Flask(__name__)


# Define the route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello_world():
    """ Returns "Hello HBNB" """
    return 'Hello HBNB!'


# Define the route for URL '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns "HBNB" """
    return "HBNB"


# Define the route for URL '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Returns “C ” followed by the value of the text variable """
    # replace underscore _ symbols with a space
    my_text = text.replace('_', ' ')
    return "C {}".format(my_text)


# Define the route for URL /python/<text>
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_py_text(text):
    """ Returns “C ” followed by the value of the text variable """
    # replace underscore _ symbols with a space
    my_text = text.replace('_', ' ')
    return "Python {}".format(my_text)


# Define the route for URL /number/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """Display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


# Define the route for URL /number_template/<n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """Display “n is a number” only if n is an integer"""
    # Render the template and pass the value of n to the template
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    # Start the Flask server, listen on 0.0.0.0 (all networks) and port 5000
    app.run(host='0.0.0.0', port=5000)
