from models import Pessoas, db_session

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

if __name__ == '__main__':
    # insere()
    consulta()
    # altera()
    # exclui()