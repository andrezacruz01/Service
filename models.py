from config import db
from passlib.hash import sha256_crypt

#Descricao dos models
class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, index=True)
    password = db.Column('password', db.String(10))
    email = db.Column('email', db.String(50), unique=True, index=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = self.set_password(password)
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def set_password(self, password):
        return sha256_crypt.encrypt(password)

    def __repr__(self):
        return '<User %r>' % (self.username)

class Pessoa(db.Model):
    __tablename__ = 'pessoa'
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True)
    nome = db.Column(db.String(255))
    endereco = db.Column(db.String(255))
    idade = db.Column(db.Integer)
    renda = db.Column(db.String(255))

    def __init__(self, cpf, nome, endereco, idade, renda):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.idade = idade
        self.renda = renda


class Dividas(db.Model):
    __tablename__ = 'dividas'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'))
    divida_descricao = db.Column(db.String(255))

    def __init__(self, user_id, divida_descricao):
        self.user_id = user_id
        self.divida_descricao = divida_descricao

class Bens(db.Model):
    __tablename__ = 'bens'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'))
    bens_descricao = db.Column(db.String(255))

    def __init__(self, user_id, bens_descricao):
        self.user_id = user_id
        self.bens_descricao = bens_descricao


class Dados(db.Model):
    __tablename__ = 'dados'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'))
    ultima_consulta = db.Column(db.String(30))

    def __init__(self, user_id, ultima_consulta):
        self.user_id = user_id
        self.ultima_consulta = ultima_consulta

class Compra(db.Model):
    __tablename__ = 'compra'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'))
    compra_descricao = db.Column(db.String(255))
    tipo_pagamento = db.Column(db.String(100))
    data_pagamento = db.Column(db.String(100))

    def __init__(self, user_id, compra_descricao, tipo_pagamento, data_pagamento):
        self.user_id = user_id
        self.compra_descricao = compra_descricao
        self.tipo_pagamento = tipo_pagamento
        self.data_pagamento = data_pagamento