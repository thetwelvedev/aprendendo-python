"""Raju e Meena adoram jogar um jogo diferente com pequenas peças de mármores, chamados Marbles. Eles têm um monte destas peças com números escritos neles. No início, Raju colocaria estes pequenos mármores um após outro em ordem ascendente de números escritos neles. Então Meena gostaria de pedir a Raju para encontrar o primeiro mármore com um certo número. Ele deveria contar 1...2...3. Raju ganha um ponto por cada resposta correta e Meena ganha um ponto se Raju falha. Depois de um número fixo de tentativas, o jogo termina e o jogador com o máximo de pontos vence. Hoje é sua chance de jogar com Raju. Sendo um/a cara esperto/a, você tem em seu favor o computador. Mas não subestime Meena, ela escreveu um programa para monitorar quanto tempo você levará para dar todas as respostas. Portanto, agora escreva o programa, que ajudará você em seu desafio com Raju."""
def busca_primeiro(arr, x):
    inicio, fim = 0, len(arr) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if arr[meio] == x:
            resultado = meio
            fim = meio - 1  # continua à esquerda
        elif arr[meio] > x:
            fim = meio - 1
        else:
            inicio = meio + 1
    return resultado


def main():
    caso = 1
    while True:
        n, q = map(int, input().split())
        if n == 0 and q == 0:
            break

        marmores = [int(input()) for _ in range(n)]
        marmores.sort()

        print(f"CASE# {caso}:")
        caso += 1

        for _ in range(q):
            x = int(input())
            pos = busca_primeiro(marmores, x)
            if pos != -1:
                print(f"{x} found at {pos + 1}")
            else:
                print(f"{x} not found")


if __name__ == "__main__":
    main()
