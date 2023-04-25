#!/usr/bin/env python3
"""1-app"""
from flask_babel import Babel
from flask import Flask, render_template
from flask import request


class Config(object):
    """babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAUlLT_LOCALE = "en"
    BABEL_DEFAUlLT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/")
def hello_world():
    """initialize"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()