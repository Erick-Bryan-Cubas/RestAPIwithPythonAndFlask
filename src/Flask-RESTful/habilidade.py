from flask_restful import Resource
from flask import request

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = request.json
        habilidade = dados.get('habilidade')
        if habilidade and habilidade not in lista_habilidades:
            lista_habilidades.append(habilidade)
            return {"status": "sucesso", "mensagem": f"Habilidade {habilidade} adicionada."}
        return {"status": "erro", "mensagem": "Habilidade inválida ou já existe."}

    def put(self, id):
        if id < len(lista_habilidades):
            dados = request.json
            lista_habilidades[id] = dados.get('habilidade')
            return {"status": "sucesso", "mensagem": f"Habilidade na posição {id} atualizada."}
        return {"status": "erro", "mensagem": "Índice inválido."}

    def delete(self, id):
        if id < len(lista_habilidades):
            lista_habilidades.pop(id)
            return {"status": "sucesso", "mensagem": f"Habilidade na posição {id} removida."}
        return {"status": "erro", "mensagem": "Índice inválido."}
