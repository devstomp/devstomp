#!venv/bin/python

from app import app
from config import *
from flask import render_template, redirect, url_for, flash, request, session
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy

import pkg_resources
import os, requests
from datetime import datetime

app.secret_key = os.urandom(128)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
