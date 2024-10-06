#Prática da aula 18
#Primeiro teste
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #Pegou teste só com gustavo e 40
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #Aqui pegou teste mas com maria e 22 substituindo gustavo e 40
print(galera)
print('-='*30)
#Segundo teste
galera2 = [['João', 19], ['Maria', 15], ['Ana', 20], ['Caio', 8]]
print(galera2)
for p in galera2:
    print(p[0]) #vai aparecer só os nomes pois todos os p[0] são nomes, já que aqui p representa cada lista dentro da lista
print('-='*30)
for p in galera2:
    print(p[1]) #vai aparecer só os nomes pois todos os p[1] são idades, já que aqui p representa cada lista dentro da lista
print('-='*30)
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos de idade.')
#Terceiro teste

#Lendo os dados
pessoas = list()
dado = list()
totalMaiorDeIdade = totalMenorDeIdade = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:]) # Cada loop ele coloca a lisat dados com dois elementos dentro da lista pessoas
    dado.clear() # Para lista tá limpa para o próximo loop
print(pessoas)

#Analisando os dados
for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        totalMaiorDeIdade += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totalMenorDeIdade += 1
print(f'Tem {totalMaiorDeIdade} maiores e {totalMenorDeIdade} menores de idade')