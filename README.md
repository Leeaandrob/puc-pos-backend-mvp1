# API Project

É um projeto voltado para a modelagem de um sistema que registra um produto, lista produtos
e deleta produto

## Setup

Para instalar esse projeto você precisa ter o python3 instalado no seu computador.

Para isso siga a instrução desse site["https://www.python.org/downloads/"]

Após o python istalado você precisa instalar as depedências utilizando o comando abaixo:

```
python3 -m venv .
source bin/activate
pip install -r requirements.txt
FLASK_APP=app.py flask db init
FLASK_APP=app.py flask  db migrate -m "entries table"
FLASK_APP=app.py flask db upgrade
```

## Routes:

### http://localhost:5000/
Request:

```
curl -v http://localhost:5000/
```

Response:

```
WORKING
```
