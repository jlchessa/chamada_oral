"""SANTO SANTO SANTO!!!"""

import random
import sqlite3


verbs_list = ['Andar', 'amar', 'bater', 'brincar', 'correr', 'ser', 'ir', 'gostar', 'odiar', 'lavar a louça',
              'lavar a roupa', 'escrever', 'ler', 'escutar', 'tocar', 'jogar', 'estudar', 'beber', 'comer','entender',
              'fazer', 'falar', 'conversar', 'cozinhar', 'trabalhar', 'dançar', 'parar', 'ter', 'cantar', 'comprar',
              'chorar', 'ligar', 'assistir', 'consertar', 'lavar', 'pular', 'acreditar', 'beijar', 'matar',
              'lutar', 'copiar', 'curtir', 'desenhar', 'morder']



class BaseDeDados:

    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def questionario_aluno(self, nome):
        nome = nome
        print(nome)
        verbo = random.choices(verbs_list, k=5)
        print(f'os verbos selecionados foram: {verbo}')
        nota = int(input(f'Quantos verbos o {nome} acertou? '))
        print(f'A nota do {nome} foi {nota}')
        
        self.cursor.execute('CREATE TABLE IF NOT EXISTS notas ('
                    'id INTEGER PRIMARY KEY,'
                    'nome TEXT,'
                    'nota INTEGER'
                    ')')
        consulta = (f'INSERT OR IGNORE INTO notas (nome, nota) VALUES (?, ?)')
        self.cursor.execute(consulta, (nome, nota))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM notas')

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()



