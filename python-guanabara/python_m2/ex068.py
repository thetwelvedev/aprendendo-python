# Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
number = 0
cont = 0
while True:
    print('-='*30)
    number = int(input('Digite um número: '))
    escolha = str(input('Par ou ímpar[P/I]: '))[0].upper()
    numberMaquina = randint(1,10)
    soma = number + numberMaquina
    if escolha == 'P':
        if soma % 2 == 0:
            print('-'*60)
            print(f'Você escolheu {number} e Máquina escolheu {numberMaquina}. Deu {soma} e é PAR!')
            print('-'*60)
            print('Você VENCEU!')
            cont += 1
        else:
            print('-'*60)
            print(f'Você escolheu {number} e Máquina escolheu {numberMaquina}. Deu {soma} e é IMPAR!')
            print('-'*60)
            print('Você PERDEU!')
            break
    if escolha == 'I':
        if soma % 2 == 0:
            print('-'*60)
            print(f'Você escolheu {number} e Máquina escolheu {numberMaquina}. Deu {soma} e é PAR!')
            print('-'*60)
            print('Você PERDEU!')
            break
        else:
            print('-'*60)
            print(f'Você escolheu {number} e Máquina escolheu {numberMaquina}. Deu {soma} e é IMPAR!')
            print('-'*60)
            print('Você VENCEU!')
            cont += 1
print('-='*30)
print(f'GAME OVER! {cont} vitória(s)!!!')