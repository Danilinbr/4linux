# # Exercícios - Aula 03

# ## Exercício 1:
# Escreva uma função que receba um nome e que tenha como saída uma saudação. O argumento da função deverá ser o nome e a saída deverá ser como a seguir:

# ```
# chamada da função: saudacao('Lalo')
# saída: 'Olá Lalo! Tudo bem com você?'
# ```
#_____________________________________________________________________________
#!/usr/bin/python3

operacoes = {
    '1': lambda x,y: x+y,
    '2': lambda x,y: x-y,
    '3': lambda x,y: x/y if y != 0 else 'Não dividirás por zero.',
    '4': lambda x,y: x*y,
    '5': lambda x,y: exit()
}


def calculadora():
    while True:
        n1=float(input('N1: '))
        n2=float(input('N2: '))

        op = input(f'Operações:\n' \
             f'1 - Soma\n' \
             f'2 - Subtração\n' \
             f'3 - Divisão\n' \
             f'4 - Multiplicação\n'
             f'5 - Sair\n' \
             f'Digite a opção desejada: ')


        if op in operacoes:
            print(operacoes[op](n1,n2))
        else:
            print('Opção inválida')


if __name__ == '__main__':
    calculadora()
# ## Exercício 2:

# Escreva uma calculadora matemática utilizando funções anônimas


# ## Exercício 3:

# Reescreva o exercício da quitanda do capítulo 2 separando as operações em funções.

#!/usr/bin/python3

def saudacao(nome):
    return f'Olá {nome}, tudo bem com você?'

print(saudacao('Lalo'))


#---------------------------------------------------------------------
#!/usr/bin/python3

cesta = []

frutas = {
  '1': 'Banana',
  '2': 'Melancia',
  '3': 'Morango'
}

precos = {
  'Banana' : 3.50,
  'Melancia' : 7.50,
  'Morango': 5.00

}

def ver_cesta(lista_compras):
    if not esta_vazia(lista_compras):
        print('Cesta de Compras:')
        for item in cesta:
            print(item)
    else:
        print('Cesta de compras está vazia.')
    print('------------------------')

def adicionar_frutas(cesta_frutas):
    fruta = escolher_fruta()
    if fruta in frutas:
        cesta_frutas.append(frutas[fruta])
        print(f'{frutas[fruta]} foi adicionado com sucesso!')
        print('------------------------')

    else:
        print('Opção inválida')
        print('------------------------')


def escolher_fruta():
    return input(f'Escolha a fruta desejada:\n' \
                 f'1 - Banana\n' \
                 f'2 - Melancia\n' \
                 f'3 - Morango\n' \
                 f'Digite a opção desejada: ')

def checkout(cesta_frutas):
    if not esta_vazia(cesta_frutas):
        total = totalizar_precos(cesta_frutas)

        print(f'Total de compras: {total}')
        print(f'Cesta de compras: {cesta_frutas}')
    else:
        print('Cesta de compras vazia.')
    print('------------------------')


def esta_vazia(cesta_frutas):
    return len(cesta_frutas) == 0

def totalizar_precos(cesta_frutas):
    total = 0
    for item in cesta_frutas:
        total += precos[item]
    return total



def sair(*args):
    exit()


def main():
    while True:
        print(f'Quitanda\n' \
              f'1: Ver cesta\n' \
              f'2: Adicionar Frutas\n' \
              f'3: Checkout\n' \
              f'4: Sair\n')

        op = input('Digite a opção desejada: ')

        if op == '1':
            ver_cesta(cesta)
        elif op == '2':
            adicionar_frutas(cesta)
        elif op == '3':
            checkout(cesta)
        elif op == '4':
            sair()
        else:
            print('Opção Inválida')


if __name__ == '__main__':
    main()
