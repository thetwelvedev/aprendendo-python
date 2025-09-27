"""Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago."""
codigo_peca1, numero_de_pecas1, valor_unitario1 = input().split()
codigo_peca2, numero_de_pecas2, valor_unitario2 = input().split()
valor_total = (int(numero_de_pecas1) * float(valor_unitario1)) + (int(numero_de_pecas2) * float(valor_unitario2))
print(f"VALOR A PAGAR: R$ {valor_total:.2f}")