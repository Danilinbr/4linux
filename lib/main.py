from funcoes import registrar_cliente, realizar_deposito, realizar_saque, verificar_cliente, limpar_tela
from classes import ValidacaoInput

def menu():
    print("1. Registrar Cliente")
    print("2. Realizar Depósito")
    print("3. Realizar Saque")
    print("4. Verificar Saldo")
    print("0. Sair")

def main():
    while True:
        limpar_tela()
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = ValidacaoInput.validar_str("Digite o nome do cliente: ", lambda x: x.isalpha() == True)
            idade = ValidacaoInput.validar_int("Digite a idade do cliente: ")
            saldo = ValidacaoInput.validar_float("Digite o saldo inicial do cliente: ")
            usuario = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")

            resultado = registrar_cliente(nome, idade, saldo, usuario, senha)
            limpar_tela()
            print(resultado)
            input("")

        elif opcao == "2":
            nome = input("Digite o nome do cliente: ")
            valor = ValidacaoInput.validar_float("Digite o valor do depósito: ")
            resultado = realizar_deposito(nome, valor)
            limpar_tela()
            print(resultado)
            input("")

        elif opcao == "3":
            nome = input("Digite o nome do cliente: ")
            valor = ValidacaoInput.validar_float("Digite o valor do saque: ")
            resultado = realizar_saque(nome, valor)
            limpar_tela()
            print(resultado)
            input("")
        
        elif opcao == "4":
            nome = input("Digite o nome do cliente: ")
            cliente = verificar_cliente(nome)
            if cliente:
                limpar_tela()
                print(f"Usuario: {cliente[0]}, Saldo: R${cliente[1]}")
                input("")
            else:
                print("Usuario não encontrado.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
