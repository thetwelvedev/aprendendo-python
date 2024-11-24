from conta import Conta
def linha():
    print('-'*30)
#Objetos
conta = Conta(123, "Leleco", 55.5, 1000.0, 1)
conta2 = Conta(321, "Leo", 125.5, 2000.0, 2)
linha()
#Assim como para os objetos usamos o self para puxar a referência no caso dos métodos são os próprios objetos
conta.extrato()
conta2.extrato()
linha()
#Usando outros métodos
pagamento = float(input('Deposite seu pagamento aqui -> '))
conta.deposita(pagamento)
print(f'extrato atual : {conta.saldo}')
linha()
saque = float(input('Retire seu pagamento aqui -> '))
conta.saca(saque)
print(f'extrato atual : {conta.saldo}')

#Quando criamos os objetos eles são a referência para acessar seus atributos, no caso seus atributos que agora tem informações e estão na memória.
#Caso queria tirar essa referência ou deixar de apontar para memória, você iguala ele a None.
#Exemplo
print(conta) #Apontando para memória
conta = None
print(conta) #Depois do None não aponta