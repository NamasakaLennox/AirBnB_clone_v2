#!/usr/bin/python3
"""
Starts a flask web application for the airbnb template
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    displays the states in the database
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)

    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
