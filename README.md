# 📽️ Pixel & Pipoca – Sistema de Locadora

Este é um projeto simples em **Python** que simula o funcionamento de uma locadora de filmes e jogos.  
O sistema permite cadastrar clientes, emprestar e devolver itens, além de listar o acervo e verificar quais produtos estão emprestados.

---

## 📂 Estrutura do Projeto
📦 Pixel&Pipoca
├── classes.py # Classes principais: Item, Filme, Jogo, Cliente, Locadora
├── defs.py # Funções auxiliares (cadastrar cliente, emprestar, devolver, listar)
├── main.py # Arquivo principal: exibe o menu e roda o programa
└── README.md # Documentação do projeto

---

## ⚙️ Funcionalidades

- ✅ Cadastro de clientes  
- ✅ Remoção de clientes  
- ✅ Empréstimo e devolução de filmes  
- ✅ Empréstimo e devolução de jogos  
- ✅ Listagem de todos os itens cadastrados  
- ✅ Listagem de itens emprestados  
- ✅ Controle de status (Disponível / Emprestado)  

---

## 🚀 Como Executar

1. Clone ou baixe o projeto.  
2. Certifique-se de ter o **Python 3.10+** instalado.  
3. Abra o terminal na pasta do projeto.  
4. Rode o programa principal:

  bash
python main.py

---

## 🖥️ Menu Principal

Ao iniciar o sistema, você verá:
--------------------------------------------------
Seja Bem-Vindo a Pixel & Pipoca
--------------------------------------------------
Menu Principal
1. Cadastrar Cliente
2. Remover Cliente
3. Emprestar Filme
4. Emprestar Jogo
5. Devolver Filme
6. Devolver Jogo
7. Listar Todos
8. Listar Emprestados
9. Sair

Digite o número da opção desejada para navegar pelo sistema.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- Estrutura de **classes e herança**
- Uso de **listas e dicionários**
- **Funções** para organização do código
- Comandos de sistema (`os.system`) para limpar tela e pausar execução
