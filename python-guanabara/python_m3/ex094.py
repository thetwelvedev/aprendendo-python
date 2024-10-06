#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
'''No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''
pessoas = []
mulheresCadastradas = []
idadeSomada = 0
while True:
    pessoa = dict()
    pessoa['Nome'] = str(input('Nome: '))
    
    sexo = str(input('Sexo [M/F]: ')).upper()[0]
    if sexo == 'M' or sexo == 'F':
        pessoa['Sexo'] = sexo
        if sexo  == 'F':#Quando for mulher coloco numa lista
            mulheresCadastradas.append(pessoa['Nome'])
    else: #Quando usuário errar a opcão
        print('ERRO! Responda apenas com M ou F')
        sexo = str(input('Sexo [M/F]: ')).upper()[0]
        if sexo  == 'F':#Quando for mulher coloco numa lista
            mulheresCadastradas.append(pessoa['Nome'])
    
    pessoa['Idade'] = int(input('Idade: '))
    idadeSomada += pessoa['Idade'] #Somo todas as idade
    pessoas.append(pessoa.copy())

    escolha = str(input('Deseja continuar[S/N]? ')).upper()[0]
    if escolha == 'N':
         break
    if escolha != 'S': #Quando usuário errar a opcão
        print('ERRO! Responda apenas com S ou N')
        escolha = str(input('Deseja continuar[S/N]? ')).upper()[0]
        if escolha == 'N':
            break

print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
#Média
mediaIdade = idadeSomada / len(pessoas)
print(f'A média de idade é {mediaIdade:.2f} anos')
#Mulheres cadastradas
print('As mulheres cadastradas foram: ', end='')
for i in range(0, len(mulheresCadastradas)):
    print(f'{mulheresCadastradas[i]}', end= ' ')
print()
#Acima da idade média
print('Lista de pessoas com idade acima da média:')
for elemento in pessoas:#Em teoria ele vai elemento por elemento e print vazio vai quebrar a linha depois de terminar o dado do elemento
    if elemento['Idade'] > mediaIdade: #Vai verificar de cada elemento a idade e ver se é maior que a média
        for k, v in elemento.items(): #Aqui ele vai pegar os dados de cada elemento
                print(f'{k} = {v}; ', end= '')
        print()