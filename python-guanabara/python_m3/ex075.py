#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
d = int(input('Digite um número: '))
tupla = (a ,b ,c , d)
# A) Quantas vezes apareceu o valor 9.
count = 0
if a == 9:
    count += 1
if b == 9:
    count += 1
if c == 9:
    count += 1
if d == 9:
    count += 1
# B) Em que posição foi digitado o primeiro valor 3.
posição = tupla.index(3)
# C) Quais foram os números pares.
listaPar =[]
par = 0
for i in range(len(tupla)): # Vai pecorrer a tupla no tamanho exato dela 
    if tupla[i] % 2 == 0:
        listaPar.append(tupla[i]) # Vai armazenar os valores
        par += 1
#Prints
print(f'''Você digitou os valores {tupla} 
Quantidade de 9: {count}
A posição do primeiro 3: {posição + 1}°
Quantidade de número par: {par} e são eles {listaPar}''')