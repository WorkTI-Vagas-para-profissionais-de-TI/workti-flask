from app import db
from ..usuarios import User

class Certificados(db.Model):
    __tablename__ = 'certificados'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(40))
    data_expedicao = db.Column(db.String(20))
    descricao_certificado = db.Column(db.Text())


    id_usuario = db.Column(db.Integer, db.ForeignKey('users.id'))
    usuario = db.relationship('User', foreign_keys=id_usuario)


    def __init__(self, titulo, data_expedicao, descricao_certificado, id_usuario):
        self.titulo = titulo
        self.data_expedicao = data_expedicao
        self.descricao_certificado = descricao_certificado
        self.id_usuario = id_usuario