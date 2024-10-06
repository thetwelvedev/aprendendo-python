#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex.: 6.127 -> 6
from math import floor
num = float(input('Digite um número[ex.: 6.127]: '))
print(f'A parte inteira do número é {floor(num)}') # floor arredonda pra baixo o número