# # Exercícios - Aula 04
# 1) Escreva um programa em Python que simule uma dança das cadeiras. Você deverá
# importar o pacote random e iniciar uma lista com nomes de pessoas que participariam da
# brincadeira. O jogo deverá iniciar com 9 cadeiras e 10 participantes. A cada rodada,
# uma cadeira deverá ser retirada e um dos jogadores, de forma aleatória, ser eliminado. O
# jogo deverá terminar quando apenas restar uma cadeira e ao final de todas as rodadas,
# deverá ser apresentado vencedor.

# Dica: [OPCIONAL] Você poderá utilizar o modulo "time" para simular um tempo de a cada rodada para criar
# um efeito mais interessante.

# Dica: [OPCIONAL] Tentem fazer a remoção de uma pessoa aleatória por rodada sem utilizar a função "choice".
# =============================================================
# import random as rdm
# import time
# import os
# import sys

# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def jogo(players):
#     num_cad = 9
#     clear()
#     print(f"Jogo iniciado. Os participantes são:\n\n {players}\n\n")
#     time.sleep(1)
#     while num_cad > 0:
#         time.sleep(2)
#         clear()
#         out = rdm.choice(players)
#         players.remove(out)
#         print(f"\nTAM TAM TAM TAM:\n\nJogador(a) {out} saiu do jogo!\n")
#         print(f"Jogadores restantes são {players}!")
#         num_cad -= 1
#     clear()
#     vencedor = str(players[0])
#     print(f"O vencedor é {vencedor}!")
#     input("")
    

# def participantes():
#     new_part = []
#     i = 0
#     lista = ["Joao", "Maria", "Tiago", "Amanda", "Emanuele", "Caio", "Suzana", "Miguel", 
#     "Rosangela", "Rian", "Lucimar", "Ulisses", "Leonardo", "Kaique", "Bruno", "Raquel", 
#     "Benedito", "Tereza", "Valmir", "Joaquim"]
#     while i < 10:
#         play = rdm.choice(lista)
#         if play in new_part:
#             None
#         else:
#             i += 1
#             new_part.append(play)
#     return new_part
    
# def main():
#     players = participantes()
#     jogo(players)

    
 

# if __name__ == '__main__':
#      main()
# =============================================================
# 2) Crie um programa utilizando dois arquivos, onde um deles possui todas as funcçoes utilizadas na aplicação.
# Onde o programa deverá perguntar ao usuario nome/idade de uma pessoa, e armazenar esses valores em um dicionario,
# e repetir essa ação até que a pessoa não queira mais adicionar nomes, em seguida, o programa deverá mostrar o numero
# de pessoas em categorias de acordo com a idade:
# 0-17 anos: Menor de idade
# 18-59 anos: Adulto
# 60+ anos: Idoso
# E deverá perguntar para o usuario se ele gostaria de exibir na tela uma lista com os nomes das pessoas de cada grupo,
# ou se o usuario deseja finalizar o programa.

from funcoes import cadastrar_pessoa, categorizar_pessoas, exibir_lista_pessoas

def main():
    pessoas = []
    
    while True:
        pessoa = cadastrar_pessoa()
        pessoas.append(pessoa)
        
        continuar = input("Deseja adicionar mais uma pessoa? (s/n): ").lower()
        if continuar != 's':
            break

    categorias = categorizar_pessoas(pessoas)

    for categoria, quantidade in categorias.items():
        print(f"{categoria}: {quantidade} pessoas")

    opcao = input("\nDeseja exibir a lista de pessoas de cada grupo? (s/n): ").lower()
    if opcao == 's':
        for categoria in categorias.keys():
            exibir_lista_pessoas(categoria, pessoas)

    print("Programa finalizado.")

if __name__ == "__main__":
    main()

# =============================================================
# 3) Crie um programa que pergunte para o usuario um numero de pessoas a participarem de um sorteio (2-20),
#  e o numero de pessoas a serem sorteadas, e depois sorteie esse numero de pessoas da lista.

# O programa deverá pegar o numero de pessoas a participar aleatoriamente desta lista:

# lista = ["Joao", "Maria", "Tiago", "Amanda", "Emanuele", "Caio", "Suzana", "Miguel", 
# "Rosangela", "Rian", "Lucimar", "Ulisses", "Leonardo", "Kaique", "Bruno", "Raquel", 
# "Benedito", "Tereza", "Valmir", "Joaquim"]

# Nota: A mesma pessoa não pode ganhar duas vezes.
