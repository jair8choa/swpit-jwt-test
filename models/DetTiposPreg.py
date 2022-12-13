from sqlalchemy import Integer,Column,String,Boolean,ForeignKey,Char,Date
from ..extensions import db

class DetTiposPreg(db.Model):
    __tablename__ = 'dettipospreg'
    idDetTipoPreg = Column(Integer, primary_key=True)
    Opcion = Column(String(50), unique=False, nullable=False)
    idTipoPregunta = Column(Integer, ForeignKey('tipos.idTipoPregunta'))
    Tipos = db.relationship("Tipos", backref='detTiposPreg', order_by=idDetTipoPreg)