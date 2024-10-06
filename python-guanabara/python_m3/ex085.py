#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente.
numeros = []
par = []
impar = []
for i in range(0, 7):
    num = int(input(f'Digite 0 {i + 1}° número: '))
    #Ver qual é ímpar e qual é par
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
#Como vão ser apenas duas listas adcionar só no final
numeros.append(par[:])
numeros.append(impar[:])
print(numeros)
par.sort() #Deixar em ordem crescente
print(f'O números pares foram: {par}')
impar.sort()
print(f'O números ímpares foram: {impar}')