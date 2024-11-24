class Conta:
    def __init__(self,numero, titular, saldo, limite, codigo_banco): #função construtora/posso passar um parâmetro opcional também para esses parâmetros
        print(f'Construindo objeto...{self}')#Self é a referência que onde encontrar o objeto, vai ser caminho para ir para cada objeto e forma distinta
        # Abributos
        self.__numero = numero #colocando esses dois underscore o atributo fica privado é equivalente ao private no java porém tem que alterar em todos os métodos pois agora faz parte do nome da variável
        self.__titular = titular #poded chamar usando por exemplo conta._Conta__saldo (<objeto>._<classe>__<atributo>) e fica oculto na recomendação
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = codigo_banco

    #Criando métodos
    def extrato(self):
        print(f'Titular: {self.__titular}')
        print(f'Saldo: {self.__saldo}')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): # Método privado foi feito para ser usado apenas dentro dessa classe
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <=  valor_disponivel_a_sacar

    def saca(self, valor):
        # verificação
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor R${valor:.2f} passou o limite')

    def transfere(self, valor, destino): #Se colocar o __ antes do método pode criar um método privado como __transfere  por exemplo
        #Encapsulamento
        self.saca(valor) #Como a origem acessa o mesmo endereço do self pois é o objeto que chama a função, entçao vou tirar p parâmetro origem da função e para chamar o método saca vou usar o self
        destino.deposita(valor)

    #Método para retornar os atributos agora privados/Getters- sempre retorna
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    #Setters - nunca retorna, só altera os elementos
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco(): #Método estático são da classe e não tem objeto, como o próprio nome já diz tem o valor estático e nenhum objeto influência nele
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}