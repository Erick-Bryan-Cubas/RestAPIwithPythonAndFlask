from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def minha_api(id):
    soma = 1 + id
    return jsonify({'id': id, 'nome': 'Bryan', 'profissao': 'Desenvolvedor'})


# @app.route('/soma/<int:valor1>/<int:valor2>')
# def soma(valor1, valor2):
#    return jsonify({'soma': valor1 + valor2})


@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
        print(dados)
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma': total})


if __name__ == '__main__':
    app.run(debug=True)