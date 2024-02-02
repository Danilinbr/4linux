import sqlite3

conn = sqlite3.connect('./lib/clientes_db.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        nome TEXT PRIMARY KEY,
        saldo REAL DEFAULT 0
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_pass (
        nome TEXT PRIMARY KEY,
        senha TEXT NOT NULL
    )
''')

conn.commit()

#===============================================================#
