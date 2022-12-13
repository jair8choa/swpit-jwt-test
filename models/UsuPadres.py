from extensions.extensions import db

class UsuPadres(db.Model):
    __tablename__ = 'usuPadres'
    idUsuPadres = Column(Integer, primary_key=True)
    FechaIngreso = Column(Date, unique=False, nullable=False)
    FechaTermino = Column(Date, unique=False, nullable=False)
    activo = Column(Integer, default=1)

    idUsuarios = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPadresFamilia = Column(Integer, ForeignKey('padresFamilia.idPadresFamilia'))
    padresFamilia = db.relationship("PadresFamilia", backref='usuPadres', order_by=idUsuPadres)
    usuarios = db.relationship("Usuarios", backref='usuPadres', order_by=idUsuPadres)