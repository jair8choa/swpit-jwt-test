from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,CHAR,Date
from extensions.extensions import db
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idusuario = Column(Integer, primary_key=True)
    Nombre = Column(String(50), unique=True, nullable=False)
    Correo = Column(String(200), unique=True, nullable=False)
    Clave = Column(String(200))
    Activo = Column(Integer, default=1)

    def __str__(self):
        return self.idusuario+"."+self.nombre+"."+self.correo

    def __repr__(self):
        return '<Usuarios %r>' % self.nombre