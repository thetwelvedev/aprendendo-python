#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um outro número: '))
n3 = float(input('Digite um outro número: '))

# Maior
if n1 >= n2 and n3: # n1 maior ou igual que n2 e n3
    maior = n1
if n2 >= n1 and n3: # n2 maior ou igual que n1 e n3
    maior = n2
if n3 >= n1 and n2: # n3 maior ou igual que n1 e n2
    maior = n3

#Menor
if n1 <= n2 and n3: # n1 menor ou igual que n2 e n3
    menor = n1
if n2 <= n1 and n3: # n2 menor ou igual que n1 e n3
    menor = n2
if n3 <= n1 and n2: # n3 menor ou igual que n1 e n2
    menor = n3
#Coloquei a igualdade pois pode ser que se repita os números
print(f'O {menor} é o menor número e o {maior} é o maior número')
