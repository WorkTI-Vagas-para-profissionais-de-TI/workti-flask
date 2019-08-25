from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired


# curriculo
class CurriculoForm(FlaskForm):
    # as informações pessoais serão instanciadas de outros models
     
    # endereco
    numero = IntegerField('numero')
    ap = IntegerField('ap')
    bloco = StringField('bloco')
    rua = StringField('rua', validators=[DataRequired()])
    quadra = StringField('quadra')
    bairro = StringField('bairro', validators=[DataRequired()])
    cidade = StringField('cidade', validators=[DataRequired()])
    estado = StringField('estado', validators=[DataRequired()])
    # id usuario
    ### cursos
    nome = StringField('nome')
    descricao = StringField('descricao')
    instituicao = StringField('instituicao')
    # id usuario
    #### experiencias
    empresa = StringField('nome')
    cargo = StringField('descricao')
    periodo = StringField('instituicao')
    descricao_profissao = StringField('instituicao')
    # id usuario
    ### certificados
    titulo = StringField('titulo')
    data_expedicao = StringField('data_expedicao')
    descricao_certificado = StringField('descricao_certificado')
    # id usuario
