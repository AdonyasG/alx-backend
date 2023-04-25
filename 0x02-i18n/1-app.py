#!/usr/bin/env python3
"""1-app"""
from flask_babel import Babel
from flask import Flask, render_template
from flask import request

app = Flask(__name__)
babel = Babel(app)



class Config(object):
    """babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAUlLT_LOCALE = "en"
    BABEL_DEFAUlLT_TIMEZONE = "UTC"

    @babel.localeselector
    def get_locale():
        """get locale"""
        return request.accept_languages.best_match(app.config['LANGUAGES'])

app.config.from_object(Config)
@app.route("/")
def hello_world():
    """initialize"""
    return render_template('1-index.html')
