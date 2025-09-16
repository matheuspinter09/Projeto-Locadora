import os
import time
from classes import *
#Estamos importando as classes que criamos no arquivo classes.py
#e importando as bibliotecas os e time para usar comandos do sistema operacional
#--------------------------------------------------
dicionario_filme={
    1 : Filme ( titulo = "Duna", duracao = 166, codigo=1,genero = "Ficção Cientifica"),
    2 : Filme ( titulo = "Vingadores: Ultimato", duracao = 181, codigo=2, genero = "Ficção Cientifica"),
    3 : Filme ( titulo = "Invocação do Mal ", duracao = 112, codigo=3, genero = "Terror"),
    4 : Filme ( titulo = "Invocação do Mal 2", duracao = 134, codigo=4, genero = "Terror"),
    5 : Filme ( titulo = "Velozes e Furiosos", duracao = 106, codigo=5, genero = "Ação"),
    6 : Filme ( titulo = "Velozes e Furiosos 2", duracao = 107, codigo=6, genero = "Ação"),
    }
#Aqui estão armazenados os filmes que a locadora possui, 
#com seus respectivos IDs, títulos, durações e gêneros.
#--------------------------------------------------
dicionario_jogo={ 
    1 : Jogo ( titulo = "Hollow Knight", codigo=1, plataforma = "PC", classificacao = "Livre"),
    2 : Jogo ( titulo = "Hollow Knight: Silksong", codigo=2, plataforma = "PC", classificacao = "Livre"),
    3 : Jogo ( titulo = "Grand Theft Auto V",codigo=3,  plataforma = "Console", classificacao = "+18"),
    4 : Jogo ( titulo = "Elden Ring", codigo=4, plataforma = "Console", classificacao = "+16"),
    5 : Jogo ( titulo = "Overcooked 2", codigo=5, plataforma = "Console", classificacao = "Livre"),
    6 : Jogo ( titulo = "Sekiro: Shadows Die Twice", codigo=6, plataforma = "PC", classificacao = "+17"),}
#Aqui estão armazenados os jogos que a locadora possui, 
#com seus respectivos IDs, títulos, plataformas e classificações.
#--------------------------------------------------
dicionario_clientes={}
#Aqui está o dicionário que irá armazenar os clientes que forem cadastrados na locadora.
#--------------------------------------------------
def cadastrar_cliente():
    print("Para adicionar um cliente, preencha as informações:")
    nome=input("Seu nome -->").capitalize()
    cpf=input("Seu cpf -->").capitalize()
    novo_id = max(dicionario_clientes.keys(), default=0) + 1
    novo_cliente=Cliente(nome, cpf) 
    dicionario_clientes[novo_id]= novo_cliente 
    print(f"Novo cliente adicionado! \nSegue o ID:{novo_id}")
    time.sleep(2)
    os.system("cls")
#Aqui está a função para cadastrar um cliente, onde o usuário irá inserir
#seu nome e cpf, e o sistema irá gerar um ID único para o cliente.
#-------------------------------------------------
def remover_cliente():
    print("Remover Cliente")
    remover_id=int(input("Digite o id:"))
    del dicionario_clientes[remover_id]
    os.system("cls")
    print(f"Cliente {remover_id} removido com sucesso! ")
    os.system("pause")
#Aqui está a função para remover um cliente, onde o usuário irá inserir
#o ID do cliente que deseja remover, e o sistema irá deletar o cliente do dicionário.
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
        print("\nID não encontrado!")

    os.system("pause")
    os.system("cls")
#Aqui está a função para emprestar um filme, onde o usuário irá inserir
#o ID do filme que deseja emprestar, e o sistema irá verificar se o filme está
#disponível ou não, e atualizar o status de emprestado do filme.
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
#Aqui está a função para emprestar um jogo, onde o usuário irá inserir
#o ID do jogo que deseja emprestar, e o sistema irá verificar se o jogo está
#disponível ou não, e atualizar o status de emprestado do jogo.
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
#Aqui está a função para devolver um filme, onde o usuário irá inserir
#o ID do filme que deseja devolver, e o sistema irá verificar se o filme está
#emprestado ou não, e atualizar o status de emprestado do filme.
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
#Aqui está a função para devolver um jogo, onde o usuário irá inserir
#o ID do jogo que deseja devolver, e o sistema irá verificar se o jogo está
#emprestado ou not, e atualizar o status de emprestado do jogo.
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
#Aqui está a função para listar todos os filmes e jogos disponíveis na locadora,
#mostrando o ID e o título de cada um.
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
        print("\nNenhum filme ou jogo emprestado no momento.\n")
    
    os.system("pause")
    os.system("cls")
#Aqui está a função para listar todos os filmes e jogos que estão emprestados,
#mostrando o ID e o título de cada um. Se nenhum estiver emprestado, uma mensagem
#é exibida informando isso.