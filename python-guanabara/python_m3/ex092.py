#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
anoAtual = date.today().year
dadosPessoais = dict()
dadosPessoais['Nome'] = str(input('Nome: '))
dadosPessoais['Idade'] = anoAtual - int(input('Ano de nascimento: ')) 
dadosPessoais['CTPS'] = int(input('Número da Carteira de Trabalho[0 se não tem]: '))
print('>'*20, end='')
print('<'*20)
for k, v in dadosPessoais.items():
    print(f'{k} tem o valor {v}')