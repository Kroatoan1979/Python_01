# Base de dados dinâmica
# O programa abaixo gere uma base de nomes guardadas na variável nomes_mem
# Pergunta ao utilizador qual o nome que deseja verificar se existe na base de dados
# Depois caso exista informa que já existe e termina a execução
# Caso não exista pergunta de deseja ou não adicionar o nome que verificou á base de dados.
# Em ambos os casos de adição ou não adição mostra o conteudo da "base de dados" ou seja da variável nomes_mem

# funções e conceitos:
# - Variáveis "list"
# - estruturas de repetição "for" e "while"
# - estruturas condicionais "if" e "elif"

import funcoes
funcoes.clean()

nomes_mem = ["Ivan", "Agostinho", "Filomena", "Sara", "João"]
print(type(nomes_mem))

nome_test = input("Informe o nome que deseja verificar: ")

while nome_test not in nomes_mem:
    for nome in nomes_mem:
        if nome == nome_test:
            print("O nome",nome_test,"já se econtra na base de dados.")
            break
    else:
        print("O nome",nome_test,"não está presente na base de dados.")
        opcao = input("Deseja adicionar o nome á base de dados? [S/N]")
        if opcao in ["S","s"]:
            nomes_mem.append(nome_test)
            print("O nome",nome_test,"foi adicionado á base de dados")
            for nome_imp in nomes_mem:
                print(nome_imp)
            funcoes.exit()
        elif opcao in ["N","n"]:
            print("O nome",nome_test,"não foi adiciponado à base de dados!")
            for nome_imp in nomes_mem:
                print(nome_imp)
            funcoes.exit()
else:
    print("O nome",nome_test,"já se econtra na base de dados.")
    funcoes.exit()