# # Exercícios - Aula 03
import os as os
import pandas
# ## Exercício 1:
# Escreva uma função que receba um nome e que tenha como saída uma saudação. O argumento da função deverá ser o nome e a saída deverá ser como a seguir:

# ```
# chamada da função: saudacao('Lalo')
# saída: 'Olá Lalo! Tudo bem com você?'
# ```
#---------------------------------------------------------------------

# def saudacao(nome):
#     return f"Olá {nome}, tudo bem com você?"

# def main():
#     print(saudacao('Lalo'))

# if __name__ == '__main__':
#     main()
#---------------------------------------------------------------------
# ## Exercício 2:

# Escreva uma calculadora matemática utilizando funções anônimas
# def isfloat(num):
#     try:
#         float(num)
#         return True
#     except ValueError:
#         return False

# def calc(num1,num2,oper):
#     os.system('clear')
#     match oper:
#         case 1:
#             return num1 + num2
#         case 2:
#             if (num1 > num2):
#                 return num1-num2
#             else:
#                 return num2-num1
#         case 3:
#             return num1*num2
#         case 4:
#             return num1/num2
#         case 5:
#             exit()

# def panel():
#     oper = 0
#     num1 = 0
#     num2 = 0
#     print("""
#     Escolha uma operação:
#     1 - Soma
#     2 - Subtração
#     3 - Multiplicação
#     4 - Divisão
#     5 - Sair

#     """)
#     oper = input("R: ")
#     if oper.isdigit() != True:
#         os.system('clear')
#         print("Escolha uma opção valida!")
#         input("")
#         return
#     else:
#         oper = int(oper)
#         if oper == 5:
#             exit()
#         while True:
#             os.system('clear')
#             num1 = float(input("Escolha o primeiro valor:\nR: "))
#             if isfloat(num1) != True:
#                 os.system('clear')
#                 print("Escolha uma opção valida!")
#                 input("")
#             else:
#                 break
#         while True:
#             os.system('clear')
#             num2 = float(input("Escolha o segundo valor:\nR: "))
#             if isfloat(num2) != True:
#                 os.system('clear')
#                 print("Escolha uma opção valida!")
#                 input("")
#             else:
#                 break
#         value = calc(num1,num2,oper)
#         print (f"O resultado da sua operação é:\n{value}")
#         input("")

# def main():
#     while True:
#         os.system('clear')
#         panel()

# if __name__ == '__main__':
#     main()

#---------------------------------------------------------------------
# ## Exercício 3:

# Reescreva o exercício da quitanda do capítulo 2 separando as operações em funções.
#---------------------------------------------------------------------
# cesta_frutas = []
# preco_cesta = []
# preco_total = 0

# def painel():
#     while True:
#         os.system('clear')
#         quitanda = input("QUITANDA\n1: Ver cesta\n2: Adicionar frutas\n3: Sair\nR: ")
#         if quitanda.isdigit() != True:
#             os.system('clear')
#             print("\nEscolha uma opção valida!\n")
#             input("")
#         else:
#             return int(quitanda)

# while True:
#     index = len(cesta_frutas)
#     quitanda_UI = painel()
#     if quitanda_UI == 1:
#         os.system('clear')
#         if index < 1:
#             print("Cesta Vazia")
#             input("")
#         else:
#             for itens in cesta_frutas:
#                 print(itens)
#             input("")

#     elif quitanda_UI == 2:
#         os.system('clear')
#         adicionar_frutas = int(input("""Escolha a fruta desejada:
# 1 - Banana - R$1
# 2 - Melancia - R$5
# 3 - Morango - R$2,5
# Digite a opção desejada:\nR: """))
#         if adicionar_frutas == 1:
#             cesta_frutas.append("Banana")
#             preco_cesta.append(1)
#             os.system('clear')
#             print("\nOpção Adicionada ao carrinho!\n")
#             input("")
#         elif adicionar_frutas == 2:
#             cesta_frutas.append("Melancia")
#             preco_cesta.append(5)
#             os.system('clear')
#             print("\nOpção Adicionada ao carrinho!\n")
#             input("")
#         elif adicionar_frutas == 3:
#             cesta_frutas.append("Morango")
#             preco_cesta.append(2.5)
#             os.system('clear')
#             print("\nOpção Adicionada ao carrinho!\n")
#             input("")
#         else:
#             os.system('clear')
#             print("\nopção invalida!\n")
#             input("")

#     elif quitanda_UI == 3:
#         for preco in preco_cesta:
#             preco_total = preco_total+preco
#         os.system('clear')
#         print(f"\n Compra ficou em R${preco_total}! Obrigado.\n")
#         input("")
#         break
#     else:
#         None
# ====================================================
# Exercicio 4:
# Escreva um programa que possua uma função que conte o
# numero de números pares passados à ela, pelo usuário.
# ====================================================
# def ui_exe4(num_list):
#     while True:
#         os.system('clear')
#         ui_inpt = input("""
# Escolha dentre as opções:
# 1 - Adicionar Numero à lista
# 2 - Visualizar numeros pares na lista
# 3 - Sair

# """)
#         if ui_inpt.isdigit() != True:
#             os.system('clear')
#             print("\nEscolha uma opção valida! Somente numero.\n")
#             input("")
#         else:
#             ui_inpt = int(ui_inpt)
#             choose(ui_inpt,num_list)


# def choose(inpt,num_list):
#     par_list = []
#     os.system('clear')
#     match inpt:
#         case 1:
#             while True:
#                 opt = input("Qual numero deseja adicionar a lista\nR: ")
#                 if opt.isdigit() != True:
#                     os.system('clear')
#                     print("\nEscolha uma opção valida! Somente numero.\n")
#                     input("")
#                 else:
#                     opt = int(opt)
#                     num_list.append(opt)
#                     return num_list
#         case 2:
#             if len(num_list) == 0:
#                 print("lista vazia")
#                 input("")
#                 return num_list
#             else:
#                 cont = 0
#                 for itens in num_list:
#                     if itens % 2 == 0:
#                         cont += 1
#                         par_list.append(itens)
#                 os.system('clear')
#                 print(f"Você possui um total de {cont} numeros pares em sua lista.\n eles são: {par_list}")
#                 input("")
#                 return num_list
#         case 3:
#             exit()

# def main():
#     num_list = []
#     ui_exe4(num_list)

# if __name__ == '__main__':
#      main()
# ====================================================
# Exercicio 5:
# Assumindo que uma lata de tinta pinta 3m², escreva um programa
# que possua uma função que receba as dimenções de uma parede,
# passadas pelo usuario, calcule sua área, e mostre uma mensagem
# dizendo quantas latas de tinta seriam necessárias para pintar
# essa parede.
# ====================================================
def tinta_calc(lar, alt):
    area = lar * alt
    qtd_latas = area / 3
    return qtd_latas

lar = input("Digite a largura da parede em metros: ")
alt = input("Digite a altura da parede em metros: ")

lar = float(lar.replace(',', '.'))
alt = float(alt.replace(',', '.'))

latas = tinta_calc(lar, alt)
print(f"São necessárias {latas:.2f} latas de tinta para pintar a parede.")

# ====================================================