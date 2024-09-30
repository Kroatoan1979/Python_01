# Título: Multibanco
#
# Descrição: O programa simula uma máquina multibanco onde são efetuadas as operações de
#            consulta de saldos, levantamentos e depósitos.
#
# Funções e conceitos abordados:
# - funções de entrada e saida "input" e "print"
# - operadores de atribuição "=", "+=", "-="
# - operadores de comparação "<=", ">="
# - operadores de lógicos "and"
# - operadores de assoçiação "not in"
# - estruturas condicionais "if", "elif", "else"

import os
import sys

os.system('cls')

saldo = 2000
limite = 100


nome = input("Qual o seu nome: ")
sobrenome = input("Qual o seu sobrenome: ")
os.system('cls')

print("O seu nome é:",nome, sobrenome,"\n\nSeja bem vindo ao nosso ATM\n")

menu_1 = -1
while menu_1 not in [1,2,3,0]:
    menu_1 = int(input("Qual operação pretende efetuar?\n [1] - Consultar saldo\n [2] - Depósito\n [3] - Levantamento\n [0] - Terminar\n -> "))
    os.system('cls')
    if menu_1 not in [1,2,3,0]:
        print("Opção inválida. Deverá escolher uma operação de [0-3]")

if menu_1 == 1:
    print("A exibir o saldo da sua conta...")
    print(nome,sobrenome,"o seu saldo é de", saldo)
elif menu_1 == 2:
    print("A efetuar depósito")
    deposito = int(input("Qual o valor que pretende depositar? "))
    saldo += deposito
    print("Depósito efetuado no valor de",deposito,"\nO seu saldo é agora de",saldo)
elif menu_1 == 3:
    print("A efetuar levantamento")
    levantamento = int(input("Qual o valor que pretende levantar? "))
    if levantamento <= saldo and levantamento <= limite:
        saldo -= levantamento
        print("Levantamento bem sucedido!\nO seu saldo é agora de", saldo)
    else:
        if levantamento > saldo and levantamento > limite:
            print("O seu saldo",saldo,"não permite efetuar o levantamento. E o levantamento ultrapassa o valor limite de",limite,"por operação!\nUm Óptimo dia!")
        elif levantamento > saldo:
            print("O seu saldo não permite efetuar o levantamento desejado")
        elif levantamento > limite:
            print("O limite de levantamento por operação é menor do que",levantamento)
elif menu_1 == 0:
    sys.exit("Programa terminado a seu pedido")       

#sys.exit("Programa terminado!")

