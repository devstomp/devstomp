from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

Bootstrap(app)

<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db/devstomp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "index"
login_manager.init_app(app)
=======
db = SQLAlchemy(app)
login_manager = LoginManager(app)

#app.register_blueprint(auth.blueprint, url_prefix='/auth')
>>>>>>> e383dc1bb08aa4a09680014044b91f3e6220ae22

# Dependenices from app
from app import forms
from app import db
