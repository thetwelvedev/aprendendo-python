#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome = 'Desconhecido', gol = 0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

nomeJogador = str(input('Digite o nome do jogador: '))
golsStr = str(input('Quantos gols no campeonato: '))
if golsStr.isnumeric(): #Se for númerico vai transformar em inteiro
    golsInt = int(golsStr)
else: #Se não for é igual a 0
    golsInt= 0
if nomeJogador.strip() == '': #Quando escrever só vai printar
    ficha()
else:
    ficha()