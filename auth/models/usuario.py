from ..extensions import db
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idusuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    correo = db.Column(db.String(200), unique=True, nullable=False)
    clave = db.Column(db.String(200))
    activo = db.Column(db.Integer, default=1)

    def __str__(self):
        return self.idusuario+"."+self.nombre+"."+self.correo

    def __repr__(self):
        return '<Usuarios %r>' % self.nombre