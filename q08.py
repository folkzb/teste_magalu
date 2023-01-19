from flask import request
import flask

app = flask.Flask(__name__)

numero = {"numero": 0}

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/contador", methods=['POST','GET','DELETE','PATCH','HEAD','OPTIONS','PROPFIND','CUSTOM'])
def contador():
    global numero
    if flask.request.method == 'POST':
        numero=''
        numero = request.get_json()
        return '',201
    elif flask.request.method == 'GET':
        return numero
    elif flask.request.method == 'DELETE':
        numero={"numero": 0}
        return '',202
    else:
        return {'error':'método invalido'}, 202

@app.route("/contador/incrementa", methods=['PUT'])
def incrementa():
    if flask.request.method == 'PUT':
        global numero
        numero=numero['numero']
        inc = numero+1
        numero = {"numero": inc}
        return '',202
    else:
        return '',202


if __name__ == '__main__':
    app.run(app.run(port=6000, host='0.0.0.0', debug=True))