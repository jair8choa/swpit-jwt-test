import json
import extensions.auth_jwt as auth_jwt
from flask import Blueprint, Flask, request, make_response,jsonify, current_app
from extensions.validation import token_required, token_generator,password_validation
from sqlalchemy.ext.automap import automap_base
from extensions.extensions import db
from models.Usuario import Usuario
from json import dumps

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/')
def index():
    return '<h1>auth<h1/>'

@auth_bp.post('/login')
def login():

    auth = request.form
    username = auth.get('username')
    password = auth.get('password')

    if not username:
        response_object = {"messages": 'username is missing'}
        return make_response(jsonify(response_object))

    token = password_validation(username, password)
    return make_response(jsonify(token))

@auth_bp.route('/check')
@token_required
def check(user):
    return make_response(jsonify({'user_id': user.idusuario}))

@auth_bp.post('/create')
@token_required
def create():
    data = json.loads(request.data)
    nuevoUsuario = Usuario()
    # nuevoUsuario.idusuario = data["idusuario"]
    nuevoUsuario.nombre = data["Nombre"]
    nuevoUsuario.correo = data["Correo"]
    nuevoUsuario.clave = data["Clave"]
    # nuevoUsuario.activo = data["Activo"]
    db.session.add(nuevoUsuario)
    db.session.commit()
    return make_response(jsonify({'res': 'user created'}))