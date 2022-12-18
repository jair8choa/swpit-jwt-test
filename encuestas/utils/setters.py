from extensions.extensions import db
from flask import Blueprint, render_template, request, redirect, make_response,jsonify
from models.ResultadosHE import ResultadosHE
from models.ResultadosTA import ResultadosTA
from models.ResultadosCA import ResultadosCA

def set_ResultadosHE(respuestas, id_user):
    nuevoresultado = ResultadosHE()
    calificacion1 = sum([int(string) for string in respuestas[0]])
    calificacion2 = sum([int(string) for string in respuestas[1]])
    calificacion3 = sum([int(string) for string in respuestas[2]])
    nuevoresultado.idUsuario = id_user
    nuevoresultado.calificacionseccion1 = calificacion1
    nuevoresultado.calificacionseccion2 = calificacion2
    nuevoresultado.calificacionseccion3 = calificacion3
    nuevoresultado.calificacionfinal = calificacion3+calificacion2+calificacion1
    nuevoresultado.resultadoseccion1 = ''
    nuevoresultado.resultadoseccion2 = ''
    nuevoresultado.resultadoseccion3 = ''
    nuevoresultado.resultadofinal = ''

    resultado = ResultadosHE.query.filter_by(idUsuario=id_user).first()
    if resultado:
        nuevoresultado.idResultadoHE = resultado.idResultadoHE
        db.session.merge(nuevoresultado)
        db.session.commit()
        return make_response(jsonify({'res': 'resultadoshe modifed'}))
    else:
        db.session.add(nuevoresultado)
        db.session.commit()
        return make_response(jsonify({'res': 'resultadoshe created'}))

def set_ResultadosTA(respuestas, id_user):
    nuevoresultado = ResultadosTA()
    nuevoresultado.idUsuario = id_user
    nuevoresultado.cantidad1 = len([int(i) for i in respuestas[0] if int(i) == 1 ])
    nuevoresultado.cantidad2 = len([int(i) for i in respuestas[0] if int(i) == 2 ])
    nuevoresultado.cantidad3 = len([int(i) for i in respuestas[0] if int(i) == 3 ])
    nuevoresultado.cantidad4 = len([int(i) for i in respuestas[0] if int(i) == 4 ])
    nuevoresultado.resultado = ""

    resultado = ResultadosTA.query.filter_by(idUsuario=id_user).first()
    if resultado:
        nuevoresultado.idResultadosTA = resultado.idResultadosTA
        db.session.merge(nuevoresultado)
        db.session.commit()
        return make_response(jsonify({'res': 'resultadoshe modifed'}))
    else:
        db.session.add(nuevoresultado)
        db.session.commit()
        return make_response(jsonify({'res': 'resultadoshe created'}))

def set_ResultadosCA(respuestas, id_user):
    nuevoresultado = ResultadosCA()
    nuevoresultado.idUsuario = id_user
    nuevoresultado.visual = 0
    nuevoresultado.auditivo = 0
    nuevoresultado.kinestesico = 0

    resultado = ResultadosCA.query.filter_by(idUsuario=id_user).first()
    if resultado:
        nuevoresultado.idResultadoCA = resultado.idResultadoCA
        db.session.merge(nuevoresultado)
        db.session.commit()
        return make_response(jsonify({'res': 'resultadoshe modifed'}))
    else:
        db.session.add(nuevoresultado)
        db.session.commit()
        return make_response(jsonify({'res': 'resultadoshe created'}))