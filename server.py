from flask import Flask, request, jsonify, flash
from config import db, app
from models import Pessoa, Dividas, Bens, Dados, Compra, User
from schm import PessoaSchema, DividaSchema, PessoaDetalhamentoSchema, BensSchema, DadosSchema, CompraSchema, UserSchema
from flask_optimize import FlaskOptimize
from flask_login import LoginManager, login_user , logout_user , current_user , login_required
from passlib.hash import sha256_crypt

app.secret_key = 'super secret key'
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

flask_optimize = FlaskOptimize()

#Declaracoes de Schemas
user_schema = UserSchema()

pessoa_schema = PessoaSchema()
pessoas_schema = PessoaSchema(many=True)

pessoa_detalhamento_schema = PessoaDetalhamentoSchema()
pessoas_detalhamento_schema = PessoaDetalhamentoSchema(many=True)

divida_schema = DividaSchema()
dividas_schema = DividaSchema(many=True)

ben_schema = BensSchema()
bens_schema = BensSchema(many=True)

dado_schema = DadosSchema()
dados_schema = DadosSchema(many=True)

compra_schema = CompraSchema()
compras_schema = CompraSchema(many=True)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    user = User(username, password, email)

    db.session.add(user)
    db.session.commit()

    flash('User successfully registered')
    return user_schema.jsonify(user)


@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    registered_user = User.query.filter_by(username=username).first()

    val = sha256_crypt.verify(password, registered_user.password)

    if registered_user is None:
        flash('Username is invalid' , 'error')
        return jsonify('{message: username invalida}')
    if val == False:
        flash('Password is invalid', 'error')
        return jsonify('{message: senha invalida}')

    login_user(registered_user)
    flash('Logged in successfully')
    return jsonify('{message: success}')

@app.route('/logout')
def logout():
    logout_user()
    return jsonify("{message: successfully logout}")

# endpoint para nova pessoa
@app.route("/api/post/pessoa", methods=["POST"])
@login_required
def post_pessoa():
    cpf = request.json['cpf']
    nome = request.json['nome']
    endereco = request.json['endereco']
    idade = request.json['idade']
    renda = request.json['renda']

    new_pessoa = Pessoa(cpf, nome, endereco, idade, renda)

    db.session.add(new_pessoa)
    db.session.commit()

    return pessoa_schema.jsonify(new_pessoa)


# endpoint para mostrar todas pessoas cadastradas
@app.route("/api/get/pessoa", methods=["GET"])
@login_required
@flask_optimize.optimize('json')
def get_pessoa():
    all_users = Pessoa.query.all()
    result = pessoas_schema.dump(all_users)
    return jsonify(result.data)


# endpoint para mostrar detalhamento
@app.route("/api/get/pessoa_detalhamento", methods=["GET"])
@login_required
@flask_optimize.optimize('json')
def get_pessoa_detalhamento():
    all_users = Pessoa.query.all()
    result = pessoas_detalhamento_schema.dump(all_users)
    return jsonify(result.data)


# endpoint para nova divida
@app.route("/api/post/dividas", methods=["POST"])
@login_required
def post_dividas():
    user_id = request.json['user_id']
    divida_descricao = request.json['divida_descricao']

    new_divida = Dividas(user_id, divida_descricao)

    db.session.add(new_divida)
    db.session.commit()

    return divida_schema.jsonify(new_divida)


# endpoint para mostrar todos dividas
@app.route("/api/get/dividas", methods=["GET"])
@login_required
@flask_optimize.optimize('json')
def get_dividas():
    all_dividas = Dividas.query.all()
    result = dividas_schema.dump(all_dividas)
    return jsonify(result.data)


# endpoint para novos bens
@app.route("/api/post/bens", methods=["POST"])
@login_required
def post_bens():
    user_id = request.json['user_id']
    bens_descricao = request.json['bens_descricao']

    new_bens = Bens(user_id, bens_descricao)

    db.session.add(new_bens)
    db.session.commit()

    return ben_schema.jsonify(new_bens)

# endpoint para mostrar todos bens
@app.route("/api/get/bens", methods=["GET"])
@login_required
@flask_optimize.optimize('json')
def get_bens():
    all_bens = Bens.query.all()
    result = bens_schema.dump(all_bens)
    return jsonify(result.data)

# endpoint para novos dados
@app.route("/api/post/dados", methods=["POST"])
@login_required
def post_dados():
    user_id = request.json['user_id']
    ultima_consulta = request.json['ultima_consulta']

    new_dados = Bens(user_id, ultima_consulta)

    db.session.add(new_dados)
    db.session.commit()

    return dado_schema.jsonify(new_dados)

# endpoint para mostrar todos dados
@app.route("/api/get/dados", methods=["GET"])
@login_required
@flask_optimize.optimize('json')
def get_dados():
    all_dados = Dados.query.all()
    result = dado_schema.dump(all_dados)
    return jsonify(result.data)

# endpoint para nova compra
@app.route("/api/post/compra", methods=["POST"])
@login_required
def post_compra():
    user_id = request.json['user_id']
    compra_descricao = request.json['compra_descricao']
    tipo_pagamento = request.json['tipo_pagamento']
    data_pagamento = request.json['data_pagamento']

    new_compra = Bens(user_id, compra_descricao, tipo_pagamento, data_pagamento)

    db.session.add(new_compra)
    db.session.commit()

    return compra_schema.jsonify(new_compra)

# endpoint para mostrar todas compras
@app.route("/api/get/compra", methods=["GET"])
@login_required
@flask_optimize.optimize('json')
def get_compra():
    all_compras = Compra.query.all()
    result = compras_schema.dump(all_compras)
    return jsonify(result.data)

if __name__ == '__main__':
    app.run(debug=True)