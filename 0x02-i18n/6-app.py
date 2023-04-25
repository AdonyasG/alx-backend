#!/usr/bin/env python3
"""6-app"""

from flask import Flask, render_template, g
from flask_babel import Babel
from flask import request
from typing import Dict


class Config(object):
    """babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """get locale"""
    if request.args.get('locale'):
        if request.args.get('locale') in app.config['LANGUAGES']:
            return request.args.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Dict:
    """getuser"""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """before request"""
    usr = get_user()
    g.usr = usr


@app.route("/", strict_slashes=False)
def hello_world():
    """initialize"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
