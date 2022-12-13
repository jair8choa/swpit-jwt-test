from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Char,Date
from extensions.extensions import db

class PadresFamilia(db.Model):
    __tablename__ = 'padresfamilia'
    idPadresFamilia =Column(Integer, primary_key=True)
    Apellidos =  Column(String(200), unique=False, nullable=False)
    Nombre = Column(String(100), unique=False, nullable=False)
    Sexo = Column(Integer, unique=False, nullable=False)
    EstadoTrabaja = Column(Integer, unique=False, nullable=False)
    TelefonoTrabajo = Column(Char(12), unique=True, nullable=False)
    EstadoVive = Column(Integer, nullable=True, nuallable=False)