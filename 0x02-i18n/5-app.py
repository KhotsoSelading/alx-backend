#!/usr/bin/env python3
"""
Topic: 0x02-i18n
Name: Khotso Selading
Date: 06-02-2024
"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    Retrieves user information based on the 'login_as' URL parameter.

    Returns:
        dict or None: User dictionary if ID value is found in users dictionary
        and 'login_as' URL parameter is provided, otherwise None.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """
    Retrieves user information based on the 'login_as' URL parameter.

    Returns:
        dict or None: User dictionary if ID value is found in users dictionary
        and 'login_as' URL parameter is provided, otherwise None.
    """
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    Adds user information to flask.g if user is found.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Selects and returns the best language match based on supported languages.
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
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
