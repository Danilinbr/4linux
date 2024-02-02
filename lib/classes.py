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

class ValidacaoInput(Exception):
    def __init__(self,input_value, message):
        self.input_value = input_value
        super().__init__(f"ValidacaoInput: {message} - Valor informado: {input_value}")

    @staticmethod
    def validar_int(mensagem):
        while True:
            try:
                valor = int(input(mensagem))
                return valor
            except ValueError:
                print("Por favor, digite um valor inteiro válido.")

    @staticmethod
    def validar_float(mensagem):
        while True:
            try:
                valor = float(input(mensagem))
                return valor
            except ValueError:
                print("Por favor, digite um valor numérico válido.")
    
    @staticmethod
    def validar_str(mensagem, validacao):
        while True:
            try:
                valor = input(mensagem)
                if not validacao(valor):
                    raise ValidacaoInput(valor, f"Somente palavras e letras são válidas.")
                return valor
            except ValueError:
                print("Somente palavras e letras são válidas.")
    