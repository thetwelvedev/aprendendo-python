#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
menor = 0
maior = 0
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if menor == 0:
        menor = peso # Como peso = 0 inicialmente ele vai ser o menor valor fiz esse para ele receber o peso
    if menor > peso:
        menor = peso #Tem que receber um valor para comparar
    if maior < peso:
        maior = peso #Tem que receber um valor para comparar
    if menor > maior:
        maior = menor #Caso o menor tiver com maior valor  ele passa para o maior
print(f'O menor peso foi {menor}kg e maior peso foi {maior}kg')

