from flask_marshmallow import Marshmallow
import config

app = config.retornoFlask()

ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'username', 'password', 'email')

class PessoaSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'cpf', 'nome', 'endereco')

class PessoaDetalhamentoSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'cpf', 'nome', 'endereco', 'idade', 'renda')

class DividaSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'user_id', 'divida_descricao')

class BensSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'user_id', 'bens_descricao')

class DadosSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'user_id', 'ultima_consulta')

class CompraSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'user_id', 'compra_descricao', 'tipo_pagamento', 'data_pagamento')