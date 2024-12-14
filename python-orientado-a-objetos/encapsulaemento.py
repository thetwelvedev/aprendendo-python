"""
_ não recomenda usar -> protected
__ não recomenda mesmo -> private -> paras alterar diretamente na classe (_NomeClasse__nomeatributo)
"""
class BaseDeDados:
    #construtor
    def __init__(self):
        self.__dados = {} #Atributo público

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {}
        self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()

bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd.apaga_cliente(2)
bd.lista_clientes()
bd.__dados = "Outra coisa" #Ele cria esse atributo que não altera o atributo privado lá na classe
print(bd.__dados)
print(bd._BaseDeDados__dados) #Assim que ele acessa esse atributo

#Por conta do getter -> usado o @property
print(bd.dados) #Pode acessar usando o nome do atributo