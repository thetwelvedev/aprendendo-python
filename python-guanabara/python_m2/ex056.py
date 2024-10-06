#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaIdade = 0
count = 0
maior = 0
countFem = 0
for c in range(1, 5):
    print(f'-----{c}º pessoa-----')
    nome = str(input('Digite seu nome: '))
    idade = float(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: Masculino ou Feminino: ')).lower()
    # Média de idade
    count += 1
    somaIdade += idade
    # Homem mais velho
    if sexo == 'masculino':
        # Captar o nome do homem mais velho
        if idade > maior: # Receber idade
            homemVelho = nome # Se tiver a mesma idade o primeiro que aparecer é o mais velho
            maior = idade # Recebendo maior idade agora
    # Mulheres com mais de 20 anos
    if sexo == 'feminino' and idade < 20:
        countFem += 1

media = somaIdade / count
print(f'A média de idade do grupo é {media}, o homem mais velho é o {homemVelho} e tem {countFem} mulhere(s) com menos de 20 anos.')