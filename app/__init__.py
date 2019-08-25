from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# app more config
app = Flask(__name__)
app.config.from_object('config')


# databse connection
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# migrate commands
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# login manager
lm = LoginManager()
lm.init_app(app)


# models
from app.models import curriculos
from app.models import vagas


# forms
from app.forms import login
from app.forms import register
from app.forms import vagas


# controllers
from app.controllers import default
from app.controllers import vagas
from app.controllers import curriculos
