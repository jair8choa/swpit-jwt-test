from extensions.extensions import db

class PadresFamilia(db.Model):
    __tablename__ = 'padresfamilia'
    idPadresFamilia =Column(Integer, primary_key=True)
    Apellidos =  Column(String(200), unique=False, nullable=False)
    Nombre = Column(String(100), unique=False, nullable=False)
    Sexo = Column(Integer, unique=False, nullable=False)
    EstadoTrabajo = Column(Integer, unique=False, nullable=False)
    TelTrabajo = Column(Char(12), unique=True, nullable=False)
    EstadoVido = Column(Integer, nullable=True, nuallable=False)