import os
import sys
import time

def clean():
    os.system('cls')

def exit():
    sys.exit()

def sleep(seg):
    time.sleep(seg)

def clean_fim():
    opcao = input("\nPretende limpar a sua consola? [S/N]")
    if opcao in ["S","s"]:
        clean()
    elif opcao in ["N","n"]:
        exit

