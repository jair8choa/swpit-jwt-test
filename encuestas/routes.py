import json
from flask import Blueprint, render_template, request, redirect, make_response,jsonify
from extensions.validation import token_required, token_generator,password_validation
from extensions.extensions import db
from models.Encuestas import Encuestas
from models.Seccion import Seccion
from models.Preguntas import Preguntas
from models.Tipos import Tipos
from models.ResultadosHE import ResultadosHE
from models.ResultadosTA import ResultadosTA
from .utils.setters import set_ResultadosHE, set_ResultadosTA, set_ResultadosCA
from .utils.getters import get_ResultadosHE, get_ResultadosTA, get_ResultadosCA

encuesta_bp = Blueprint('encuesta_bp', __name__,static_folder='static', template_folder='templates')

@encuesta_bp.post('/resultados')
@token_required
def resultadosta_post(current_user):
    data = json.loads(request.data)
    if(data['id_encuesta'] == 1): return set_ResultadosHE(data['respuestas'], current_user.idusuario)
    elif(data['id_encuesta'] == 2): return set_ResultadosTA(data['respuestas'], current_user.idusuario)
    elif(data['id_encuesta'] == 3): return set_ResultadosCA(data['respuestas'], current_user.idusuario)
    else: return make_response(jsonify({'res': 'error'}), 404)

@encuesta_bp.get('/resultados/<int:id>')
@token_required
def get_resultado(current_user, id):
    if(id == 1): return get_ResultadosHE(current_user.idusuario)
    elif(id == 2): return get_ResultadosTA(current_user.idusuario)
    elif(id == 3): return get_ResultadosCA(current_user.idusuario)
    else: return make_response(jsonify({'res': 'error'}), 404)

@encuesta_bp.route('/<id>')
def get_encuesta(id):
    res = {}
    encuesta = Encuestas.query.filter_by(idEncuesta=id).first()
    res["id"] = encuesta.idEncuesta
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
    return json.dumps(res)

@encuesta_bp.route('/')
def get_encuestas():
    res = []
    encuestas = Encuestas.query.all()
    for encuesta in encuestas:
        res_encuesta = {}
        res_encuesta["id"] = encuesta.idEncuesta
        res_encuesta["nombre"] = encuesta.Nombre
        res_encuesta["descripcion"] = encuesta.Descripcion
        res.append(res_encuesta)
    return json.dumps(res)

