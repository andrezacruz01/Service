from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_compress import Compress

#Metodo de retorno do app
def retornoFlask():
    app = Flask(__name__)

    return app

COMPRESS_MIMETYPES = ['text/html', 'text/css', 'application/json']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500

app = retornoFlask()

Compress(app)

#Predefinicoes de banco

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'base.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)