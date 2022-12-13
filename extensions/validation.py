import jwt
import bcrypt
from flask import request,make_response, jsonify, current_app
from functools import wraps
from models.Usuario import Usuario
from .auth_jwt import token_generator,get_payload

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            bearer = request.headers['Authorization']
            token = bearer.split()[1]
        else:
            return make_response(jsonify({'message': 'token is missing'}))
        try:
            data = get_payload(token, current_app.config.get('SECRET_KEY'))
            current_user = Usuario.query.filter_by(idusuario=data['sub']).first()
        except Exception as e:
            return make_response(jsonify({'message': 'token is invalid'}))
        return f(current_user, *args, **kwargs)
    return decorator

def password_validation(username, password):
    try:
        token = None
        usuario = Usuario.query.filter_by(nombre=username).first()
        if usuario == None:
            return 'user is invalid'
        if(bcrypt.checkpw(password.encode('utf-8'), usuario.clave.encode('utf-8'))):
            token = token_generator(user_id=usuario.idusuario, private_key= current_app.config.get('SECRET_KEY'))
            return token
        else:
            return 'password is invalid'
    except Exception as e:
        return str(e)