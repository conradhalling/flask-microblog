from flask import Flask

app = Flask(__name__)

# Import routes here to avoid circular imports.
from microblog import routes
