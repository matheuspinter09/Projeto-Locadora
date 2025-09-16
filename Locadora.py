import os
import time
from defs import *  
#importa todas as funções do arquivo defs.py
#-------------------------------------------------

os.system("cls")

print(50 * "-")
print("Seja Bem-Vindo a Pixel & Pipoca")
print(50 * "-")
time.sleep(2)
#Aqui está o título da nossa locadora, que aparece quando o sistema é iniciado.
#-------------------------------------------------
while True:
    os.system("cls")
    print("Menu Principal")
    print("1 - Cadastrar Cliente")
    print("2 - Remover Cliente")
    print("3 - Emprestar Filme")
    print("4 - Emprestar Jogo")
    print("5 - Devolver Filme")
    print("6 - Devolver Jogo")
    print("7 - Listar Todos")
    print("8 - Listar Emprestados")
    print("9 - Sair")

#menu principal que aparece para o usuário, com todas as opções disponíveis.
#-------------------------------------------------

    try:    
        opcao = int(input("Escolha uma opção:"))
    except ValueError:
        print("Opção inválida! Digite um número.")
        time.sleep(2)
        os.system("cls")
        exit()
#Aqui está a verificação para garantir que o usuário insira um número válido.
#-------------------------------------------------

    match opcao:
        case 1:
            cadastrar_cliente()
            os.system("pause")
            os.system("cls")
        case 2:
            remover_cliente()
            os.system("pause")
            os.system("cls")
        case 3:
            emprestar_filme()
            os.system("pause")
            os.system("cls")
        case 4:
            emprestar_jogo()
            os.system("pause")
            os.system("cls")
        case 5:
            devolver_filme()
            os.system("pause")
            os.system("cls")
        case 6:
            devolver_jogo()
            os.system("pause")
            os.system("cls")
        case 7:
            listar_todos()
            os.system("pause")
            os.system("cls")
        case 8:
            listar_emprestado()
            os.system("pause")
            os.system("cls")
        case 9:
            print("Saindo...")
            time.sleep(2)
            os.system("cls")
            exit()
        case _:
            print("Opção inválida!")
            time.sleep(2)
            os.system("cls")
            exit()
#Aqui está o sistema de correspondência para chamar a função correta
#com base na opção escolhida pelo usuário no menu principal.
#-------------------------------------------------