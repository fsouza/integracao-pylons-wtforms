"""The application's model objects"""
from wtforms_pylons_academico.model.meta import Session, metadata
import sqlalchemy as sa
from sqlalchemy import orm

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

aluno_table = sa.Table('alunos', metadata,
                        sa.Column('id', sa.Integer, primary_key = True),
                        sa.Column('nome', sa.String(100), nullable = False),
                        sa.Column('data_nascimento', sa.Date, nullable = False))

class Aluno(object):
    """docstring for Aluno"""
    def __init__(self, nome = None, data_nascimento = None):
        super(Aluno, self).__init__()
        self.nome = nome
        self.data_nascimento = data_nascimento

orm.mapper(Aluno, aluno_table)
