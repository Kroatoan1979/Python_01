# Título:
#
# Descrição: 
#                    
# Funções e conceitos abordados:
# - 

import funcoes
funcoes.clean()

liga = [
    [1, 2, 3, 4, 5],
    ["sporting", "porto", "benfica", "santa clara", "guimarães"],
    [18, 15, 13, 12, 12]
]

clube = ""
posicao = 0
pontuacao = 0

print("Campeão provisório ->",liga[1][0])
pos = int(input("Qual a posição da tabela que deseja verificar? "))

for x in liga[0]:
    if x == pos:
        print(f"O clube na posição {pos} é o {liga[1][pos -1]} e tem no momento {liga[2][pos -1]} pontos atribuidos")
    else:
        continue

# opc = input("Deseja verificar a tabela completa [S/N]")





print("LIGA PORTUGAL".center(47,"#"))

for x in liga[0]:
    if x >= 1:
        print(f"{x}  {liga[1][x-1]}  {liga[2][x-1]}->pts")

