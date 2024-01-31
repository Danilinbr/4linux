# Crie um script para simular uma lanchonete.
# 
# - Essa lanchonete deverá ter 5 tipos de comida e 3 tipos de bebidas no cardápio.
# - Quando clientes chegarem a essa lanchonete, eles deverão fazer um pedido aleatório de comida + bebida.
# - A lanchonete deverá ter um numero limitado de porções dessas comidas/bebidas. Comida = 5, bebida = 7.
# - Quando o cliente fazer o pedido, ele deverá ser notificado se as opções escolhidas estão disponiveis,
# e quais seus preços.

# Criar um DB.
# Criar uma tabela pra comida e uma pra bebida.
# Preencher essas tabelas.

# Criar uma função pra simular um cliente comprando algo.

import sqlite3 # Criar e gerenciar os bancos de dados.
from random import randint # Usado pra gerar um numero inteiro aleatorio.


conexao = sqlite3.connect("estoque.db") # Cria um banco de dados ou se conecta à ele se ele ja existir.
cursor = conexao.cursor() # Cria um cursor pra editarmos o banco de dados.

# Criamos comandos para a criação das tabelas:
tabela_comida = """
CREATE TABLE comidas (
id integer primary key autoincrement,
nome,
preco,
quantidade
)"""

tabela_bebida = """
CREATE TABLE bebidas (
id integer primary key autoincrement,
nome,
preco,
quantidade
)"""

#Criamos as tabelas, caso elas ainda não existam:
try:
    cursor.execute(tabela_comida)
    cursor.execute(tabela_bebida)

    #Criamos liastas contendo os valores a serem adicionados nas nossas tabelas:
    comidas = [("Hamburger", 25.00, 5), ("HotDog", 12.00, 5), ("Misto quente", 7.50, 5), ("Chocolate", 5.00, 5), ("Pão", 1.50, 5)]
    bebidas = [("Coca cola", 10.00, 7), ("Fanta", 8.00, 7), ("Cerveja", 12.00, 7)]

    #Adicionamos os valores nas tabelas:
    for item in comidas:
        adiciona_item = f"""
    INSERT INTO comidas (nome, preco, quantidade)
    VALUES ("{item[0]}", "{item[1]}", "{item[2]}")"""
        cursor.execute(adiciona_item)

    for item in bebidas:
        adiciona_item = f"""
    INSERT INTO bebidas (nome, preco, quantidade)
    VALUES ("{item[0]}", "{item[1]}", "{item[2]}")"""
        cursor.execute(adiciona_item)

    #Salvamos as alterações feitas:
    conexao.commit()

#Se a tabela já existir, continua a execução:
except sqlite3.OperationalError:
    pass

#Função para checar determinado valor de dentro de determinada tabela:
def checa_tabela(tabela, coluna, id):
    comando_checa_tabela = f"SELECT {coluna} FROM {tabela} WHERE id == {id}"
    cursor.execute(comando_checa_tabela)
    conteudo = cursor.fetchall()
    return(conteudo[0][0])

#Função par atualizar a quantidade de determinado item dentro de determinada tabela:
def atualiza_tabela(tabela, novo_valor, id):
    comando_atualiza_tabela = f'UPDATE {tabela} SET quantidade = {novo_valor} WHERE id = {id}'
    cursor.execute(comando_atualiza_tabela)
    conexao.commit()

#Função para executar um pedido aleatório:
def fazer_pedido():
    pedido_comida = randint(1, 5)
    pedido_bebida = randint(1, 3)

    qtd_comida = int(checa_tabela("comidas", "quantidade", pedido_comida))
    qtd_bebida = int(checa_tabela("bebidas", "quantidade", pedido_bebida))

    preco_comida = float(checa_tabela("comidas", "preco", pedido_comida))
    preco_bebida = float(checa_tabela("bebidas", "preco", pedido_bebida))

    print(f'Os itens escolhidos foram {checa_tabela("comidas", "nome", pedido_comida)} e {checa_tabela("bebidas", "nome", pedido_bebida)}.')

    if int(qtd_comida) > 0 and int(qtd_bebida) > 0:
        atualiza_tabela("comidas", qtd_comida - 1, pedido_comida)
        atualiza_tabela("bebidas", qtd_bebida - 1, pedido_bebida)

        return(f"O valor total da sua compra é de R${preco_bebida + preco_comida}")

    else:
        return("Porém infelizmente o pedido feito não está em estoque.")

#Faemos o pedido:
print(fazer_pedido())
