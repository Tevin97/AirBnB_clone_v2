#!/usr/bin/python3
""" starts a Flask web application  """

from flask import Flask, render_template


app = Flask("__name__")


# Defile the route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello():
    """ Returns "Hello HBNB" """
    return render_template("10-hbnb_filters.html")


if __name__ == "__main__":
    # Start the Flask server, listen on 0.0.0.0 (all networks) and port 5000
    app.run(host="0.0.0.0", port=5000)
