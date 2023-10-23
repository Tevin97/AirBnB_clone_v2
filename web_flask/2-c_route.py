#!/usr/bin/python3
""" starts a Flask web application  """

from flask import Flask


app = Flask(__name__)

# Defile the route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello_world():
    """ Returns "Hello HBNB" """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns "HBNB" """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Returns “C ” followed by the value of the text variable """
    # replace underscore _ symbols with a space
    my_text = text.replace('_',' ')
    return "C {}".format(my_text)

if __name__ == '__main__':
    #Start the Flask server, listen on 0.0.0.0 (all networks) and port 5000
    app.run(host='0.0.0.0', port=5000)
