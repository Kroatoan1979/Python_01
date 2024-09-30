# Título: Password
#
# Descrição: Programa que simula um acesso permitido ou negado por password
#                    
# Funções e conceitos abordados:
# - ciclo infinito "while True"
# - instrução break (para criar por exemplo exceções em ciclos)

import funcoes
funcoes.clean()

while True:
    password = input("Insira a password: ")

    if password == "pass":
        break
    else:
        print("Acesso negado!")

print("Acesso concedido!")