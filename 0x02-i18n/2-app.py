#!/usr/bin/env python3
"""2-app"""

from flask import Flask, render_template
from flask_babel import Babel
from flask import request


class Config(object):
    """babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def hello_world():
    """initialize"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    """get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
