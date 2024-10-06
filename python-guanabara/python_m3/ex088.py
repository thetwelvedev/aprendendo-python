#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
palpites = []
jogoDaMegaSena = []
print('-'*40)
print(f"{'JOGA NA MEGA SENA':^40}")
print('-'*40)
escolhaDeJogos = int(input('Quantos jogos deseja sortear? '))
for i in range(0, escolhaDeJogos): #Quantidade de jogos que seram feitos
    contador = 0
    while True: #Formando os jogos da mega sena que são 6 números
        num = randint(1,60)
        if num not in jogoDaMegaSena:
            jogoDaMegaSena.append(num)
            contador += 1
        if contador == 6:
            break
    jogoDaMegaSena.sort() #Vai deixar em ordem crescente
    palpites.append(jogoDaMegaSena[:]) #Pegando uma lista clonada para não ter elo com a lista quando for modificada
    jogoDaMegaSena.clear()
    #Printando os valores
    if i == 0: #Para printar apenas antes do primeiro jogo
        print('-='*3, f' SORTEANDO {escolhaDeJogos} JOGOS ', '-='*3)
    sleep(1)
    print(f'Jogo {i + 1}: {palpites[i]}')
    if i == 5:
        print('-='*5, '< BOA SORTE! >', '-='*5)