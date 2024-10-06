#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
anoAtual = date.today().year
contMaior = 0
contMenor = 0
for c in range (1, 7):
    anoDeNascimento = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    idade = anoAtual - anoDeNascimento
    if idade < 21:
        contMenor += 1
    else:
        contMaior += 1

print(f'Número de pessoas menores de idade: {contMenor}')
print(f'Número de pessoas maiores de idade: {contMaior}')