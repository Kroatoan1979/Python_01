# Título: Par ou impar
#
# Descrição: Programa solicita um algarismo ao utilizador caso seja par continua a executar e a solicitar algarismos, caso seja impar o programa termina.
#                    
# Funções e conceitos abordados:
# - 

import funcoes
funcoes.clean()

algarismo = int(input("Digite um algarismo: "))

par = algarismo % 2

while par == 0:
    print(algarismo,"é um número par.")
    algarismo = int(input("Digite um novo algarismo por favor: "))
    par = algarismo % 2

print(algarismo,"é impar")
