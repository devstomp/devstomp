from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db/devstomp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "index"
login_manager.init_app(app)

# Dependenices from app
from app import forms
from app import db
