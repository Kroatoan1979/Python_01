# Título: Comparador numérico
# Descrição: Solicita ao utilizador a introdução de 2 algarismos e depois compara-os e indica qual a sua relação de grandeza
# Funções e conceitos abordados:
# - funções de entrada e saida "input" e "print"
# - operadores de comparação "<",">"
# - estruturas condicionais "if", "elif", "else"

import funcoes
funcoes.clean()

x = input("Introduza o primeiro algarismo: ")
y = input("Introduza o segundo algarismo: ")

if x > y:
    print(x,"é maior do que",y)
elif x < y:
    print(x,"é menor do que",y)
else:
    print(x,"é igual a",y)
