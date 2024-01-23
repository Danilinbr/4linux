# IF - Condição

idade = int(input("Qual é a sua idade? "))

if idade ==+ 18:
    print("Voce é maior de idade.")

elif idade > 15:
    print("Voce tem pelo menos 15 anos.")

elif idade > 10:
    print("Voce tem pelo menos 10 anos.")

else:
    print("Voce tem menos de 10 anos.")


# FOR / WHILE - Repetição
    
for numero in range(0, 10):
    print(numero)


resposta = "nao"
while resposta != "sim":
    print("Imprimindo mensagem do loop")
    resposta = input("Quer parar o loop? [sim/nao] ")


while True:
    resposta = input("Quer parar o loop? [sim/nao] ")
    if resposta == "sim":
        break


# TUPLA / LISTA / DICIONARIO / SET - Coleções
    
tupla = ("Beterraba", "Mandioca", "Batata", 50, True)
# INDEX       0            1          2      3    4     

for cachorro in tupla:
    print(f"O objeto {cachorro} é um {type(cachorro)}")


lista = ["Beterraba", "Mandioca", "Batata", 50, True]
# INDEX       0            1          2      3    4

lista.append("Pão de batata")
lista.remove(50)
lista.pop(0)
lista.insert(2, "Avião")

print(lista)


# Métodos em Strings
frase = "Testando uma nova frase"
print(frase.replace("a", "---"))
