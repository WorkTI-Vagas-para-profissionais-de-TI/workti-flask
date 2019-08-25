from app import db
from .usuarios import User


class Vagas(db.Model):
    __tablename__ = 'vagas'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80))
    descricao = db.Column(db.Text())
    dataPublicacao = db.Column(db.Text())
    id_usuario = db.Column(db.Integer, db.ForeignKey('users.id'))
        # na tabela USERS ele referencia ao id de usuario
    usuario = db.relationship('User', foreign_keys=id_usuario)


    def __init__(self, titulo, descricao, dataPublicacao, id_usuario):
        self.titulo = titulo
        self.descricao = descricao
        self.dataPublicacao = dataPublicacao
        self.id_usuario = id_usuario

    def __repr__(self):
        return '<Vagas %r>' % self.id
