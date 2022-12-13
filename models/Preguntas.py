from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Char,Date
from ..extensions import db

class Preguntas(db.Model):
    __tablename__ = 'preguntas'
    idPregunta = Column(Integer, primary_key=True)
    NumeroPregunta = Column(Integer, unique=False, nullable=False)
    TituloPregunta = Column(String(200), unique=False, nullable=False)
    idTipoPregunta = Column(Integer, ForeignKey('tipos.idTipoPregunta'))
    Tipos = db.relationship("Tipos", backref='preguntas', order_by=idPregunta)
    idSeccion = Column(Integer, ForeignKey('seccion.idSeccion'))
    Seccion = db.relationship("Seccion", backref='preguntas', order_by=idPregunta)