# Título: Coluna
#
# Descrição: É solicitado ao utilizador qual a largura e altura da coluna a exibir.
#            Mediante os valores de largura e altura introduzidos é exibida uma coluna com # de largura e altura introduzidas
#  
# Funções e conceitos abordados:
# - estruturas de repetição: "for in range()"
# - estruturas de repetição: "for in range()" aninhadas

import funcoes

funcoes.clean()

largura = int(input("Qual a largura da coluna pretendida? "))
altura = int(input("Qual a altura da coluna pretendida? " ))


for n in range(altura):
    for n in range(largura):
        print("#", end="")
    print("")