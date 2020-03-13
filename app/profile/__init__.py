from flask import Blueprint

bp_prof: Blueprint = Blueprint('prof', __name__)

from app.profile import routes
