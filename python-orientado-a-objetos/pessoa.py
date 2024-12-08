from datetime import datetime
from random import randint
class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
#métodos de instância - métodos com o parâmetro self que é usado para referenciar a própria instância do objeto dentro do método.
    def falar(self, assunto):
        if self.comendo:
             print(f"{self.nome} não pode falar comendo.")
             return
        if self.falando:
             print(f"{self.nome} já está falando.")
             return
        
        print(f"{self.nome} está falando sobre {assunto}.")
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
             print(f"{self.nome} não está falando.")
             return
        
        print(f"{self.nome} parou de falar.")
        self.falando = False
    
        
    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo {alimento}.")
            return
        
        if self.falando:
             print(f"{self.nome} não pode comer falando.")
             return
        
        print(f"{self.nome} está comendo {alimento}.")
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo.")
            return
        
        print(f"{self.nome} parou de comer.")
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    
#Método de classe (@classmethod) - que são métodos que pertencem à classe em si, não às suas instâncias.
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimneto):
        idade = cls.ano_atual - ano_nascimneto
        return cls(nome, idade)

#Método estáticos  (@staticmethod) - que são métodos que não referenciam a classe ou instância em seu corpo. São similares à funções normais, porém, por questão de organização, são criados dentro da classe.
    @staticmethod
    def gerar_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa.por_ano_nascimento('Luiz', 1992)
#p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.idade)
print(p1.get_ano_nascimento())
print(Pessoa.gerar_id())