# Título: Calculadora aritmética simples
# Descrição: 
# Programa exibe a opção ao utilizador de qual a operação que pretende efetuar.
# Depois solicita a introdução do primeiro e segundo algarismos e efetua a operação apresentando o resuntado no monitor.
# Funções e conceitos abordados:
# - contrução e importação de funções
# - funções de entrada e saida "input" e "print"
# - operadores aritméticos "+", "-", "*", "/"
# - operadores comparação "=="
# - operadores associação "not in"
# - estruturas condicionais "if", "elif", "else"
# - estruturas de repetição "while"

import funcoes
funcoes.clean()

def menu_01():
    print("|##############################|")
    print("|                              |")
    print("|   1 - Adição                 |")
    print("|   2 - Subtração              |")
    print("|   3 - Multiplicação          |")
    print("|   4 - Divisão                |")
    print("|   0 - Sair                   |")
    print("|                              |")
    print("|##############################|")

menu_01()

operacao = int(input("Qual a operação que deseja efetuar? [0-4]: "))

while operacao not in [0,1,2,3,4]:
    operacao = int(input("Deverá escolher a operação pretendida de [0-4]: "))

if operacao == 0:
    print("Programa terminado!")
    funcoes.exit()

x = int(input("Qual o primeiro algarismo? "))
y = int(input("Qual o segundo algarismo? "))

if operacao == 1:
    soma = x + y
    print("Escolheu adicionar",x,"+",y,"\nO resultado da adição é =",soma)
if operacao == 2:
    subtracao = x - y
    print("Escolheu subtrair",x,"-",y,"\nO resultado da subtração é =",subtracao)
if operacao == 3:
    multiplicacao = x * y
    print("Escolheu multiplicar",x,"X",y,"\nO resultado da multiplicação é =",multiplicacao)
if operacao == 4:
    divisao = x / y
    print("Escolheu dividir",x,":",y,"\nO resultado da divisão é =",divisao)
