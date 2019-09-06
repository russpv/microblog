from flask import Blueprint

bp = Blueprint('auth', __name__)  # name of blueprint package, and name of base module

from app.auth import routes  # attach all routes to blueprint instance