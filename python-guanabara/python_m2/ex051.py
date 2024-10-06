#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
a1 = float(input('Digite o primeiro termo: '))
r = float(input('Qual a razão? '))
cont = 0
for n in range(1, 11):  
    an = a1 + (n -1)*r
    cont += 1
    print(f'A termo {cont}º da progressão é {an}')
print('Acabou')