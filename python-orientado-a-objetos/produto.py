class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


    # Getter - é um método que retorna o valor de um atributo de classe
    @property
    def preco(self):
        return self._preco
    
    # Setter - é um método que modifica o valor do atributo de classe
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str): # Vai fazer quando for string sair sem R$
            valor = float(valor.replace('R$', ''))
        self._preco = valor

p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('Camiseta', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)

'''Os getters e setters do python não precisam modificar outras partes da classe, só precisa fazer getter e o setter
- São como filtros, proteções, onde os atributos vão passar primeiro nos setters e getters e depois são passados nos outros métodos'''