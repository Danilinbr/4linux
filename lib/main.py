from funcoes import registrar_cliente, realizar_deposito, realizar_saque

def menu():
    print("1. Registrar Cliente")
    print("2. Realizar Depósito")
    print("3. Realizar Saque")
    print("0. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            idade = int(input("Digite a idade do cliente: "))
            saldo = float(input("Digite o saldo inicial do cliente: "))
            usuario = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")

            resultado = registrar_cliente(nome, idade, saldo, usuario, senha)
            print(resultado)

        elif opcao == "2":
            nome = input("Digite o nome do cliente: ")
            valor = float(input("Digite o valor do depósito: "))
            resultado = realizar_deposito(nome, valor)
            print(resultado)

        elif opcao == "3":
            nome = input("Digite o nome do cliente: ")
            valor = float(input("Digite o valor do saque: "))
            resultado = realizar_saque(nome, valor)
            print(resultado)

        elif opcao == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
