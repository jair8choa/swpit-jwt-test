import json
from flask import Blueprint
from models.Encuestas import Encuestas
from models.Seccion import Seccion
from models.Preguntas import Preguntas
from models.Tipos import Tipos
encuesta_bp = Blueprint('encuesta_bp', __name__)

@encuesta_bp.route('/')
def index():
    return '<h1>encuestas<h1/>'

@encuesta_bp.route('/<id>')
def get_encuestas(id):
    res = {}
    encuesta = Encuestas.query.filter_by(idEncuesta=id).first()
    res["titulo"] = encuesta.Nombre
    res["descripcion"] = encuesta.Descripcion
    secciones = Seccion.query.filter_by(idEncuesta=id).all()
    res["secciones"] = []
    for seccion in secciones:
        res_seccion = {}
        res_seccion["titulo"] = seccion.Titulo
        res_seccion["instrucciones"] = seccion.Instrucciones
        preguntas = Preguntas.query.filter_by(idSeccion=seccion.idSeccion).all()
        res_seccion["preguntas"] = []
        for pregunta in preguntas:
            res_preguntas = {}
            res_preguntas["numero"] = pregunta.NumeroPregunta
            res_preguntas["titulo"] = pregunta.TituloPregunta
            res_seccion["preguntas"].append(res_preguntas)
        res["secciones"].append(res_seccion)
    res_json = json.dumps(res, indent=4)
    return res_json