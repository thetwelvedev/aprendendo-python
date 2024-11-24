class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    #Getter
    @property # Vai fazer executar esse método direto quando chamar o nome ex.: cliente.nome/ o atributo tem que tá privado
    def nome(self): # Vai sempre retornar a primeira letra maiúscula
        print('Chamando @property nome()')
        return self.__nome.title()
    #É como se tivesse acessando o atributo diretamente mas nesse caso ele tá privado e executa o método mas tudo fica mascarado por conta do @property

    #Setter
    @nome.setter # @<atributo>.setter
    def nome(self, nome):
        print('Chamando o setter nome()')
        self.__nome = nome