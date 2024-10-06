#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
def linha():
    print('<>'*20)
jogador =  dict()
jogador['Nome'] = str(input('Nome: '))
jogador['Partidas'] = int(input('Números de partidas: '))
gols = []
golsTotais = 0
for i in range (1, jogador['Partidas'] + 1):
    golPorPartida = int(input(f'Quantos gols fez na partida {i}? '))
    gols.append(golPorPartida)
    golsTotais += golPorPartida
jogador['gols'] = gols
jogador['golsTotais'] = golsTotais
linha()
print(jogador)
linha()
for k, v in jogador.items():
    print(f'O {k} tem valor {v}')
linha()
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas')
for i in range (0, jogador['Partidas']): # fiz o range normal pois na lista o range começa no 0 
    print(f'   =>Na partida {i + 1}, fez {gols[i]} gols')
print(f'Foi um total de {jogador["golsTotais"]} gols ')