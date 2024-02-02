import sqlite3
from clientes import Clientes
from lib import dbs

def cadastrar_cliente(nome, senha):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes WHERE nome=?', (nome,))
    existing_client = cursor.fetchone()

    if existing_client is None:
        cliente = Clientes(nome, senha)
        cliente.salvar_no_db()
        return True
    else:
        return False

def fazer_login(nome, senha):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes WHERE nome=? AND senha=?', (nome, senha))
    return cursor.fetchone() is not None
