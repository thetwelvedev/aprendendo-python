# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
'''A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
PrecoTotal = 0
cont1000 = 0
menor = 0
produtoBarato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    PrecoTotal += preco # Vai armazenar todo o preço
    if preco > 1000:
        cont1000 += 1
    # Parar o loop
    escolha = str(input('Quer continuar?[S/N] '))[0].upper()
    if escolha == 'N':
        break
    # Menor valor
    if menor > preco or menor == 0:# Aqui tanto se o novo preco for menor quanto quando menor tem o valor 0 ele vai receber esse novo valor
        menor = preco
        produtoBarato = produto # Receber o nome do produto mais barato

print(f'''Total gasto: R${PrecoTotal:.2f}
Quantidade de produto que custa mais de mil: {cont1000}
Produto mais barato: {produtoBarato}''')