from dbs import DBMain
from classes import ValidacaoInput

def registrar_cliente(nome, idade, saldo, usuario, senha):
    db = DBMain()
    db.criar_tabelas()

    db.cursor.execute("SELECT * FROM clientes WHERE nome=?", (nome,))
    if db.cursor.fetchone() is not None:
        db.fechar_conexao()
        return "Cliente já registrado."

    db.cursor.execute("INSERT INTO clientes VALUES (?, ?, ?)", (nome, idade, saldo))

    db.cursor.execute("INSERT INTO usuarios VALUES (?, ?, ?)", (nome, usuario, senha))

    db.conn.commit()
    db.fechar_conexao()
    return "Cliente registrado com sucesso."

def realizar_deposito(nome, valor):
    db = DBMain()
    db.criar_tabelas()

    db.cursor.execute("SELECT * FROM clientes WHERE nome=?", (nome,))
    cliente = db.cursor.fetchone()

    if cliente is not None:
        novo_saldo = cliente[2] + valor
        db.cursor.execute("UPDATE clientes SET saldo=? WHERE nome=?", (novo_saldo, nome))
        db.conn.commit()
        db.fechar_conexao()
        return f"Depósito de R${valor} realizado. Novo saldo: R${novo_saldo}."
    else:
        db.fechar_conexao()
        return "Cliente não encontrado."

def realizar_saque(nome, valor): 
    db = DBMain()
    db.criar_tabelas()

    db.cursor.execute("SELECT * FROM clientes WHERE nome=?", (nome,))
    cliente = db.cursor.fetchone()

    if cliente is not None:
        if cliente[2] >= valor:
            novo_saldo = cliente[2] - valor
            db.cursor.execute("UPDATE clientes SET saldo=? WHERE nome=?", (novo_saldo, nome))
            db.conn.commit()
            db.fechar_conexao()
            return f"Saque de R${valor} realizado. Novo saldo: R${novo_saldo}."
        else:
            db.fechar_conexao()
            return "Saldo insuficiente."
    else:
        db.fechar_conexao()
        return "Cliente não encontrado."
    
def verificar_cliente(nome):
    db = DBMain()
    db.criar_tabelas()
    db.cursor.execute("SELECT nome, saldo FROM clientes WHERE nome=?", (nome,))
    cliente = db.cursor.fetchone() 
    db.fechar_conexao()
    return cliente

def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')