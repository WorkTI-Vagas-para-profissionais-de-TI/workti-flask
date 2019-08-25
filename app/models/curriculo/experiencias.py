from app import db
from ..usuarios import User

class Experiencias(db.Model):
    __tablename__ = 'experiencias'

    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.String(120))
    cargo = db.Column(db.String(120))
    periodo = db.Column(db.String(20))
    descricao_profissao = db.Column(db.Text())

    id_usuario = db.Column(db.Integer, db.ForeignKey('users.id'))
    usuario = db.relationship('User', foreign_keys=id_usuario)


    def __init__(self, empresa, cargo, periodo, descricao_profissao, id_usuario):
        self.empresa = empresa
        self.cargo = cargo
        self.periodo = periodo
        self.descricao_profissao = descricao_profissao
        self.id_usuario