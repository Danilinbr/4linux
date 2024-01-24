# # Exercícios - Aula 03
import os as os
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
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def calc(num1,num2,oper):
    os.system('clear')
    match oper:
        case 1:
            return num1 + num2
        case 2:
            if (num1 > num2):
                return num1-num2
            else:
                return num2-num1
        case 3:
            return num1*num2
        case 4:
            return num1/num2
        case 5:
            exit()

def panel():
    oper = 0
    num1 = 0
    num2 = 0
    print("""
    Escolha uma operação:
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Sair
          
    """)
    oper = input("R: ")
    if oper.isdigit() != True:
        os.system('clear')
        print("Escolha uma opção valida!")
        input("")
        return
    else:
        oper = int(oper)
        if oper == 5:
            exit()
        while True:
            os.system('clear')
            num1 = float(input("Escolha o primeiro valor:\nR: "))
            if isfloat(num1) != True:
                os.system('clear')
                print("Escolha uma opção valida!")
                input("")
            else:
                break
        while True:
            os.system('clear')
            num2 = float(input("Escolha o segundo valor:\nR: "))
            if isfloat(num2) != True:
                os.system('clear')
                print("Escolha uma opção valida!")
                input("")
            else:
                break
        value = calc(num1,num2,oper)
        print (f"O resultado da sua operação é:\n{value}")
        input("")
    
def main():
    while True:
        os.system('clear')
        panel()

if __name__ == '__main__':
    main()

#---------------------------------------------------------------------
# ## Exercício 3:

# Reescreva o exercício da quitanda do capítulo 2 separando as operações em funções.
#---------------------------------------------------------------------
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
