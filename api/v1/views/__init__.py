# api/v1/views/__init__.py

from flask import Blueprint

# Create a Blueprint instance with a URL prefix of /api/v1
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import everything from the package api.v1.views.index
from api.v1.views.index import *
