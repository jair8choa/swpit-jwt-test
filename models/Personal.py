from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Char,Date
from extensions.extensions import db

class Personal(db.Model):
    __tablename__ = 'personal'
    idPersonal = Column(Integer, primary_key=True)
    nt = Column(Integer, unique=True, nullable=False)
    Apellidos = Column(String(100), nullable=False)
    Nombre = Column(String(100), nullable=False)
    rfc = Column(Char(13), unique=True, nullable=False)
    Direccion = Column(String(200), nullable=False)
    CorreoPersonal = Column(String(200), unique=True, nullable=False)
    CorreoInstitucional = Column(String(200), unique=True, nullable=False)
    TelCelular = Column(Char(12), unique=True, nullable=False)
    TelCasa = Column(Char(12), unique=True, nullable=True)
    Plaza = Column(Char(12), unique=False, nullable=False)
    Tipo = Column(Char, unique=False, nullable=False)