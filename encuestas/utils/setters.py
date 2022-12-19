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
    nuevoresultado.resultadoseccion1 = caliseccion(nuevoresultado.calificacionseccion1)
    nuevoresultado.resultadoseccion2 = caliseccion(nuevoresultado.calificacionseccion2)
    nuevoresultado.resultadoseccion3 = caliseccion(nuevoresultado.calificacionseccion3)
    nuevoresultado.resultadofinal = califinal(nuevoresultado.calificacionfinal)

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
    if nuevoresultado.cantidad3+nuevoresultado.cantidad4 > nuevoresultado.cantidad1+nuevoresultado.cantidad2:
        nuevoresultado.resultado = "Menor acertividad"
        nuevoresultado.mensaje = "Te aconsejamos cambiar tu conducta o en algun momento podrias ver lesionados tus derechos."
    else:
        nuevoresultado.resultado = "Mayor acertividad"
        nuevoresultado.mensaje = "Te aconsejamos mantener tu conducta y evitaras que en algun momento veas lesionados tus derechos."

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
    respuestas  = [int(i) for i in respuestas[0]]
    nuevoresultado.idUsuario = id_user
    nuevoresultado.visual = respuestas[0]+respuestas[2]+respuestas[5]+respuestas[8]+respuestas[9]+respuestas[10]+respuestas[13]
    nuevoresultado.auditivo = respuestas[1]+respuestas[4]+respuestas[11]+respuestas[14]+respuestas[16]+respuestas[20]+respuestas[22]
    nuevoresultado.kinestesico = respuestas[3]+respuestas[6]+respuestas[7]+respuestas[12]+respuestas[18]+respuestas[21]+respuestas[23]
    
    if(nuevoresultado.auditivo > nuevoresultado.visual and nuevoresultado.auditivo > nuevoresultado.kinestesico): nuevoresultado.resultado = "Auditiva"
    elif(nuevoresultado.visual > nuevoresultado.auditivo and nuevoresultado.visual > nuevoresultado.kinestesico): nuevoresultado.resultado = "Visual"
    elif(nuevoresultado.kinestesico > nuevoresultado.auditivo and nuevoresultado.kinestesico > nuevoresultado.visual): nuevoresultado.resultado = "Kinestesica"
    elif(nuevoresultado.auditivo == nuevoresultado.kinestesico == nuevoresultado.visual): nuevoresultado.resultado = "Visual Auditiva Kinestesica"
    elif(nuevoresultado.visual == nuevoresultado.auditivo): nuevoresultado.resultado = "Visual Auditiva"
    elif(nuevoresultado.visual == nuevoresultado.kinestesico): nuevoresultado.resultado = "Visual Kinestisica"
    elif(nuevoresultado.auditivo == nuevoresultado.kinestesico): nuevoresultado.resultado = "Auditiva Kinestesica"

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


def caliseccion(total):
    if total >= 20:
        return "Muy alto"
    elif total >= 19:
        return "Alto"
    elif total >= 18:
        return "Por encima del promedio"
    elif total >= 16:
        return "Promedio alto"
    elif total >= 14:
        return "Promedio"
    elif total >= 12:
        return "Promedio bajo"
    elif total >= 11:
        return "Por debajo del promedio"
    elif total >= 10:
        return "Bajo"
    else:
        return "Muy bajo"

def califinal(total):
    if total >= 57:
        return "Muy alto"
    elif total >= 52:
        return "Alto"
    elif total >= 50:
        return "Por encima del promedio"
    elif total >= 48:
        return "Promedio alto"
    elif total >= 43:
        return "Promedio"
    elif total >= 39:
        return "Promedio bajo"
    elif total >= 37:
        return "Por debajo del promedio"
    elif total >= 34:
        return "Bajo"
    else:
        return "Muy bajo"