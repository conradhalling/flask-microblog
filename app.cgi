#!/Users/halto/src/conradhalling/flask-microblog/venv313/bin/python3

"""
This CGI script runs the Flask-based microblog application.
"""

from wsgiref.handlers import CGIHandler
from microblog import app

CGIHandler().run(app)
