from extensions.extensions import db
from sqlalchemy import Column, Integer,CHAR,Date,String,ForeignKey

class ResultadosHE(db.Model):
    __tablename__ = 'resultadoshe'
    idResultadoHE= Column(Integer,primary_key=True)
    resultadoseccion1 = Column(String(45))
    resultadoseccion2 = Column(String(45))
    resultadoseccion3 = Column(String(45))
    resultadofinal = Column(String(45))
    calificacionseccion1 =  Column(Integer)
    calificacionseccion2 =  Column(Integer)
    calificacionseccion3 =  Column(Integer)
    calificacionfinal =  Column(Integer)
    idUsuario = Column(Integer, ForeignKey('usuarios.idusuario'))
    encuesta = db.relationship("Usuario", backref='resultadoshe', order_by=idResultadoHE)

