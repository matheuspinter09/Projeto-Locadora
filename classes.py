class Item:
    def __init__(self, titulo: str, codigo: int, emprestado: bool = False):
        self.__titulo = titulo
        self.__codigo = codigo
        self.__emprestado = False
#--------------------------------------------------
    def __repr__(self):
        return f'Item("{self.titulo}", "{self.codigo}")'
#--------------------------------------------------
    def getTitulo(self):
        return self.__titulo
    def getCodigo(self):
        return self.__codigo
    def getEmprestado(self):    
        return self.__emprestado
#--------------------------------------------------
    def setTitulo(self, titulo):
        self.__titulo = titulo
    def setCodigo(self, codigo):
        self.__codigo = codigo
    def setEmprestado(self, status: bool):
        self.__emprestado = status
#--------------------------------------------------
class Filme(Item):
    def __init__(self, titulo:str, genero: str, duracao: int):
        super().__init__(titulo, genero, duracao)
        self.__genero = genero
        self.__duracao = duracao
    def getGenero(self):
        return self.__genero
    def getDuracao(self):
        return self.__duracao
#--------------------------------------------------
class Jogo(Item):
    def __init__(self, titulo:str,plataforma: str, classificacao: int):
        super().__init__(titulo, plataforma, classificacao)
        self.__plataforma = plataforma
        self.__classificacao = classificacao
    def getPlataforma(self):
        return self.__plataforma
    def getClassificacao(self):
        return self.__classificacao
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
#--------------------------------------------------
class Locadora:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__clientes = []
        self.__itens = []
    
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