# Service
Para executar a aplicação  é necessario:

pip install - 

Flask (1.0.2)
flask-marshmallow (0.9.0)
Flask-SQLAlchemy (2.3.2)
marshmallow (2.16.3)
marshmallow-sqlalchemy (0.15.0)
flask-compress (1.4.0)
passlib (1.7.1)

Execução:
No terminal:

Para criar database:

python
from models import db
db.create_all()
exit()

export FLASK_APP=server.py
flask run

VERIFIQUE QUAL PORTA O FLASK ESTA RODANDO!

PARA TER ACESSO AOS ENDPOINTS:
Precisa realizar o /register
com email e username únicos.

Após, sucesso, pode fazer o login com username e password no /login.
