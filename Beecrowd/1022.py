"""A tarefa aqui neste problema é ler uma expressão matemática na forma de dois números Racionais (numerador / denominador) e apresentar o resultado da operação. Cada operando ou operador é separado por um espaço em branco. A sequência de cada linha que contém a expressão a ser lida é: número, caractere, número, caractere, número, caractere, número. A resposta deverá ser apresentada e posteriormente simplificada. Deverá então ser apresentado o sinal de igualdade e em seguida a resposta simplificada. No caso de não ser possível uma simplificação, deve ser apresentada a mesma resposta após o sinal de igualdade.

Considerando N1 e D1 como numerador e denominador da primeira fração, segue a orientação de como deverá ser realizada cada uma das operações:
Soma: (N1*D2 + N2*D1) / (D1*D2)
Subtração: (N1*D2 - N2*D1) / (D1*D2)
Multiplicação: (N1*N2) / (D1*D2)
Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)"""
import math

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

n = int(input())

for _ in range(n):
    partes = input().split()

    # Caso a entrada venha no formato com espaços entre tudo: "1 / 2 + 3 / 4"
    if len(partes) == 7:
        N1 = int(partes[0])
        D1 = int(partes[2])
        op = partes[3]
        N2 = int(partes[4])
        D2 = int(partes[6])
    # Caso a entrada venha compacta: "1/2 + 3/4"
    elif len(partes) == 3:
        N1, D1 = map(int, partes[0].split('/'))
        op = partes[1]
        N2, D2 = map(int, partes[2].split('/'))
    else:
        continue  # formato inesperado, pula

    if op == '+':
        NR = N1 * D2 + N2 * D1
        DR = D1 * D2
    elif op == '-':
        NR = N1 * D2 - N2 * D1
        DR = D1 * D2
    elif op == '*':
        NR = N1 * N2
        DR = D1 * D2
    elif op == '/':
        NR = N1 * D2
        DR = N2 * D1

    # Simplificação
    div = math.gcd(abs(NR), abs(DR))
    simpN = NR // div
    simpD = DR // div

    print(f"{NR}/{DR} = {simpN}/{simpD}")