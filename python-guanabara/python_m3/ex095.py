#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
def linha():
    print('--'*30)
jogadores = []
jogador =  dict()
gols = []
golsTotais = 0
while True:
    jogador['Nome'] = str(input('Nome: '))
    jogador['Partidas'] = int(input('Números de partidas: '))
    for i in range (1, jogador['Partidas'] + 1):
        golPorPartida = int(input(f'Quantos gols fez na partida {i}? '))
        gols.append(golPorPartida)
        golsTotais += golPorPartida
    jogador['gols'] = gols[:]
    jogador['golsTotais'] = golsTotais
    jogadores.append(jogador.copy())
    #Limpando os dados para o próximo loop
    gols.clear()
    golsTotais = 0
    escolha = str(input('Deseja continuar[S/N]? ')).upper()[0]
    if escolha == 'N':
         break
linha()
print(f'{"cod":<3} {"nome":<15}{"gols":<30}{"total"}')#Eu fiz o alinhamento de texto/Concatenação
for i , elemento in enumerate(jogadores):
    print(f'{i:>3} {str(elemento["Nome"]) :<15}{str(elemento["gols"]) :<30}{str(elemento["golsTotais"]) :<5}') #Tive colocar os elementos dentro do str() pois tava dando erro de TypeError: unsupported format string passed to list.__format__
linha()
escolha2 = 0
while True:
    escolha2 = int(input('Mostrar dado de qual jogador[999 para parar]? '))
    if escolha2 == 999:#Condição de parada
        break
    print(f'>>Levantamento do jogador: {jogadores[escolha2]["Nome"]}<<')

    for i in range (0, jogadores[escolha2]['Partidas']): # Vai ser números de partida de um jogador específico
        print(f'   =>Na partida {i + 1}, fez {jogadores[escolha2]["gols"][i]} gols') #Vai mostrar cada gol de cada partida, pois vai acessar primeiro um jogador específico, depois dentro do dicionário vai acessar a chave 'gols' que tem uma lista dentro e logo após vai acessar o gol da posição referente ao i
    print(f'Foi um total de {jogadores[escolha2]["golsTotais"]} gols ') #Peguei os gols totais acessando o dicionário dentro da lista