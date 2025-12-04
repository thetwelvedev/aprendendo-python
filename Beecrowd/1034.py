"""Todos os anos, artistas de todo o mundo se reúnem na cidade, onde fazem esculturas de gelo gigantescas. A cidade vira uma galeria de arte ao céu aberto, uma vez que as esculturas ficam expostas na rua por semanas, sem derreter. Afinal, a temperatura média no inverno de Harbin (época em que ocorrerá a final mundial do ICPC) é de -20 graus.

O primeiro passo para fazer a escultura é montar um grande bloco de gelo da dimensão pedida pelo artista. Os blocos são recortados das geleiras de Harbin em blocos de altura e profundidade padrão e vários comprimentos diferentes. O artista pode determinar qual o comprimento que ele deseja que tenha o seu bloco de gelo para que a escultura possa começar a ser esculpida.

Os comprimentos disponíveis dos blocos são {a1; a2; ...;  aN} e o comprimento que o artista deseja é M. O bloco de comprimento 1 é muito usado, por este motivo ele sempre aparece na lista de blocos disponíveis. Sua tarefa é determinar o número mínimo de blocos tal que a soma de seus comprimentos seja M."""
import sys

def solve():
    input = sys.stdin.readline
    T = int(input().strip())

    for _ in range(T):
        N, M = map(int, input().split())
        coins = list(map(int, input().split()))
        coins.sort()

        # DP para mínimo número de blocos
        INF = 10**9
        dp = [INF] * (M + 1)
        dp[0] = 0

        for c in coins:
            for x in range(c, M + 1):
                if dp[x - c] + 1 < dp[x]:
                    dp[x] = dp[x - c] + 1

        print(dp[M])

