#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
números = [randint(1,10),randint(1,10), randint(1,10),randint(1,10),randint(1,10)]

def sorteia():
    from time import sleep
    #Vamos pecorrer a lista
    print(f'Vamos sortear {len(números)} valores da lista: ', end='')
    for valor in números:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
    print('Pronto!')
def somaPar():
    soma = 0
    for valor in números: #Pecorrendo a lista
        if valor % 2 == 0: #Pegando os valores pares
            soma += valor
    print(f'Somando os valores pares da lista {números}, fica igual a {soma}')

sorteia()
somaPar()