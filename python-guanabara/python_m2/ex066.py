#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um número inteiro[Digite 999 para parar]: '))
    if n == 999: # Quando for 999 digitado
        break
    #Coloquei depois da flag para quando dar break não contar que o número 999
    cont += 1 # Contador
    soma += n 
print(f'Foram digitados {cont} números e sua soma deu {soma}.')