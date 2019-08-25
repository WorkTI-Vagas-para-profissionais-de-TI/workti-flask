from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class VagasForm(FlaskForm):
    titulo = StringField('titulo', validators=[DataRequired()])
    descricao = StringField('descricao', widget=TextArea(), validators=[DataRequired()])
    dataPublicacao = StringField('dataPublicacao', validators=[DataRequired()])
