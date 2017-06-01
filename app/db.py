from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.username = username
        self.authenticated = False

    def __repr__(self):
        return '<User %r>' % self.name

class Information(db.Model):
    __tablename__ = 'information'
    
    github = db.Column(db.String(20), unique=True, nullable=False)
    twitter = db.Column(db.String(20), unique=True, nullable=False)
    linkedin = db.Column(db.String(20), unique=True, nullable=False)
    gravatar = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(100), unique=True, nullable=False)