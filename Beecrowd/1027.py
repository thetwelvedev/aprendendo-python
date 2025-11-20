"""A tarefa é simples. Através de alguns pontos críticos em 2D, você deve desenhar uma onda como uma curva. Seu objetivo é incluir tantos pontos quantos forem possível.

Haverá uma linha imaginária y = a, a qual chamaremos de eixo principal para a curva.
Todos os pontos na curva deverão ter diferentes coordenadas x. Suas coordenadas y devem ser na forma a-1 ou a+1.
Dois pontos consecutivos na curva devem ter diferença de 2 na coordenada y."""

import sys
from collections import defaultdict

def max_wave(points_low, points_high):
    # Ordena por x
    low = sorted(points_low)
    high = sorted(points_high)

    def simulate(start_low: bool):
        i = j = 0
        count = 0
        last_x = -10**9
        want_low = start_low

        while True:
            if want_low:
                # procura o menor x > last_x em low
                while i < len(low) and low[i] <= last_x:
                    i += 1
                if i == len(low):
                    break
                last_x = low[i]
                i += 1
            else:
                # procura o menor x > last_x em high
                while j < len(high) and high[j] <= last_x:
                    j += 1
                if j == len(high):
                    break
                last_x = high[j]
                j += 1

            count += 1
            want_low = not want_low

        return count

    return max(simulate(True), simulate(False))

def main():
    data = sys.stdin.read().replace('–', '-').split()
    p = 0

    while p < len(data):
        n = int(data[p])
        p += 1
        if n == 0:
            print(0)
            continue

        by_y = defaultdict(set)

        for _ in range(n):
            x = int(data[p])
            y = int(data[p+1])
            p += 2
            by_y[y].add(x)

        ans = 1

        for y in by_y:
            if y + 2 in by_y:
                ans = max(ans, max_wave(by_y[y], by_y[y+2]))

        print(ans)

if __name__ == "__main__":
    main()