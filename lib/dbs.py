import sqlite3

class DBMain:
    def __init__(self, db_name='./lib/clientes_db.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def criar_tabelas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                nome TEXT PRIMARY KEY,
                idade INTEGER,
                saldo REAL DEFAULT 0
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                nome TEXT PRIMARY KEY,
                usuario TEXT,
                senha TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()