class A:
    #Variável de classe
    vc = 123

    def __init__(self):
        #Variável de instância
        self.vc = 321

a1 = A()
a2 = A()

print(a1.vc)
print(a2.vc)
print(A.vc)

print("-"*20)
#Vai mudar em todas as instâncias pois usa a classe diretamente para modificar
A.vc = 321

a1.vc = 321
print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

print("-"*20)
print(a1.vc)
print(a2.vc)
print(A.vc)