from app import db
from .curriculo import certificados, cursos, enderecos, experiencias
from .usuarios import User

class Curriculo(db.Model):
    __tablename__ = 'curriculos'

    id = db.Column(db.Integer, primary_key=True)

    id_certificados = db.Column(db.Integer, db.ForeignKey('certificados.id'))
    id_cursos = db.Column(db.Integer, db.ForeignKey('cursos.id'))
    id_enderecos = db.Column(db.Integer, db.ForeignKey('enderecos.id'))
    id_experiencias = db.Column(db.Integer, db.ForeignKey('experiencias.id'))
    id_usuario = db.Column(db.Integer, db.ForeignKey('users.id'))

    certificados = db.relationship('Certificados', foreign_keys=id_certificados)
    cursos = db.relationship('Cursos', foreign_keys=id_cursos)
    enderecos = db.relationship('Enderecos', foreign_keys=id_enderecos)
    experiencias = db.relationship('Experiencias', foreign_keys=id_experiencias)
    usuario = db.relationship('User', foreign_keys=id_usuario)

    def __init__(self, id_certificados, id_cursos, id_enderecos, id_experiencias, id_usuario):
        self.id_certificados = id_certificados
        self.id_cursos = id_cursos
        self.id_enderecos = id_enderecos
        self.id_experiencias = id_experiencias
        self.id_usuario = id_usuario