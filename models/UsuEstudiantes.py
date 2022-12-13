from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Char,Date
from extensions.extensions import db

class UsuEstudiantes(db.Model):
    __tablename__ = 'usuestudiantes'
    idUsoEstudiante = Column(Integer, primary_key=True)
    FechaIngreso= Column(Date, unique=True, nullable=False)
    FechaTermino= Column(Date, unique=True, nullable=True)
    Activo = Column(Integer, default=1)

    idEstudiante = Column(Integer, ForeignKey('estudiantes.idEstudiantes'))
    idUsuarios = Column(Integer, ForeignKey('estudiantes.idEstudiantes'))
    estudiantes = db.relationship ("Estudiantes", backref='usoEstudiantes', order_by=idUsoEstudiante)
    usuarios = db.relationship ("Usuarios", backref='usoEstudiantes', order_by=idUsoEstudiante)