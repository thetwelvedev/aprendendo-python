#Funções 2
def linha():
    print('-'*30)
#Interactive Help
#help()
#print(input.__doc__)

#docstrings
#ex1
linha()
def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    Parâmetro i: início da contagem
    Parâmetro f: fim da contagem
    Parâmetro p: passo da contagem
    return: sem retorno
    """
    #docstring
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')
contador(2,10,2)
linha()
help(contador)
#Parâmetros opcionais
#ex2
linha()
def somar(a,b,c=0): #Caso c não tenha valor ele fica com valor 0, o parâmetro opcional pode ser colocado em qualquer parâmetro
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)
linha()    
#Escopo de variáveis
#ex3
def teste():
    x = 8 #Escopo local(só funciona nessa parte, neste caso dentro dessa função)
    print(f'Na função teste, n = {n}')
    print(f'Na função teste, x = {x}')
#Programa pricipal
n = 2 #Escopo global
print(f'No programa principal, n = {n}')
teste()
linha()
#ex4
def função():
    global n1 #nesse caso agora o n1 daqui dentro é o global e o de fora não tem valor
    n1 = 4
    print(f'N1 dentro vale {n1}')
n1 = 2 #Escopo global, mas agora tá sem valor pelo comando global dentro da função
função()
print(f'N1 fora vale {n1}')
#Retorno de resultados
linha()
#ex5
def somar2(a=0,b=0,c=0): #Caso c não tenha valor ele fica com valor 0, o parâmetro opcional pode ser colocado em qualquer parâmetro
    s = a + b + c
    return s

r1 = somar2(3,2,5)
r2 = somar2(1,7)
r3 = somar2(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}') #útil para quando for personalizar os resultados 
print(somar2(5,10,15))

#Prática
#ex1
def fatorial(num=1):
    f = 1
    for c in range(num,0,-1): #Aqui ele vai fazer um for decrescente 
        f *= c
    return f
linha()
n = int(input('Digite um número: '))
print(f'{n}! = {fatorial(n)}')

#ex2
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
linha()
n = int(input('Digite um número: '))
print(par(n))
if par(n):
    print('É par!')
else:
    print('Não é par!')