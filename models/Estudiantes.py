from extensions.extensions import db
from sqlalchemy import Column, Integer,CHAR,Date,String

class Estudiantes(db.Model):
    __tablename__ = 'estudiantes'
    idEstudiante= Column(Integer,primary_key=True)
    NumeroControl = Column(CHAR(10), unique=True, nullable=False)
    ApellidoPaterno = Column(String(100), unique=True, nullable=False)
    ApellidoMaterno = Column(CHAR(100), unique=True, nullable=False)
    Nombre = Column(String(100), unique=True, nullable=False)
    Sexo= Column(Integer, unique=True, nullable=False)
    Nacimiento= Column(Date, unique=True, nullable=False)
    RFC= Column(CHAR(13), unique=True, nullable=False)
    ESC= Column(Integer, unique=True, nullable=False)