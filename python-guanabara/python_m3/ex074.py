#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
maior = menor = 0
for i in range(0,5):
    if numeros[i] > maior or maior == 0:
        maior = numeros[i]
    elif numeros[i] < menor or menor == 0:
        menor = numeros[i]

print(f'Os valores sorteados foram: {numeros}')
print(f'''\nO menor valor da tupla: {menor}
O maior valor da tupla: {maior}''')
#or
print('-='*20) 
print(f'Os valores sorteados foram: ', end= '')
for n in numeros:
    print(f'{n}', end =' ')
print(f'''\nO menor valor da tupla: {min(numeros)}
O maior valor da tupla: {max(numeros)}''')
