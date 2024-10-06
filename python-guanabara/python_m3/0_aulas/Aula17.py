#Prática da aula 17

num = [2, 5, 9, 1]
#Substitui elemento
num[2] = 3
#Adiciona elemento
num.append(7)
print(num)
num2 = [2, 5, 7, 1, 9, 15, 3]
#Deixa em ordem
num2.sort()
print(num2)
#Deixa em ordem decrescente
num2.sort(reverse=True)
print(num2)
#Len() mostra o tamanho/quantidade de elemento
print(f'Essa lista tem {len(num2)} elementos')
#insert(a,b) a é parâmetro da posição a ser inserida e b é o parâmetro do valor, ele afasta tudo que vem depois
num2.insert(2, 999)
print(num2)
#pop() remove o último elemento sem parâmetro
num2.pop()
print(num2)
#pop() remove o elemento da posição indicada com o parâmetro
num2.pop(2)
print(num2)
#remove() remove a primeira ocorência do elemento
num3 = [2, 5, 7, 1, 9, 15, 3, 3, 7573, 3873, 9]
num3.remove(9)
print(num3)
if 4 in num3:
    num.remove(4)
else:
    print('Não achei o 4!')

#Maneiras de criar listas
valores = []
valores.append(3)
valores.append(4)
valores.append(5)
#Como pecorrer os valores
for valor in valores:
    print(f'{valor}...', end='')
print() #para quebrar linha do outro código
#Com valores e o índice
for índice, valor in enumerate(valores):
    print(f'Na posição {índice} encontrei o {valor}!')
#Pegando valores do teclado para lista
nomes = list() #pode ser só []
#for cont in range(0, 5):
#    nomes.append(str(input('Digite um nome: ')))
#print(nomes)

#Multiplas listas
a = [1,2,3]
b = a #As listas estão ligadas se alterar em uma altera na outra
print(a)
print(b)
b[2] = 8
print(a)
print(b)
#Para criar clone/copia
a = [1,2,3]
b = a[:]
print(a)
print(b)
b[2] = 8
print(a)
print(b)