#!/usr/bin/env python3
"""
This script is related to the i18n topic.
Author: Khotso Selading
Date: 06-02-2024
"""
import babel
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration settings for Flask Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Detects if the incoming request contains a 'locale' argument and if its
    value is a supported locale, returns it.
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Renders a basic 'Hello, World!' page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
