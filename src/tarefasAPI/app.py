from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

tarefas = [
    {
        'id': 0,
        'responsavel': u'Amanda',
        'tarefa': u'Fazer compras',
        'status': False
    },
    {
        'id': 1,
        'responsavel': u'Bryan',
        'tarefa': u'Consertar o PC',
        'status': False
    }
]

# Consulta todas as tarefas e insere uma nova tarefa
@app.route('/tarefas/', methods=['GET', 'POST'])

def get_tarefas():
    if request.method == 'GET':
        return jsonify(tarefas)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])
    
# Consulta uma tarefa específica, altera ou deleta
@app.route('/tarefas/<int:tarefa_id>', methods=['GET', 'PUT', 'DELETE'])

def get_tarefa(tarefa_id):  
    if request.method == 'GET':
        try:
            response = tarefas[tarefa_id]
        except IndexError:
            mensagem = 'Tarefa de ID {} não existe'.format(tarefa_id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        # Verifica se 'status' está nos dados recebidos e se a tarefa existe
        if 'status' in dados and tarefa_id < len(tarefas):
            # Atualiza apenas o status
            tarefas[tarefa_id]['status'] = dados['status']
            return jsonify(tarefas[tarefa_id])
        else:
            return jsonify({'status': 'erro', 'mensagem': 'Chave status ausente ou tarefa inexistente'})
    elif request.method == 'DELETE':
        tarefas.pop(tarefa_id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluido'})
            


# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True)