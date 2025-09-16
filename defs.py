import os
import time
from classes import *
#--------------------------------------------------
dicionario_filme={
    1 : Filme ( titulo = "Duna", duracao = 166, genero = "Ficção Cientifica"),
    2 : Filme ( titulo = "Vingadores: Ultimato", duracao = 181, genero = "Ficção Cientifica"),
    3 : Filme ( titulo = "Invocação do Mal ", duracao = 112, genero = "Terror"),
    4 : Filme ( titulo = "Invocação do Mal 2", duracao = 134, genero = "Terror"),
    5 : Filme ( titulo = "Velozes e Furiosos", duracao = 106, genero = "Ação"),
    6 : Filme ( titulo = "Velozes e Furiosos 2", duracao = 107, genero = "Ação"),
    }
#--------------------------------------------------
dicionario_jogo={ 
    1 : Jogo ( titulo = "Hollow Knight", plataforma = "PC", classificacao = "Livre"),
    2 : Jogo ( titulo = "Hollow Knight: Silksong", plataforma = "PC", classificacao = "Livre"),
    3 : Jogo ( titulo = "Grand Theft Auto V", plataforma = "Console", classificacao = "+18"),
    4 : Jogo ( titulo = "Elden Ring", plataforma = "Console", classificacao = "+16"),
    5 : Jogo ( titulo = "Overcooked 2", plataforma = "Console", classificacao = "Livre"),
    6 : Jogo ( titulo = "Sekiro: Shadows Die Twice", plataforma = "PC", classificacao = "+17"),}
#--------------------------------------------------
dicionario_clientes={}
#--------------------------------------------------
def cadastrar_cliente():
    print("Para adicionar um cliente, preencha as informações:")
    nome=input("Seu nome -->").capitalize()
    cpf=input("Seu cpf -->").capitalize()
    novo_id = max(dicionario_clientes.keys(), default=0) + 1
    novo_cliente=Cliente(nome, cpf) 
    dicionario_clientes[novo_id]= novo_cliente 
    print(f"Novo cliente adicionado!{novo_id}")
    time.sleep(2)
    os.system("cls")
#-------------------------------------------------
def remover_cliente():
    print("Remover Cliente")
    remover_id=int(input("Digite o id:"))
    del dicionario_clientes[remover_id]
    os.system("cls")
    print(f"Cliente {remover_id} removido com sucesso! ")
    os.system("pause")
#-------------------------------------------------
def emprestar_filme():
    id_filme = int(input("Digite o ID do filme que deseja emprestar: ")) 
    
    if id_filme in dicionario_filme: 
        Filme = dicionario_filme[id_filme] 
        if not Filme.getEmprestado():
            Filme.setEmprestado(True)
            print(f'Filme "{Filme.getTitulo()}" emprestado com sucesso!')
        else:
            print(f'O filme "{Filme.getTitulo()}" já está emprestado.') 
    else:
        print("ID não encontrado!")

    os.system("pause")
    os.system("cls")
#-------------------------------------------------
def emprestar_jogo():
    id_jogo = int(input("Digite o ID do jogo que deseja emprestar: ")) 
    
    if id_jogo in dicionario_jogo:
        Jogo = dicionario_jogo[id_jogo] 
        if not Jogo.getEmprestado(): 
            Jogo.setEmprestado(True) 
            print(f'Jogo "{Jogo.getTitulo()}" emprestado com sucesso!')
        else:
            print(f'O jogo "{Jogo.getTitulo()}" já está emprestado.') 
    else:
        print("ID não encontrado!")

    os.system("pause")
    os.system("cls")
#-------------------------------------------------
def devolver_filme():
    id_filme = int(input("Digite o ID do filme que deseja devolver: ")) 
    
    if id_filme in dicionario_filme: 
        Filme = dicionario_filme[id_filme]
        if Filme.getEmprestado(): 
            Filme.setEmprestado(False) 
            print(f'Filme "{Filme.getTitulo()}" devolvido com sucesso!')
        else:
            print(f'O filme "{Filme.getTitulo()}" não está emprestado.')
    else:
        print("ID não encontrado!")

    os.system("pause")
    os.system("cls")
#-------------------------------------------------
def devolver_jogo():
    id_jogo = int(input("Digite o ID do jogo que deseja devolver: ")) 
    
    if id_jogo in dicionario_jogo: 
        Jogo = dicionario_jogo[id_jogo]
        if Jogo.getEmprestado(): 
            Jogo.setEmprestado(False) 
            print(f'Jogo "{Jogo.getTitulo()}" devolvido com sucesso!')
        else:
            print(f'O jogo "{Jogo.getTitulo()}" não está emprestado.')
    else:
        print("ID não encontrado!")

    os.system("pause")
    os.system("cls")
#-------------------------------------------------
def listar_todos():
    os.system("cls")

    print("Filmes:")
    for id_filme, filme in dicionario_filme.items():
        print(f"ID: {id_filme} | Título: {filme.getTitulo()}")

    print("\nJogos:")
    for id_jogo, jogo in dicionario_jogo.items():
        print(f"ID: {id_jogo} | Título: {jogo.getTitulo()}")

    os.system("pause")
    os.system("cls")
#-------------------------------------------------
def listar_emprestado():
    encontrados = False
    os.system("cls")

    print("Filmes:")
    for id_filme, filme in dicionario_filme.items():
        if filme.getEmprestado():
            print(f"ID: {id_filme} | Título: {filme.getTitulo()}")
            encontrados = True


    print("\nJogos:")
    for id_jogo, jogo in dicionario_jogo.items():
        if jogo.getEmprestado():
            print(f"ID: {id_jogo} | Título: {jogo.getTitulo()}")
            encontrados = True

    if not encontrados:
        print("Nenhum filme ou jogo emprestado no momento.")
    
    os.system("pause")
    os.system("cls")