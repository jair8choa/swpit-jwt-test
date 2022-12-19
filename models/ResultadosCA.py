from extensions.extensions import db
from sqlalchemy import Column, Integer,CHAR,Date,String,ForeignKey,Text

class ResultadosCA(db.Model):
    __tablename__ = 'resultadosca'
    idResultadoCA= Column(Integer,primary_key=True)
    visual =  Column(Integer)
    auditivo =  Column(Integer)
    kinestesico =  Column(Integer)
    resultado =  Column(Text)
    idUsuario = Column(Integer, ForeignKey('usuarios.idusuario'))
    encuesta = db.relationship("Usuario", backref='resultadosca', order_by=idResultadoCA)

