import json
from flask import Blueprint, render_template, request, redirect
from models.Encuestas import Encuestas
from models.Seccion import Seccion
from models.Preguntas import Preguntas
from models.Tipos import Tipos

encuesta_bp = Blueprint('encuesta_bp', __name__,static_folder='static', template_folder='templates')

@encuesta_bp.route('/')
def index():
    return '<h1>encuestas<h1/>'

@encuesta_bp.post('/calificar')
def calificar():
    data = json.loads(request.data)
    suma1 = sum([int(i) for i in data["res1"]])
    suma2 = sum([int(i) for i in data["res2"]])
    suma3 = sum([int(i) for i in data["res3"]])
    sumaTotal = suma1+suma2+suma3
    res = calif(sumaTotal)
    return res

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
        res_seccion["id"] = seccion.idSeccion
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
    return render_template('Cuestionario.html', res=res)

def calif(total):
    if total >= 57:
        return "Muy alto"
    elif 52 <= total <= 56:
        return "Alto"
    elif 50 <= total <= 51:
        return "Por encima del promedio"
    elif 48 <= total <= 49:
        return "Promedio alto"
    elif 43 <= total <= 47:
        return "Promedio"
    elif 39 <= total <= 42:
        return "Promedio bajo"
    elif 37 <= total <= 38:
        return "Por debajo del promedio"
    elif 34 <= total <= 36:
        return "Bajo"
    elif 0 <= total <= 33:
        return "Muy bajo"
