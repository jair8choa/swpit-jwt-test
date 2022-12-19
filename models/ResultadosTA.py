from extensions.extensions import db
from sqlalchemy import Column, Integer,CHAR,Date,String,ForeignKey,Text

class ResultadosTA(db.Model):
    __tablename__ = 'resultadosta'
    idResultadosTA= Column(Integer,primary_key=True)
    resultado = Column(String(45))
    cantidad1 =  Column(Integer)
    cantidad2 =  Column(Integer)
    cantidad3 =  Column(Integer)
    cantidad4 =  Column(Integer)
    mensaje = Column(Text)
    idUsuario = Column(Integer, ForeignKey('usuarios.idusuario'))
    encuesta = db.relationship("Usuario", backref='resultadosta', order_by=idResultadosTA)

