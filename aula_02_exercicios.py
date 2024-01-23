import os as os
# 1) Escreva um script em Python que substitua o caractere “x” por espaço considerando a
# seguinte frase:
# “Umxpratoxdextrigoxparaxtrêsxtigresxtristes”
# ======================================================================================================
frase = "Umxpratoxdextrigoxparaxtrêsxtigresxtristes"
frase = frase.replace("x"," ")

print(frase)
input("")
os.system('clear')

# ======================================================================================================
# 2) Escreva um programa que receba o ano de nascimento, e que ele retorne à geração
# a qual a pessoa pertence. Para definir a qual geração uma pessoa pertence temos a
# seguinte tabela:

# Geração        Intervalo

# Baby Boomer -> Até 1964
# Geração X   -> 1965 - 1979
# Geração Y   -> 1980 - 1994
# Geração Z   -> 1995 - Atual

# Para testar se seu script está funcionando, considere os seguintes resultados esperados:

# • ano nascimento = 1988: Geração: Y
# • ano nascimento = 1958: Geração: Baby Boomer
# • ano nascimento = 1996: Geração: Z
# ======================================================================================================
nasc = int(input("Escreva o ano em que você nasceu:\n"))

if nasc <= 1964:
     print("Geração Baby boomer")
elif nasc >= 1965 and nasc <= 1979:
     print("Geração X")
elif nasc >= 1980 and nasc <= 1994:
     print("Geração Y")
elif nasc >= 1995:
     print("Geração Z")

input("")
os.system('clear')

# ======================================================================================================
# 3) Escreva um script em python que represente uma quitanda. O seu programa deverá
# apresentar as opções de frutas, e a cada vez que você escolher a fruta desejada, a fruta
# deverá ser adicionada a uma cesta de compras.

# Menu principal:

# Quitanda:
# 1: Ver cesta
# 2: Adicionar frutas
# 3: Sair

# Menu de frutas:
# Digite a opção desejada:
# Escolha fruta desejada:
# 1 - Banana
# 2 - Melancia
# 3 - Morango

# Digite à opção desejada: 2
# Melancia adicionada com sucesso!

# Os menus 1 e 2 deverão retornar ao menu principal após executar as suas tarefas.
# Você deverá validar as opções digitadas pelo usuário (caso ele digitar algo errado, a mensagem:
# Digitado uma opção inválida

# O programa deverá ser encerrado apenas se o usuário digitar a opção 3.
# ======================================================================================================
# cesta_frutas = []
# while True:
#     index = len(cesta_frutas)
#     input("")
#     os.system('clear')
#     quitanda_UI = int(input("QUITANDA\n1: Ver cesta\n2: Adicionar frutas\n3: Sair\nR: "))
#     if quitanda_UI == 1:
#         if index < 1:
#             print("Cesta Vazia")
#         else:
#             for itens in cesta_frutas:
#                 print(itens)
#     elif quitanda_UI == 2:
#         os.system('clear')
#         adicionar_frutas = int(input("""Escolha a fruta desejada:
# 1 - Banana
# 2 - Melancia
# 3 - Morango
# Digite a opção desejada:\n"""))
#         if adicionar_frutas == 1:
#             cesta_frutas.append("Banana")
#         elif adicionar_frutas == 2:
#             cesta_frutas.append("Melancia")
#         elif adicionar_frutas == 3:
#             cesta_frutas.append("Morango")
#         else:
#             print("\nopção invalida!\n")
#     elif quitanda_UI == 3:
#         break
#     else:
#         print("\nEscolha uma opção valida!\n")
#         quitanda_UI = 0

# ======================================================================================================
# 4) Altere o exercicio numero 3 para adicionar o preço dos itens comprados, mantendo uma conta do valor
# total gasto nas compras, e no fim, imprima o valor total e os itens na cesta de compras.
cesta_frutas = []
preco_cesta = []
preco_total = 0
while True:
    index = len(cesta_frutas)
    os.system('clear')
    quitanda_UI = int(input("QUITANDA\n1: Ver cesta\n2: Adicionar frutas\n3: Sair\nR: "))
    if quitanda_UI == 1:
        os.system('clear')
        if index < 1:
            print("Cesta Vazia")
            input("")
        else:
            for itens in cesta_frutas:
                print(itens)
            input("")

    elif quitanda_UI == 2:
        os.system('clear')
        adicionar_frutas = int(input("""Escolha a fruta desejada:
1 - Banana - R$1
2 - Melancia - R$5
3 - Morango - R$2,5
Digite a opção desejada:\nR: """))
        if adicionar_frutas == 1:
            cesta_frutas.append("Banana")
            preco_cesta.append(1)
            os.system('clear')
            print("\nOpção Adicionada ao carrinho!\n")
            input("")
        elif adicionar_frutas == 2:
            cesta_frutas.append("Melancia")
            preco_cesta.append(5)
            os.system('clear')
            print("\nOpção Adicionada ao carrinho!\n")
            input("")
        elif adicionar_frutas == 3:
            cesta_frutas.append("Morango")
            preco_cesta.append(2.5)
            os.system('clear')
            print("\nOpção Adicionada ao carrinho!\n")
            input("")
        else:
            os.system('clear')
            print("\nopção invalida!\n")
            input("")
        
    elif quitanda_UI == 3:
        for preco in preco_cesta:
            preco_total = preco_total+preco
        os.system('clear')
        print(f"\n Compra ficou em R${preco_total}! Obrigado.\n")
        input("")
        break
    else:
        print("\nEscolha uma opção valida!\n")
        quitanda_UI = 0

