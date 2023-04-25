#!/usr/bin/env python3
"""0-app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """initialize"""
    return render_template('index.html')
