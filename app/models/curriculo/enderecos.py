from app import db
from ..usuarios import User

class Enderecos(db.Model):
    __tablename__ = 'enderecos'

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    ap = db.Column(db.Integer)
    bloco = db.Column(db.String(20))
    rua = db.Column(db.String(80))
    quadra = db.Column(db.String(20))
    bairro = db.Column(db.String(80))
    cidade = db.Column(db.String(100))
    estado = db.Column(db.String(80))


    id_usuario = db.Column(db.Integer, db.ForeignKey('users.id'))
    usuario = db.relationship('User', foreign_keys=id_usuario)


    def __init__(self, numero, ap, bloco, rua, quadra, bairro, cidade, estado, id_usuario):
        self.numero = numero
        self.ap = ap
        self.bloco = bloco
        self.rua = rua
        self.quadra = quadra
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.id_usuario = id_usuario