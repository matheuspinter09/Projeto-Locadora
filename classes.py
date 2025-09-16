class Item:
    def __init__(self, titulo: str, codigo: int, emprestado: bool = False):
        self.__titulo = titulo
        self.__codigo = codigo
        self.__emprestado = emprestado
#Classe Item que foi pedido no projeto com todas as suas devidas funções de possuir, título, código e status de emprestado.
#--------------------------------------------------
    def __repr__(self):
        return f'Item("{self.__titulo}", "{self.__codigo}")'
#O método mágico '__repr__' (representação) é usado para criar uma string,que representa o objeto.
#Dessa forma ele irá imprimir o título e o código do item quando for chamado.
#--------------------------------------------------
    def getTitulo(self):
        return self.__titulo
    def getCodigo(self):
        return self.__codigo
    def getEmprestado(self):    
        return self.__emprestado
#os métodos getters são usados para acessar os atributos privados da classe.
#--------------------------------------------------
    def setTitulo(self, titulo):
        self.__titulo = titulo
    def setCodigo(self, codigo):
        self.__codigo = codigo
    def setEmprestado(self, status: bool):
        self.__emprestado = status
#os métodos setters são usados para modificar os atributos privados da classe.
#--------------------------------------------------
class Filme(Item):
    def __init__(self, titulo: str, codigo: int, genero: str, duracao: int):
        super().__init__(titulo, codigo)
        self.__genero = genero
        self.__duracao = duracao
    def getGenero(self):
        return self.__genero
    def getDuracao(self):
        return self.__duracao
#Essa é a clase filme que foi pedida no projeto, que herda os atributos da classe Item e possui
#os atributos adicionais de gênero e duração, como um filme deve ter.
#--------------------------------------------------
class Jogo(Item):
    def __init__(self, titulo: str, codigo: int, plataforma: str, classificacao: str):
        super().__init__(titulo, codigo)
        self.__plataforma = plataforma
        self.__classificacao = classificacao
    def getPlataforma(self):
        return self.__plataforma
    def getClassificacao(self):
        return self.__classificacao
#Essa é a classe jogo que foi pedida no projeto, que herda os atributos da classe Item e possui
#os atributos adicionais de plataforma e classificação, como um jogo deve ter.
#--------------------------------------------------
class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__itens_emprestados = []

    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
    
    def getItensEmprestados(self):
        return self.__itens_emprestados
    
    def adicionarItemEmprestado(self, item: Item):
        self.__itens_emprestados.append(item)

    def devolverItemEmprestado(self, item: Item):
        self.__itens_emprestados.remove(item)
#Essa é a classe cliente que foi pedida no projeto, que possui os atributos de nome e cpf.
#Além disso, ela possui uma lista para armazenar os itens emprestados e fazer com que eles
#possam ser adicionados e removidos dessa lista.
#--------------------------------------------------
class Locadora:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__clientes = {}
        self.__itens = {}
    
    def adicionarCliente(self, id_cliente: int, cliente: Cliente):
        self.__clientes[id_cliente] = cliente
    
    def adicionarItem(self, id_item: int, item: Item):
        self.__itens[id_item] = item

    def listarClientes(self):
        for id, cliente in self.__clientes.items():
            print(f"[{id}] {cliente.getNome()} - {cliente.getCpf()}")

    def listarItens(self):
        for id, item in self.__itens.items():
            status = "Emprestado" if item.getEmprestado() else "Disponível"
            print(f"[{id}] {item.getTitulo()} - {status}")
#Essa é a classe locadora que foi pedida no projeto, que possui os atributos de nome,
#clientes e itens. Além disso, ela possui métodos para adicionar clientes e itens,
#e listar os clientes e itens disponíveis na locadora.
#--------------------------------------------------