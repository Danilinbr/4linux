# # IF - Condição

# idade = int(input("Qual é a sua idade? "))

# if idade ==+ 18:
#     print("Voce é maior de idade.")

# elif idade > 15:
#     print("Voce tem pelo menos 15 anos.")

# elif idade > 10:
#     print("Voce tem pelo menos 10 anos.")

# else:
#     print("Voce tem menos de 10 anos.")


# # FOR / WHILE - Repetição
    
# for numero in range(0, 10):
#     print(numero)


# resposta = "nao"
# while resposta != "sim":
#     print("Imprimindo mensagem do loop")
#     resposta = input("Quer parar o loop? [sim/nao] ")


# while True:
#     resposta = input("Quer parar o loop? [sim/nao] ")
#     if resposta == "sim":
#         break


# # TUPLA / LISTA / DICIONARIO / SET - Coleções
    
# tupla = ("Beterraba", "Mandioca", "Batata", 50, True)
# # INDEX       0            1          2      3    4     

# for cachorro in tupla:
#     print(f"O objeto {cachorro} é um {type(cachorro)}")


# lista = ["Beterraba", "Mandioca", "Batata", 50, True]
# # INDEX       0            1          2      3    4

# lista.append("Pão de batata")
# lista.remove(50)
# lista.pop(0)
# lista.insert(2, "Avião")

# print(lista)


# # Métodos em Strings
# frase = "Testando uma nova frase"
# print(frase.replace("a", "---"))

# # Dicionários - Hash Table

# # chave -> valor

# # dicionario = {"Altura": 1.80}

# # dicionario["Nome"] = "Tiago"
# # dicionario["Cor"] = "Verde"

# #              |------ITEM----|  |----ITEM-----|
# # DICIONARIO = {'Nome': 'Tiago', 'Cor': 'Verde'}
# #               CHAVE  :  VALOR,  CHAVE: VALOR

# # for x, y in dicionario.items():
# #     print(f"Chave: {x}, Valor: {y}")


# # SETS
    
# # variavel = {10, 15, 30, "teste", 15}
# # variavel.add(20)

# # print(variavel)


# # FUNÇÕES

# # print("imprimir")
# # soma(4, 5)

# # def soma(x, y):
# #     resultado = x + y
# #     return resultado


# # print(soma(4, 7))
# # print(soma(10, 23))
# # print(soma(70, 1))


# # Funções LAMBDA / Funções Anonimas

# # diferenca = lambda x, y: x - y

# # print(diferenca(7, 5))

# # Módulos

# # Modulos nativos
# import os
# os.system()
# from os import system
# system()

# # Modulos baixados através do pip
# from flask import Request
# import pandas

# # Modulos de terceiros
# import arquivo_baixado
# arquivo_baixado.funcoes()

# # =============================================

# import random

# random.choice()
# random.random(1, 100)
# random.randint(1, 100)

# =============================================
# Manipulação de arquivos

# r -> READ   -> Leitura
# w -> WRITE  -> Escrita (SOBRESCREVE)
# a -> APPEND -> Anexar
# + -> Leitura e escrita

# arquivo = open("texto.txt", "a")

# conteudo = "\nQuarta linha do arquivo de texto"

# arquivo.write(conteudo)

# arquivo.close()

#====================================================
# arquivo = open("texto.txt", "r")

# conteudo = arquivo.readlines()
# for linha in conteudo:
#     print(linha, end="")

# arquivo.close()

# Arquivos .csv

import csv

# arquivo = open("registro.csv",'a')

# with open("/mnt/e/My_Git/4Linux_Git/4linux/registro.csv",'r') as arquivo:
#     conteudo = []
#     reader = csv.reader(arquivo, delimiter=';')
#     for lines in reader:
#         conteudo.append(lines)
#     for linha in conteudo:
#         print(linha)

# with open("/mnt/e/My_Git/4Linux_Git/4linux/registro.csv",'w') as arquivo:
#     conteudo = []
#     writer = csv.writer(arquivo, delimiter=';')
#     for lines in writer:
#         conteudo.append(lines)
#     for linha in conteudo:
#         print(linha)

with open("registro.csv", "r") as arquivo:
    conteudo = csv.reader(arquivo, delimiter=";")
    # cabeçalho = next(conteudo)
    # primeira_linha = next(conteudo)
    # segunda_linha = next(conteudo)
    # terceira_linha = next(conteudo)

    lista_conteudo = []

    for linha in conteudo:
        lista_conteudo.append(linha)

    for linha in lista_conteudo:
        print(linha)

with open("registro.csv", "a+", newline="") as arquivo:
    escrita = csv.writer(arquivo, delimiter=";")

    escrita.writerow(["444444444", "Tiago P", 27, "M", "Brasileiro"])
# AULA 06 -------------------------------------------
# Class / Classes
# Crie uma classe pra simular uma pilha, onde itens só podem ser removidos do topo.

class Pilha:

    def __init__(self):
        self.pilha = []
        self.__topo = 0

    def empilhar(self, item):
        self.pilha.append(item)
        self.__topo += 1

    def desempilhar(self):
        if self.__topo > 0:
            ultimo_item = self.pilha[-1]
            self.pilha.remove(ultimo_item)
            self.__topo -= 1
            return "Item removido"
        else:
            return "Nenhum item empilhado"
        
    def checar(self):
        return self.pilha
        
balcao = Pilha()
print(balcao.pilha)

balcao.empilhar("Prato de vidro verde")
balcao.empilhar("Prato de porcelana azul")
balcao.empilhar("Prato de metal")
balcao.empilhar("Prato de madeira")

balcao.desempilhar()
balcao.desempilhar()

# Encapsulamento

print(balcao.checar())

# Herança

class Funcionario:

    def __init__(self):
        self.__nome = ""
        self.__idade = 0
        self.__salario = 0



class Gerentes(Funcionario):

    def __init__(self):
        super().init__()
        self.__bonus = "25%"


# Polimorfismo
class Cliente:

    def __init__(self):
        self.carrinho = []
        self.cpf = ''
        self.total = 0

    def adicionar_item(self, item):
        self.carrinho.append(item)

    def caixa(self):
        for item in self.carrinho:
            self.total += 1.99
        return self.total
    
class ClienteVIP(Cliente):

    def __init__(self):
        super().__init__()
        self.desconto = 0.95

    def caixa(self):
        for item in self.carrinho:
            self.total += 1.99
        return self.total * self.desconto
