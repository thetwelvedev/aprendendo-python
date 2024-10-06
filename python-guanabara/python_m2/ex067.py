#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
n = 0
while n >= 0:
    n = float(input('Digite um número e saiba sua tabuada: '))
    print('-'*30)
    if n >= 0:
        for c in range(1, 11):
            print(f'{n} x {c} = {n * c}')
    else:
        print('Programa encerrado!')
    print('-'*30)