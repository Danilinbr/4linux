# 1) Em muitos programas, nos é solicitado o preenchimento de algumas informações como
# nome, CPF, idade e unidade federativa. Escreva um script em Python que solicite as
# informações cadastrais mencionadas e que em seguida as apresente da seguinte forma:

# -----------------------------
# Confirmação de cadastro:
# Nome: Guido Van Rossum
# CPF: 999.888.777/66
# Idade: 65
# -----------------------------

# Nome = input ("Digite seu nome:\n")
# Cpf = input ("Digite seu CPF (Apenas numeros):\n")
# Cpf_format = f"{Cpf[:3]}.{Cpf[3:6]}.{Cpf[6:9]}/{Cpf[9:]}"
# Idade = input ("Digite sua idade (Apenas numeros):\n")

# print (f"Confirmação de cadastro:\n",
#     f"Nome: {Nome}\n",
#     f"CPF: {Cpf_format}\n",
#     f"Idade: {Idade}")
# 2) Escreva um script em Python que receba dois números e que seja realizado as seguintes
# operações:
# • soma dos dois números
# • diferença dos dois números
# O resultado deverá ser apresentado conforme a seguir - no exemplo foram digitados os números
# 4 e 2:

# ------------------------------

# Soma: 4 + 2 = 6
# Diferença: 4 - 2 = 2

num1 = int(input ("\nDigite um numero:\n"))
num2 = int(input ("Digite outro numero:\n"))

Soma = num1+num2
print (f"Soma: {num1} + {num2} = {Soma}\n")

if (num1 > num2):
    Diferença = num1 - num2
    print (f"Diferença: {num1} - {num2} = {Diferença}")
else:
    Diferença = num2 - num1
    print (f"Diferença: {num2} - {num1} = {Diferença}")
