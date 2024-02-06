#!/usr/bin/env python3
"""
This script is related to the i18n topic.
Author: Khotso Selading
Date: 06-02-2024
"""
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


class Config(object):
    """
    Configuration settings for Babel.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for Babel.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Selects and returns the best language match based on supported languages.

    Returns:
        str: The selected language code.
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the index page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
