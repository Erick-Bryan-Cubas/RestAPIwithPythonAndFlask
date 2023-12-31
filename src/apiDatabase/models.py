""" 
Arquivo de configuração do banco de dados
"""

from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///atividades.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                            bind=engine))


Base = declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__ = 'pessoas' #nome da tabela
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True) #nome da coluna
    idade = Column(Integer)

    def __repr__(self):
        return '<Pessoa {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()
    
    def delete(self):
        db_session.delete(self)
        db_session.commit()
        
class Atividades(Base):
    __tablename__ = 'atividades' #nome da tabela
    id = Column(Integer, primary_key=True)
    nome = Column(String(80)) #nome da coluna
    status = Column(String(20), default='pendente')  #status da atividade
    pessoa_id = Column(Integer, ForeignKey('pessoas.id')) #chave estrangeira
    pessoa = relationship("Pessoas") #relacionamento com a tabela pessoas
    
    def __repr__(self):
        return '<Atividade {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()
    
    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Usuarios(Base):
    __tablename__ = 'usuarios' #nome da tabela
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True) #nome da coluna
    senha = Column(String(20)) #senha do usuário
    ativo = Column(Boolean, default=True) #usuário ativo ou não
    
    def __repr__(self):
        return '<Usuario {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()
    
    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine) #cria o banco de dados
    
if __name__ == '__main__':
    init_db()