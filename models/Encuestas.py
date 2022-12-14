from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date
from extensions.extensions import db

class Encuestas(db.Model):
    __tablename__ = 'encuestas'
    idEncuesta = Column(Integer,primary_key=True)
    Nombre = Column(String(100), unique=False, nullable=False)
    Descripcion = Column(String(500), unique=False, nullable=False)
    Instrucciones = Column(String(1000), unique=False, nullable=False)
    Observaciones = Column(String(500), unique=False, nullable=True)
    EstadoEncuesta = Column(Integer, unique=False, nullable=False)