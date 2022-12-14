
from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date
from extensions.extensions import db

class Seccion(db.Model):
    __tablename__ = 'seccion'
    idSeccion =  Column(Integer, primary_key=True)
    Titulo = Column(String(200), unique=False, nullable=False)
    Instrucciones = Column(String(500), unique=False, nullable=True)
    idEncuesta = Column(Integer, ForeignKey('encuestas.idEncuesta'))
    encuesta = db.relationship("Encuestas", backref='seccion', order_by=idSeccion)
