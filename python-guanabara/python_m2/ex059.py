#Crie um programa que leia dois valores e mostre um menu na tela:
'''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
a = float(input('Digite um valor: '))
b = float(input('Digite um valor: '))
while True:
    escolha = int(input('''Faça sua escolha:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Sua escolha: '''))
    
    if escolha == 1: # Soma
        soma = a + b
        print(f'A soma de {a} + {b} = {soma}')
    elif escolha == 2:# Multiplicação
        multi = a * b
        print(f'A multiplicação de {a} * {b} = {multi}')
    elif escolha == 3: # Maior
        if a > b:
            maior = a
            print(f'O maior entre {a} e {b} é o {maior}')
        else:
            maior = b
            print(f'O maior entre {a} e {b} é o {maior}')
    elif escolha == 4: # Digitar novos números
        a = float(input('Digite um valor: '))
        b = float(input('Digite um valor: '))
    elif escolha == 5:
        print('Programa encerrado!')
        break
