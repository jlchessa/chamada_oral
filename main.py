""" SANTO DEUS!!!"""
from lista import *

if __name__ == '__main__':
    base = BaseDeDados('base.db')
    base.questionario_aluno("Aluno 1")
    base.questionario_aluno("Aluno 2")
    base.questionario_aluno("Aluno 3")
    base.questionario_aluno("Aluno 4")
    base.listar()
    
