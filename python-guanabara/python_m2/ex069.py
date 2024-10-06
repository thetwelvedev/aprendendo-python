#Crie um programa que leia a idade e o sexo de várias pessoas.A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
'''A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
contIdade = 0
contMasc = 0
contFem20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo[M/F]: '))[0].upper()
    if idade > 18:
        contIdade += 1 # contador de pessoas com mais de 18 anos
    if sexo == 'M':
        contMasc += 1 # contador de homems
    if idade < 20 and sexo == 'F':
        contFem20 += 1 # contador de mulheres com menos de 20
    escolha = str(input('Quer continuar?[S/N] '))[0].upper()
    if escolha == 'N':
        break
print(f'''Pessoas com mais de 18: {contIdade}
Quantidade de homems: {contMasc}
Quantidade de mulheres com menos de 20 anos: {contFem20}''')