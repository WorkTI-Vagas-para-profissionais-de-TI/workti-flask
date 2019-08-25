from flask import render_template, flash
from flask_login import login_required, current_user
from app import app, db


from app.models.curriculos import Curriculo
from app.models.curriculo.certificados import Certificados
from app.models.curriculo.cursos import Cursos
from app.models.curriculo.enderecos import Enderecos
from app.models.curriculo.experiencias import Experiencias


from app.forms.curriculo import CurriculoForm


# CREATE
@app.route('/curriculo/register', methods=['GET', 'POST'])
@login_required
def createCurriculo():
    form = CurriculoForm()
    if form.validate_on_submit():
        endereco = Enderecos(
            form.numero.data,
            form.ap.data,
            form.bloco.data,
            form.rua.data,
            form.quadra.data,
            form.bairro.data,
            form.cidade.data,
            form.estado.data,
            current_user.id
        )
        db.session.add(endereco)
        db.session.commit()
        certificado = Certificados(
            form.titulo.data,
            form.data_expedicao.data,
            form.descricao_certificado.data,
            current_user.id
        )
        db.session.add(certificado)
        db.session.commit()

        curso = Cursos(
            form.nome.data,
            form.descricao.data,
            form.instituicao.data,
            current_user.id
        )
        db.session.add(curso)
        db.session.commit()
        experencia = Experiencias(
            form.empresa.data,
            form.cargo.data,
            form.periodo.data,
            form.descricao_profissao.data,
            current_user.id
        )
        db.session.add(experencia)
        db.session.commit()
        curriculo = Curriculo(
            certificado.id,
            curso.id,
            endereco.id,
            experencia.id,
            current_user.id
        )
        db.session.add(curriculo)
        db.session.commit()
        flash('Currículo cadastrado!')
    else:
        print(form.errors)
    return render_template('curriculos/register.html', form=form)
