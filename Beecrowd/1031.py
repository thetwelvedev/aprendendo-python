"""Durante uma crise de energia na Nova Zelândia no inverno passado (causada por uma escassez de chuva e, consequentemente, por causa dos níveis baixos nas barragens hidrográficas), um esquema de contingência foi desenvolvido para desligar a energia para as áreas do país de forma sistemática, de uma forma totalmente justa. O país foi dividido em N regiões (Auckland seria a região número 1 e Wellington a número 13). Um número, m, seria escolhido randomicamente e a energia deveria ser desligada primeiro na região 1 (claramente o ponto de início mais justo) e então em cada m região após esta, indo de uma a outra região e ignorando as regiões já desligadas. Por exemplo, se N = 17 e m = 5, a energia deverá ser desligada em todas as regiões seguindo a seguinte ordem: 1,6,11,16,5,12,2,9,17,10,4,15,14,3,8,13,7.
O problema é que, claramente seria mais justo desligar a região de Wellington por último (Isso porque é onde a sede da empresa se encontra). Portanto, para um dado N (regiões), o número aleatório m (salto) precisa ser cuidadosamente escolhido de forma que a região 13 seja a última região a ser escolhida.
Escreva um programa que leia o número de regiões e determine o menor número m que assegure que Wellington (região 13) possa continuar funcionando enquanto o resto do país esteja desligado."""
def remaining(n, k):
    r = 0
    i = 1

    while i < n:
        r = (r+k) % i

        i += 1
    return r 


while True:
    num = int(input())
    if num == 0:
        break
    y = 1
    while True:
        if remaining(num, y) != 11:
            y += 1
        else:
            break
    print(y)