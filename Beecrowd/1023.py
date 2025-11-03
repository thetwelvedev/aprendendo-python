"""Devido às constantes estiagens que aconteceram nos últimos tempos em algumas regiões do Brasil, o governo federal criou um órgão para a avaliação do consumo destas regiões com finalidade de verificar o comportamento da população na época de racionamento. Este órgão responsável irá pegar algumas cidades (por amostragem) e verificará como está sendo o consumo de cada uma das pessoas da cidade e o consumo médio de cada cidade por habitante."""
def main():
    cidade = 1
    while True:
        N = int(input())
        if N == 0:
            break

        consumo = [0] * 201  # agrupa direto por consumo por pessoa
        total_pessoas = 0
        total_consumo = 0

        for _ in range(N):
            X, Y = map(int, input().split())
            c = Y // X
            consumo[c] += X
            total_pessoas += X
            total_consumo += Y

        if cidade > 1:
            print()
        print(f"Cidade# {cidade}:")
        cidade += 1

        primeiro = True
        for c in range(201):
            if consumo[c] > 0:
                if not primeiro:
                    print(" ", end="")
                print(f"{consumo[c]}-{c}", end="")
                primeiro = False
        print()

        media = total_consumo / total_pessoas
        truncado = int(media * 100)
        print(f"Consumo medio: {truncado / 100:.2f} m3.")

if __name__ == "__main__":
    main()
