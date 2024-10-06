#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[m', end=' ')
    print(f'{c}', end =' ')

if cont == 2: #Para ser primo tem que ser divisível por 1 e ele mesmo no caso 2 números
    print(f'\nO número {n} é PRIMO')
else:
    print(f'\nO número {n} é NÃO É PRIMO')