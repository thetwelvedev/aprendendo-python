#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anoAtual = date.today().year
anoDeNascimento = int (input('Ano de nascimento: '))
idade = anoAtual - anoDeNascimento

if idade < 18:
    print(f'Você ainda vai se alistar, falta {18 - idade} ano(s)!') # 18  - idade = quanto falta para o ano do alistamento
elif idade == 18:
    print('Você deve se alistar esse ano!')
elif idade > 18:
    print(f'Você devia ter se alistado há {anoAtual - (18 + anoDeNascimento)} ano(s)!') # anoAtual - (18 + anoDeNascimento) = tem que passou para o alistamento
