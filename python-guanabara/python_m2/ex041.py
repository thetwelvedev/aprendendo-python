#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
'''– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''
from datetime import date
anoDeNascimento = int(input('Digite sua data de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoDeNascimento
print('Sua categoria é a:',end=' ')
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JÚNIOR')
elif 19 < idade <= 25:
    print('SÊNIOR')  
else: 
     print('MASTER') 