# Título: Condtruto de menus
#
# Descrição: 
# Solicita ao utilizador:
# - a mensagem que deseja destacar
# - a altura e largura pretendidas
# - o caracter com que deseja construir o menu
# Depois devolve a mensagem em modo centralizado no menu 
#                    
# Funções e conceitos abordados:
# - Contagem de caracteres de strings | contagem = len(mens)
# - formatação de strings | print(mens.upper().center(largura, caracter), end="")
# - formatação de strings | print(f"A mensagem {mens} que pretende destacar tem um total de {contagem} carateres.")
# - estruturas de repetição aninhadas

import funcoes

funcoes.clean()

texto = input("Qual a mensagem que pretende para o seu menu: ")

mens = f" {texto} "

contagem = len(mens)
print(f"A mensagem {mens} que pretende destacar tem um total de {contagem} carateres.")

largura = int(input("Qual a largura que deseja para o seu menu: "))
altura = int(input("Qual a altura que deseja para o seu menu: "))
caracter = input("Qual o caracter com que pretende construir o seu menu: ") 

altura_2 = altura // 2
for alt in range(altura_2):
    print()
    for lar in range(largura):
        print(caracter, end="")
print()

print(mens.upper().center(largura, caracter), end="")

for alt in range(altura_2):
    print()
    for lar in range(largura):
        print(caracter, end="")
print("\n")