# Reescreva o exercicio 4 da aula 05 adicionando tratamentos de erro, 
# com a finalidade de que o programa nunca dê uma exceção e também que ele
# não aceite dados incorretos em nenhum momento.

import csv
import os
import sys
import time

class NaoEsperado(Exception):
    def __init__(self,input_value, message):
        self.input_value = input_value
        super().__init__(f"NaoEsperado: {message} - Valor informado: {input_value}")

    
def obter_input(msg, err_msg, req_msg, tipo, validacao):
    while True:
        try:
            entrada = tipo(input(msg))

            if not validacao(entrada):
                raise NaoEsperado(entrada, f"info: '{err_msg}' - inválido(a). Requisitos: {req_msg}")
            else:
                return entrada
        except NaoEsperado as erro:
            print(erro)

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
        cpf_ini = obter_input("Digite o CPF (11 digitos): ","CPF","11 digitos numéricos.", str, lambda x: len(x) == 11 and x.isdigit())
        cpf_format = f"{cpf_ini[:3]}.{cpf_ini[3:6]}.{cpf_ini[6:9]}/{cpf_ini[9:]}"
        retn = consultar_existencia(cpf_format)
        match retn:
            case 1:
                limpar_tela()
                print("CPF ja cadastrado! retornando ao menu!")
                time.sleep(3)
                return
            case 2:
                break
    nome = obter_input("\nDigite o Nome: ","Nome","Somente Letras.", str,lambda x: isinstance(x, str))
    idade = obter_input("\nDigite a Idade: ","Idade","Somente Numeros", int,lambda x: isinstance(x, int))
    sexo = obter_input("\nDigite o Sexo: ","Sexo","Somente as letras 'M' ou 'F", str.upper,lambda x: (x.upper() == 'M' or x.upper() == 'F') and isinstance(x, str))
    endereco = obter_input("\nDigite o Endereço: ","Endereço","Numero de caracteres menor que 300 ", str,lambda x: len(x) < 300)

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