from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from app import app, db


from app.models.vagas import Vagas
from app.forms.vagas import VagasForm


# CREATE
@app.route('/vagas/register', methods=['GET', 'POST'])
@login_required
def insertVaga():
    form = VagasForm()
    if form.validate_on_submit():
        vagas = Vagas(
            form.titulo.data,
            form.descricao.data,
            form.dataPublicacao.data,
            current_user.id
        )
        db.session.add(vagas)
        db.session.commit()
        flash('Dados inseridos com sucesso')
    else:
        print(form.errors)
    return render_template('vagas/register.html', form=form)


# READ ALL
@app.route('/vagas')
@login_required
def getVagas():
    vaga = Vagas.query.all()
    return render_template('vagas/list.html', vaga=vaga)



# READ BY ID
@app.route('/vagas/id/<id>')
@login_required
def getVagasById(id):
    vaga = Vagas.query.filter_by(id=id).all()
    if vaga:
        return render_template('vagas/list.html', vaga=vaga)
    else:
        flash('Vaga não foi encontrada!')
        return redirect(url_for('getVagas'))



# UPDATE BY ID
@app.route('/vagas/edit/<id>', methods=['GET', 'POST'])
@login_required
def editVaga(id):
    vaga = Vagas.query.filter_by(id=id).first()
    print(vaga.id)
    if not vaga:
        flash('Essa vaga não existe no nosso sistema')
        return redirect(url_for('getVagas'))

    if vaga.id_usuario != current_user.id:
        flash('Você não pode editar essa vaga!')
        return redirect(url_for('getVagas'))
    else:
        form = VagasForm()

        if form.validate_on_submit():
            vaga.id = id
            vaga.titulo = form.titulo.data
            vaga.descricao = form.descricao.data
            vaga.dataPublicacao = form.dataPublicacao.data

            db.session.commit()
            flash('Informações atualizadas com sucesso')
    return render_template('vagas/register.html', form=form)



# DELETE ALL
@app.route('/vagas/delete-minhas-vagas/all')
@login_required
def deleteAllVagas():
    vaga = Vagas.query.filter_by(id_usuario=current_user.id).all()
    db.session.delete(vaga)
    db.session.commit()
    flash('Todas as vagas da sua empresa foram deletadas.')
    return redirect(url_for('getVagas'))



# DELETE BY ID
@app.route('/vagas/delete/id/<id>')
@login_required
def deleteVagaById(id):
    vaga = Vagas.query.filter_by(id=id).first()
    if vaga.id_usuario != current_user.id:
        flash('Você não pode deletar essa vaga!')
        return redirect(url_for('getVagas'))
    else:
        vaga = Vagas.query.filter_by(id=id).first()
        db.session.delete(vaga)
        db.session.commit()
        flash('Vaga deletada com sucesso.')
        return redirect(url_for('getVagas'))
