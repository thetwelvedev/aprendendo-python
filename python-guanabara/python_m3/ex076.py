#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ('Caderno', 20.00,
            'Lápis', 1.00,
            'Borracha', 2.50,
            'Estojo', 15.90,
            'Tesoura', 8.49,
            'Caneta', 1.49,
            'Livro', 34.49,
            'Mochila', 145.99)
for i in range(0, len(listagem)):
    if i % 2 == 0: # só os pares
        print(f'{listagem[i]:.<30}', end='')# < depois do : significa que tudo vai ficar a esquerda/ e o que ficar entre o : e < vai aparecer no espaço determinado pelo número
    if i % 2 != 0: # Só os impares
        print(f'R${listagem[i]:>7.2f}')# o :>7 significa que vai ficar tabulado a direita um espaço de 7/o número de casa do float tem que aparecer depois