from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Char,Date
from extensions.extensions import db

class PadresEstudiantes(db.Model):
    __tablename__ = 'padresestudiantes'
    idPadreEstudiantes = Column(Integer, primary_key=True)
    idPadresFamilia = Column(Integer, ForeignKey('padresFamilia.idPadresFamilia'))
    idEstudiante = Column(Integer, ForeignKey('estudiantes.idEstudiante'))
    padresFamilia = db.relationship("PadresFamilia", backref='padresEstudiantes', order_by=idPadreEstudiantes)
    estudiantes = db.relationship ("Estudiantes", backref='padresEstudiantes', order_by=idPadreEstudiantes)