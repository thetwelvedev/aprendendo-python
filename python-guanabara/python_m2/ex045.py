# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
escolhaUsuario = int(input('''Você escolhe sua opção:
[1]Pedra
[2]Papel                           
[3]Tesoura
Sua opção: '''))
print('-='*26)
#Pegar os nomes das opções do usuário
if escolhaUsuario == 1:
    escolhaUsuario = 'Pedra'
elif escolhaUsuario == 2:
    escolhaUsuario = 'Papel'
elif escolhaUsuario == 3:
    escolhaUsuario = 'Tesoura'

#Pegar os nomes das opções da máquina
escolhaMaquina = randint(1,3)
if escolhaMaquina == 1:
    escolhaMaquina = 'Pedra'
elif escolhaMaquina == 2:
    escolhaMaquina = 'Papel'
elif escolhaMaquina == 3:
    escolhaMaquina = 'Tesoura'

#Comparar as escolhas da máquina e usuário
print(f'Você escolheu {escolhaUsuario} e a máquina {escolhaMaquina}! ', end='') # Mostra as escolhas
if escolhaUsuario == escolhaMaquina:
    print('EMPATE!')
elif escolhaUsuario != escolhaMaquina: # As possibilidades que não são empate
    if escolhaUsuario == 'Pedra' and escolhaMaquina == 'Papel':
        print('Você PERDEU!')
    elif escolhaUsuario == 'Pedra' and escolhaMaquina == 'Tesoura':
        print('Você VENCEU!')
    elif escolhaUsuario == 'Papel' and escolhaMaquina == 'Pedra':
        print('Você VENCEU!')    
    elif escolhaUsuario == 'Papel' and escolhaMaquina == 'Tesoura':
        print('Você PERDEU!')
    elif escolhaUsuario == 'Tesoura' and escolhaMaquina == 'Pedra':
        print('Você PERDEU!')    
    elif escolhaUsuario == 'Tesoura' and escolhaMaquina == 'Papel':
        print('Você VENCEU!') 
print('-='*26)
print('FIM DE JOGO!')
print('-='*6)