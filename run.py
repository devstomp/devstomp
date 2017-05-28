#!venv/bin/python

from app import app
from config import *
from app.forms import LoginForm, SignupForm
from flask import render_template, redirect, url_for, flash, request, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy

import pkg_resources
import os, requests
from datetime import datetime

login_manager = LoginManager(app)
login_manager.login_view = "index"

# Test variable
user = "Alan"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
# Go to home if not logged in. Otherwise redirect to profile
def index():
    form = LoginForm()
    if session.get('logged_in'):
        return redirect(url_for('profile', user=user))
    else:
        return render_template('index.html', user=user, form=form)
        if request.method == 'POST':
            session['logged_in'] = True
            return redirect(url_for('index'))

# Profile Page 
@app.route("/profile/<user>", methods=['GET'])
def profile(user):
    return render_template('profile.html', user=user)

# About Page - Static
@app.route("/about")
def about():
    return render_template('about.html')

# Setting Page - Static, but alters JS of webpage
@app.route("/settings")
def settings():
    return render_template('settings.html')

# Logout by removing logged_in session cookie, redirecting to index
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
