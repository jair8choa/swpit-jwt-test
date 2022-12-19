from extensions.extensions import db
from flask import Blueprint, render_template, request, redirect, make_response,jsonify
from models.ResultadosHE import ResultadosHE
from models.ResultadosTA import ResultadosTA
from models.ResultadosCA import ResultadosCA

def get_ResultadosHE(id):
    resultado = ResultadosHE.query.filter_by(idUsuario=id).first()
    if resultado:
        res = {}
        res["idResultadoHE"] = resultado.idResultadoHE
        res["idUsuario"] = resultado.idUsuario
        res["resultadoseccion1"] = resultado.resultadoseccion1
        res["resultadoseccion2"] = resultado.resultadoseccion2
        res["resultadoseccion3"] = resultado.resultadoseccion3
        res["resultadofinal"] = resultado.resultadofinal
        res["calificacionseccion1"] = resultado.calificacionseccion1
        res["calificacionseccion2"] = resultado.calificacionseccion2
        res["calificacionseccion3"] = resultado.calificacionseccion3
        res["calificacionfinal"] = resultado.calificacionfinal
        return make_response(jsonify(res))
    else:
        return make_response(jsonify({'res': 'encuesta no existe'}), 404)

def get_ResultadosTA(id):
    resultado = ResultadosTA.query.filter_by(idUsuario=id).first()
    if resultado:
        res = {}
        res["idResultadosTA"] = resultado.idResultadosTA
        res["idUsuario"] = resultado.idUsuario
        res["cantidad1"] = resultado.cantidad1
        res["cantidad2"] = resultado.cantidad2
        res["cantidad3"] = resultado.cantidad3
        res["cantidad4"] = resultado.cantidad4
        res["resultado"] = resultado.resultado
        res["mensaje"] = resultado.mensaje
        return make_response(jsonify(res))
    else:
        return make_response(jsonify({'res': 'encuesta no existe'}), 404)

def get_ResultadosCA(id):
    resultado = ResultadosCA.query.filter_by(idUsuario=id).first()
    if resultado:
        res = {}
        res["idResultadoCA"] = resultado.idResultadoCA
        res["idUsuario"] = resultado.idUsuario
        res["visual"] = resultado.visual
        res["auditivo"] = resultado.auditivo
        res["kinestesico"] = resultado.kinestesico
        res["resultado"] = resultado.resultado
        return make_response(jsonify(res))
    else:
        return make_response(jsonify({'res': 'encuesta no existe'}), 404)