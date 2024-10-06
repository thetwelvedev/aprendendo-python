#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
cadastro = []
while True:
    #Coletando Dados
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    cadastro.append([nome, [nota1, nota2], media])
    escolha = str(input('Deseja continuar[S/N]? '))[0].upper()
    if escolha == 'N':
        break
print('-='*20)
print(f"{'No.':<3}", f"{'NOME':<10}", f"{'MÉDIA':<5}")
print('--'*20)
# Aqui o i é o índice, cada lista dentro da lista cadastro é o aluno(com os dados de nome, notas e média) e isso vai ser percorrido em cadastro através do enumerate
for i, aluno in enumerate(cadastro):
    print(f'{i:<3}', f'{aluno[0]:<10}', f'{aluno[2]:>5.1f}')
print('--'*20)
#Aqui como são dados de uma lista dentro da lista mas a posição dos dados são sempre as mesmas eu só mudo a posição das listas que estão dentro da lista cadastro
while True:
    escolhaMedia = int(input('Deseja ver a nota e qual aluno? [No.]: '))
    print(f'Notas de {cadastro[escolhaMedia][0]} são {cadastro[escolhaMedia][1]}')
    escolha = str(input('Deseja continuar[S/N]? '))[0].upper()
    if escolha == 'N':
        break