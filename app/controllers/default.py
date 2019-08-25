from flask import render_template, flash, redirect, url_for, session
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, lm
from datetime import timedelta
from sqlalchemy.exc import OperationalError

from app.models.usuarios import User

from app.forms.login import LoginForm
from app.forms.register import RegisterForm


@app.errorhandler(401)
def unauthorized(e):
    return render_template('errors/401.html'), 401


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()



@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=120)


# index
@app.route('/index')
@app.route('/')
def index():
    try:
      #return render_template('index.html')
      return redirect(url_for('login'))
    except OperationalError:
      flash('Banco de dados não conectado')
      return 'Base de dados nao conectado'


# register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        novo_usuario = User(form.name.data, form.email.data, form.password.data)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Agora você pode logar no sistema.')
        return redirect(url_for('login'))
    return render_template('usuario/register.html', form=form)



# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # se o usuario existe
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Seja bem vindo(a) ' + current_user.name)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('getVagas'))
        else:
            flash('Informações inválidas.')
    else:
        print(form.errors)
    return render_template('usuario/login.html', form=form)



# logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Deslogado com sucesso.')
    return redirect(url_for('index'))
