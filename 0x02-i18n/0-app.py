#!/usr/bin/env python3
"""
Topic: 0x02-i18n
Name: Khotso Selading
Date: 30-01-2024
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Route function for the root endpoint.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
