#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
numeroSorteado = randint(1,5)
numeroUsuario = int(input('Adivinhe um número entre 0 e 5: '))
if (numeroUsuario == numeroSorteado):
    print('Você acertou!')
else:
    print('Você errou!')