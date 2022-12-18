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
            return make_response(jsonify({'message': 'token is missing'}), 401)
        try:
            data = get_payload(token, current_app.config.get('SECRET_KEY'))
            current_user = Usuario.query.filter_by(idusuario=data['sub']).first()
        except Exception as e:
            return make_response(jsonify({'message': 'token is invalid'}), 401)
        return f(current_user, *args, **kwargs)
    return decorator

def password_validation(username, password):
    try:
        token = None
        usuario = Usuario.query.filter_by(Nombre=username).first()
        if usuario == None:
            response_object = {"messages": 'user is invalid'}
            return make_response(jsonify(response_object), 401)
        if(bcrypt.checkpw(password.encode('utf-8'), usuario.Clave.encode('utf-8'))):
            token = token_generator(user_id=usuario.idusuario, private_key= current_app.config.get('SECRET_KEY'))
            return {"token": "bearer "+token, "user_id": usuario.idusuario}
        else:
            response_object = {"messages": 'password is invalid'}
            return make_response(jsonify(response_object), 401)
    except Exception as e:
        return str(e)