#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Digite um número: '))
print(f'Calculando {n}! = ',end='') # Esse end ='' é para juntar com o próximo print
fat = 1
while n != 0:
    fat = fat * n # Aqui o fatorial vai recebendo os números decrescidos e multiplicando pelo anterior
    if n != 1:
        print(f'{n} x ', end='') # Como o 1 é o último e ele vai ter que aparecer com um igual depois dele fiz essa condição
    else:
        print(f'{n} = {fat} ', end='') # Para mostrar a parte final do resultado
    n -= 1 # como o fatorial vai mutiplicando pelo número decrescido coloquei e contador -1
