#!/usr/bin/env python3
"""1-app"""
from flask_babel import Babel
from flask import Flask, render_template


class Config(object):
    """babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object('1-app.Config')


@app.route("/")
def hello_world():
    """initialize"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
