from flask import Blueprint

encuesta_bp = Blueprint('encuesta_bp', __name__)

@encuesta_bp.route('/')
def index():
    return '<h1>encuestas<h1/>'