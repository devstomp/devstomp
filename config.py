from app import app
from os import urandom

'''
Configuration file for devstomp
'''

app.secret_key = urandom(128)
