from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Programador(Base):
    __tablename__ = 'programador'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    email = Column(String)
    habilidades = relationship("ProgramadorHabilidade", back_populates="programador")

class Habilidade(Base):
    __tablename__ = 'habilidade'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    programadores = relationship("ProgramadorHabilidade", back_populates="habilidade")

class ProgramadorHabilidade(Base):
    __tablename__ = 'programador_habilidade'
    id = Column(Integer, primary_key=True)
    programador_id = Column(Integer, ForeignKey('programador.id'))
    habilidade_id = Column(Integer, ForeignKey('habilidade.id'))
    programador = relationship("Programador", back_populates="habilidades")
    habilidade = relationship("Habilidade", back_populates="programadores")


engine = create_engine('sqlite:///banco_de_dados.db')
Base.metadata.create_all(engine)
