import sqlite3

#============================================#
#Infos sobre cliente#
#============================================#
class Clientes:
    def __init__(self, nome, senha, saldo=0):
        self.nome = nome
        self.senha = senha
        self.saldo = saldo

    def salvar_no_db(self):
        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO clientes (nome, senha, saldo)
            VALUES (?, ?, ?)
        ''', (self.nome, self.senha, self.saldo))
        conn.commit()

#============================================#
#Usuario e senha em outra tabela             #
#============================================#
    def salvar_no_db(self):
        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO clientes (nome, senha, saldo)
            VALUES (?, ?, ?)
        ''', (self.nome, self.senha, self.saldo))
        conn.commit()
