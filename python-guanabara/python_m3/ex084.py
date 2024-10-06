#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:  
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
cadastro = []
pessoa = []
maiorPeso = menorPeso = 0
pessoaMaior = pessoaMenor = ''
while True:
    #Coletando os dados
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))

    #Analisando os dados
    for p in cadastro:
        if p[1] > maiorPeso or maiorPeso == 0:
            maiorPeso = p[1]
        if p[1] < menorPeso or menorPeso == 0:
            menorPeso = p[1]
    
    #Preparando os dados para o próximo loop
    cadastro.append(pessoa[:]) #Tem que ser a lista clone se não os dados ficam ligados e não da de alterar as coisas
    pessoa.clear() # Tem que limpar a lista que vai ser colocada dentro da outra lista pois no loop trabalhamos só com ela de lista, caso contrário teria que substituir o elemento na posição da lista

    #Quebrando o loop infinito
    escolha = str(input('Quer continuar? [S/N] ')).upper()[0]
    if 'N' in escolha:
        break

print(f'Total de pessoas cadastradas: {len(cadastro)}')
print(f'O maior peso foi {maiorPeso}kg. Peso de ', end='')
for p in cadastro:
    if p[1] == maiorPeso:
        print(f'{p[0]} ', end='') # Caso tenha mais de um ele vai colocando do lado os nomes
print(f'\nO menor peso foi {menorPeso}kg. Peso de ', end='')
for p in cadastro:
    if p[1] == menorPeso:
        print(f'{p[0]} ', end='')
#Tive que colocar esse for fora do loop pois não dava de juntar os nomes das pessoas uma do lado da outra de outra forma, claro que sem aparecer os []