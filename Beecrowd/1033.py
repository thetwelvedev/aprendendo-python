"""Os números de fibonacci são definidos pela seguinte recorrência:

fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1)+fib(n-2)
Mas não estamos interessados em números de Fibonacci aqui. Gostaríamos de saber quantas chamadas recursivas seriam necessárias para um determinado número de Fibonacci n, seguindo a recorrência normal. Uma vez que os números serão bem grandes, não será uma tarefa muito simples para você. Mas então vamos torná-la um pouco mais fácil: queremos que você apresente somente o ultimo dígito do numero de chamadas, onde este número deve estar na base b."""
b = 0


class Matriz:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.M = [[0 for _ in range(m)] for _ in range(n)]

    def __mul__(self, outra):
        global b
        resposta = Matriz(self.m, outra.n)

        for i in range(self.n):
            for j in range(outra.m):
                for k in range(self.m):
                    resposta.M[i][j] += self.M[i][k] * outra.M[k][j]
                    resposta.M[i][j] %= b

        return resposta


def potencia(base, expoente):
    if(expoente == 1):
        return base
    elif(expoente % 2):
        return base * potencia(base, expoente - 1)
    else:
        pot = potencia(base, expoente // 2)
        return pot * pot


T = 1
while True:
    try:
        n, b = [int(x) for x in input().strip().split(' ')]

        if(n == 0 and b == 0):
            break

        A = Matriz(3, 3)
        A.M[0][0] = 1
        A.M[0][1] = 1
        A.M[0][2] = 1
        A.M[1][0] = 1
        A.M[2][2] = 1

        B = Matriz(3, 1)
        B.M[0][0] = 1
        B.M[1][0] = 1
        B.M[2][0] = 1

        if(n < 2):
            print(f'Case {T}: {n} {b} 1')
        else:
            An1 = potencia(A, n - 1)
            R = An1 * B

            print(f'Case {T}: {n} {b} {R.M[0][0]}')

        T += 1
    except EOFError:
        break