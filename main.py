from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer,primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    def __repr__(self):
        return f"ID: {self.id} - NOME: {self.nome}"
    
class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer,primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    def __repr__(self):
        return f"ID: {self.id} - CURSO: {self.nome}"
    
    