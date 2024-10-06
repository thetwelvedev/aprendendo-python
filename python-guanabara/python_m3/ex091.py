#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)} #Inicialmente linha feito cada jogador um dicionário individual e coloquei numa lista mas na hora de usar o key e values percebi que podia ser tudo dentro do mesmo dicionário já que não vou mudar os dados
print('Valores sorteados: ')
ranking = []
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogadores.items(), key= itemgetter(1), reverse=True) # Se fosse 0 seria por ordem de key e como é 1 é por ordem de values/ o reverse=True deixa na ordem decrescente
#E no sorted usa jogadores.items() pois pega as keys e os values
print('>>> Ranking de jogadores <<<')
contador = 1
for elemento in ranking:
    print(f'{contador} Lugar - {elemento[0]} ficou com {elemento[1]}')
    contador += 1
    sleep(1)
#Guanabas usou
for i, v in enumerate(ranking):
    print(f'{i + 1}° Lugar - {v[0]} ficou com {v[1]}')
    sleep(1)