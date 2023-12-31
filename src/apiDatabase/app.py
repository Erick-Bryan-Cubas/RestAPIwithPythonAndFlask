from flask import Flask, request
from flask_restful import Api, Resource
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth
import json

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# Credenciais de acesso em dicionário
# USUARIOS = {
#    'Bryan': 'jdTExrf97l',
#    'DIO': 'rA7hTEFJ2Z'
# }

# @auth.verify_password
# def verificacao(login, senha):
#    print('Validando usuário')
#    print(USUARIOS.get(login) == senha)
#    if not (login, senha):
#        return False
#    return USUARIOS.get(login) == senha

# @auth.verify_password
# def verificacao(login, senha):
#    print('Validando usuário')
#    if not (login, senha):
#        return False
#    return Usuarios.query.filter_by(login=login, senha=senha).first()


@auth.verify_password
def verificacao(login, senha):
    print('Validando usuário')
    if not (login, senha):
        return False
    usuario = Usuarios.query.filter_by(login=login).first() 
    if usuario and usuario.senha == senha and usuario.ativo:
        return True
    return False


class Pessoa(Resource):
    @auth.login_required # Para acessar o método get é necessário estar logado
    
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'
            }
        return response
    
    @auth.login_required
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response
    
    @auth.login_required
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = f'Pessoa {pessoa.nome} excluída com sucesso'
        pessoa.delete()
        return {'status': 'sucesso', 'mensagem': mensagem}
    

class ListaPessoas(Resource):
    
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response
    
    @auth.login_required
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response
    
class ListaAtividades(Resource):
    
    @auth.login_required
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome, 'status': i.status} for i in atividades]
        return response
    
    @auth.login_required
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response
    

class AtividadesPorPessoa(Resource):
    
    @auth.login_required
    def get(self, nome_pessoa):
        pessoa = Pessoas.query.filter_by(nome=nome_pessoa).first()
        if pessoa:
            atividades = Atividades.query.filter_by(pessoa_id=pessoa.id).all()
            response = [{'id': atividade.id, 'nome': atividade.nome, 'status': atividade.status} for atividade in atividades]
            return response
        return {'status': 'error', 'mensagem': 'Pessoa não encontrada'}
    

class AtividadeStatus(Resource):
    
    @auth.login_required
    def get(self, id):
        atividade = Atividades.query.get(id)
        if atividade:
            response = {'id': atividade.id, 'nome': atividade.nome, 'status': atividade.status}
            return response
        return {'status': 'error', 'mensagem': 'Atividade não encontrada'}

    @auth.login_required
    def put(self, id):
        atividade = Atividades.query.get(id)
        if atividade:
            dados = request.json
            if 'status' in dados:
                atividade.status = dados['status']
                atividade.save()
                response = {'id': atividade.id, 'nome': atividade.nome, 'status': atividade.status}
                return response
            return {'status': 'error', 'mensagem': 'Campo status não fornecido'}
        return {'status': 'error', 'mensagem': 'Atividade não encontrada'}

    
api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')
api.add_resource(AtividadesPorPessoa, '/atividades/pessoa/<string:nome_pessoa>/')
api.add_resource(AtividadeStatus, '/atividades/status/<int:id>/')


if __name__ == '__main__':
    app.run(debug=True)