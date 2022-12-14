from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date
from extensions.extensions import db

class Tipos(db.Model):
    __tablename__ = 'tipos'
    idTipoPregunta = Column(Integer, primary_key=True)
    Nombre = Column(String(50), unique=False, nullable=False),
    Opcion = Column(Integer, unique=False, nullable= False)