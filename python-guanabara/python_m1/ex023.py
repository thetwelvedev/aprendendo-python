#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''Ex.: número: 1834 unidade: 4, dezena: 3, centena: 8, milhar: 1 '''
number = str(input('Digite um número inteiro entre 0 e 9999: '))
unidade = number[-1] #Colacando negativo ele vai contando de trás para frente
dezena = number[-2]
centena = number[-3]
milhar = number[-4]

print(f'''Unidade: {number[-1]}
Dezena: {number[-2]}
Centena: {number[-3]}
Milhar: {number[-4]}''')