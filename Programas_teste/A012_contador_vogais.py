# Título:
#
# Descrição: 
#                    
# Funções e conceitos abordados:
# - 

import funcoes
funcoes.clean()

texto = input("Faremos uma contagem do número de vogais existente no seu texto.\nInforme qual o texto a analisar: ")
VOGAIS = "AEIOU"
counter = 0

for letra in texto:
    if letra.upper() in VOGAIS:
        counter += 1

print(f"O seu texto apresenta {counter} vogais")
