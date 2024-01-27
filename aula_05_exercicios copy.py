import csv

def realizar_cadastro():
    # Coleta de informações
    cpf = input("Digite o CPF: ")
    nome = input("Digite o Nome: ")
    idade = input("Digite a Idade: ")
    sexo = input("Digite o Sexo: ")
    endereco = input("Digite o Endereço: ")

    # Criando um dicionário com as informações
    cadastro = {"CPF": cpf, "Nome": nome, "Idade": idade, "Sexo": sexo, "Endereço": endereco}

    # Escrevendo no arquivo CSV
    with open("cadastro.csv", "a", newline="", encoding="utf-8") as arquivo_csv:
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=["CPF", "Nome", "Idade", "Sexo", "Endereço"], delimiter=";")
        
        # Verifica se o arquivo já existe, se não, escreve os cabeçalhos
        if arquivo_csv.tell() == 0:
            escritor_csv.writeheader()

        # Escreve a linha do cadastro
        escritor_csv.writerow(cadastro)

    print("Cadastro realizado com sucesso!")

def main():
    realizar_cadastro()

if __name__ == "__main__":
    main()