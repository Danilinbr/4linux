# # Exercícios - Aula 05
# 1) Escreva um programa em python que conte as vogais que a música ‘Faroeste Caboclo’
# tem em sua letra. Armazena a letra da música em um arquivo do tipo txt.
# Dica: Não se esqueça de considerar as letras maiúsculas, minúsculas e com acentuação.
# def contar_vogais(letra):
#     vogais = "aeiouáéíóúãõâêîôûàèìòùäëïöü"
#     contador = 0

#     for char in letra:
#         if char.lower() in vogais:
#             contador += 1

#     return contador

# def main():
#     with open("faroeste.txt", "r", encoding="utf-8") as arquivo:
#         letra_musica = arquivo.read()
        
#     qtd_vogais = contar_vogais(letra_musica)

#     print(f"A letra da música tem {qtd_vogais} vogais.")

# if __name__ == "__main__":
#     main()

# ====================================================================================
# 2) Escreva um programa em python que realize um cadastro. Deverão ser coletadas as
# seguintes informações:

# CPF
# Nome
# Idade
# Sexo
# Endereço

# Os registros deverão ser armazenados em um arquivo CSV. Caso desejar manter o padrão
# brasileiro, o CSV será separado pelo caractere ;
# ====================================================================================
import csv
import os
import sys
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_inicial():
    print("""Qual operação deseja fazer?
1 - Cadastrar usuario.
2 - Consultar usuario cadastrado.
3 - Excluir cadastro.
4 - Sair
""")
    
def painel(prompt, opts):
    while True:

        try:
            opt = int(input(f"{prompt}"))
            if opt in opts:
                return opt
            else:
                print("Opção invalida!")
                time.sleep(1)
                limpar_tela()
                display_inicial()
        except ValueError:
            limpar_tela()
            print("Digite o numero da opção!")
            time.sleep(1)
            limpar_tela()
            display_inicial()

def realizar_cadastro():
    limpar_tela()
    while True:
        cpf_ini = input("Digite o CPF: ")
        cpf_exist = f"{cpf_ini[:3]}.{cpf_ini[3:6]}.{cpf_ini[6:9]}/{cpf_ini[9:]}"
        retn = consultar_existencia(cpf_exist)
        match retn:
            case 1:
                limpar_tela()
                print("CPF ja cadastrado! retornando ao menu!")
                time.sleep(3)
                return
            case 2:
                break
    nome = input("\nDigite o Nome: ")
    idade = input("\nDigite a Idade: ")
    sexo = input("\nDigite o Sexo: ")
    endereco = input("\nDigite o Endereço: ")

    cpf_format = f"{cpf_ini[:3]}.{cpf_ini[3:6]}.{cpf_ini[6:9]}/{cpf_ini[9:]}"
    cadastro = {"CPF": cpf_format, "Nome": nome, "Idade": idade, "Sexo": sexo, "Endereço": endereco}

    with open("cadastro.csv", "a", newline="", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=["CPF", "Nome", "Idade", "Sexo", "Endereço"], delimiter=";")
        if arquivo.tell() == 0:
            writer.writeheader()
        writer.writerow(cadastro)

    limpar_tela()
    print("Cadastro realizado com sucesso!")
    time.sleep(2)




# ====================================================================================
# 3) Implemente uma função de consulta no programa do exercício 2.
def consultar_existencia(cpf_consulta):
    with open("cadastro.csv", "r", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo, delimiter=";")
        
        for linha in reader:
            if linha["CPF"] == cpf_consulta:
                return 1
        
        return 2

def consultar_cadastro(cpf_consulta):
    limpar_tela()
    with open("cadastro.csv", "r", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo, delimiter=";")
        
        for linha in reader:
            if linha["CPF"] == cpf_consulta:
                print(f"CPF: {linha['CPF']}")
                print(f"Nome: {linha['Nome']}")
                print(f"Idade: {linha['Idade']}")
                print(f"Sexo: {linha['Sexo']}")
                print(f"Endereço: {linha['Endereço']}")
                input("\nAperte qualquer tela para voltar!")
                return
        limpar_tela()
        print("CPF não encontrado.")
        time.sleep(2)

# ====================================================================================
# 4) Implemente uma função de exclusão no programa do exercício 2.
        
def excluir_cadastro(cpf_exclusao):
    with open("cadastro.csv", "r", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo, delimiter=";")
        cadastros = list(reader)

    encontrado = False
    for cadastro in cadastros:
        if cadastro["CPF"] == cpf_exclusao:
            encontrado = True
            cadastros.remove(cadastro)
            break

    if encontrado:
        with open("cadastro.csv", "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=["CPF", "Nome", "Idade", "Sexo", "Endereço"], delimiter=";")
            writer.writeheader()
            writer.writerows(cadastros)

        limpar_tela()
        print("Cadastro excluído com sucesso.")
        time.sleep(2)
    else:
        limpar_tela()
        print("CPF não encontrado para exclusão.")
        time.sleep(2)
#==========
    # MAIN
#==========

def main():

    while True:
        limpar_tela()
        display_inicial()
        opt = painel("Digite a opção desejada: ", [1, 2, 3, 4])

        match opt:
            case 1:
                realizar_cadastro()
            case 2:
                limpar_tela()
                cpf_ini = input("Digite o CPF para consulta: ")
                cpf_consulta = f"{cpf_ini[:3]}.{cpf_ini[3:6]}.{cpf_ini[6:9]}/{cpf_ini[9:]}"
                consultar_cadastro(cpf_consulta)
            case 3:
                limpar_tela()
                cpf_ini = input("Digite o CPF para exclusão: ")
                cpf_exclusao = f"{cpf_ini[:3]}.{cpf_ini[3:6]}.{cpf_ini[6:9]}/{cpf_ini[9:]}"
                excluir_cadastro(cpf_exclusao)
            case 4:
                limpar_tela()
                print("Terminando o programa de cadastro. Obrigado!")
                time.sleep(2)
                sys.exit()
        limpar_tela()

if __name__ == "__main__":
    main()