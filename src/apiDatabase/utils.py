from models import Pessoas, Usuarios, db_session

def insere():
    pessoa = Pessoas(nome='Bryan', idade=24)
    print(pessoa)
    db_session.add(pessoa)
    db_session.commit()
    
def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome='Bryan').first()
    # print(pessoa.idade)

def altera():
    pessoa = Pessoas.query.filter_by(nome='Bryan').first()
    pessoa.nome = 'Erick Bryan'
    pessoa.save()
    
def exclui():
    pessoa = Pessoas.query.filter_by(nome='Erick Bryan').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)
    

def altera_usuario(login, senha, ativo):
    usuario = Usuarios.query.filter_by(login=login).first()
    usuario.senha = senha
    usuario.ativo = ativo
    usuario.save()



if __name__ == '__main__':
    # insere()
    # consulta()
    # altera()
    # exclui()
    # insere_usuario('Bryan', 'jdTExrf97l')
    # insere_usuario('DIO', 'rA7hTEFJ2Z')
    altera_usuario('Bryan', 'jdTExrf97l', True)
    consulta_todos_usuarios()