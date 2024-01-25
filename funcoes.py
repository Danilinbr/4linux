def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    return {"nome": nome, "idade": idade}

def categorizar_pessoas(pessoas):
    categorias = {"Menor de idade": 0, "Adulto": 0, "Idoso": 0}
    
    for pessoa in pessoas:
        idade = pessoa["idade"]
        if idade <= 17:
            categorias["Menor de idade"] += 1
        elif 18 <= idade <= 59:
            categorias["Adulto"] += 1
        else:
            categorias["Idoso"] += 1
    
    return categorias

def exibir_lista_pessoas(categoria, pessoas):
    print(f"\n{categoria}:\n")
    for pessoa in pessoas:
        if categoria == "Menor de idade" and pessoa["idade"] <= 17:
            print(pessoa["nome"])
        elif categoria == "Adulto" and 18 <= pessoa["idade"] <= 59:
            print(pessoa["nome"])
        elif categoria == "Idoso" and pessoa["idade"] >= 60:
            print(pessoa["nome"])

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def painel(prompt, input):
    while True:
        clear()
        try:
            opt = print(f"{prompt}")
            if opt in input:
                return opt
            else:
                clear()
                print("Opção invalida!")
        except ValueError:
            print("Digite o numero da opção!")