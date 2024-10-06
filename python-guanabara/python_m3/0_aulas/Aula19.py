#Dicionários
def linha():
    print('-='*20)

linha()
dados = dict()
dados = {'nome': 'pedro', 'idade': 25} #Agora os dados tem um nome ao ínves de um índice
print(dados['nome'])
print(dados['idade'])
linha()

#Adiconar elemento
dados['sexo'] = 'M'

#Remover elemento
del dados['idade']
print(dados)
linha()

#Outro exemplo
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas',}
#Valores
print(filme.values())
#Keys
print(filme.keys())
#Tudo
print(filme.items())
linha()

#Usando o for
for k, v in filme.items():
    print(f'O {k} é {v}')
#Posso interagir listas, dicionários e tuplas
linha()

#Prática
pessoas = {'nome': 'Pedro', 'sexo': 'M', 'idade': 25}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
linha()
for k in pessoas.keys():
    print(k)
linha()
for v in pessoas.values():
    print(v)
linha()
for k, v in pessoas.items(): #substitui o enumerate de tupla e lista
    print(f'O {k} é {v}')
linha()

#Criando um discinário dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
linha()
print(brasil[0])
linha()
print(brasil[1])
linha()
print(brasil[0]['uf'])
linha()

#Outro exemplo 
estado =  dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) # o copy() é o [:] da lista, já que se não clonar vai manter o elo e modificar sempre o mesmo dado, assim colocando dado repitido
print(brasil)
linha()
for e in brasil: #Vai pegar cada dicionário dentro da lista
    for k, v in e.items(): #Vai pegar cada key e values de cada dicionário
        print(f' O campo {k} tem valor {v}')