#!/usr/bin/env python3
"""
Topic: 0x02-i18n
Name: Khotso Selading
Date: 06-02-2024
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Configuration settings for Flask Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Selects the best language match for a web page."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page."""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
