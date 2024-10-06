#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# reprovado(nota<=5), recuperação(5<nota<7) e aprovado(nota>=7)
ficha = dict()
ficha['Nome'] = str(input('Digite seu nome: '))
ficha['Nota'] = int(input('Digite sua média: '))

print(f'''-O nome é igual a {ficha['Nome']}
-A média igual a {ficha['Nota']}''')
if ficha['Nota'] <= 5:
    situacao = 'Reprovado'
elif 5 < ficha['Nota'] < 7:
    situacao = 'Recuperação'
elif ficha['Nota'] >= 7:
    situacao = 'Aprovado'
print(f'-Sua situação é igual a {situacao}')