from app import db
from ..usuarios import User

class Cursos(db.Model):
    __tablename__ = 'cursos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.Text())
    instituicao = db.Column(db.String(80))


    id_usuario = db.Column(db.Integer, db.ForeignKey('users.id'))
    usuario = db.relationship('User', foreign_keys=id_usuario)


    def __init__(self, nome, descricao, instituicao, id_usuario):
        self.nome = nome
        self.descricao = descricao
        self.instituicao = instituicao
        self.id_usuario = id_usuario
