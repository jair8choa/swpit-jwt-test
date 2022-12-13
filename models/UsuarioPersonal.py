from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Char,Date
from extensions.extensions import db

class UsuarioPersonal(db.Model):
    __tablename__ = 'usuariopersonal'
    idUsuarioPersonal = Column(Integer, primary_key=True)
    FechaIngreso = Column(Date, unique= False, nullable=False)
    FechaTermino = Column(Date, unique=False, nullable=False)
    Activo = Column(Integer, default=1)

    idPersonal = Column(Integer, ForeignKey('personal.idPersonal'))
    idUsuarios = Column(Integer, ForeignKey('usuarios.idUsuario'))
    personal = db.relationship("Personal", bnackref='usuarioPersonal', order_by=idUsuarioPersonal)
    usuarios = db.relationship("Usuarios", backref='usuarioPersonal', order_by=idUsuarioPersonal)