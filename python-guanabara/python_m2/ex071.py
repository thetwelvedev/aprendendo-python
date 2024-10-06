'''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
saque = int(input('Quanto deseja sacar: '))
total = saque
ced = 50
contCed = 0
while True:
    if total >= ced: # Se é maior que o valor atual da cédula vai realizar as operações
        total -= ced # vai tirar o valor atual quantas vezes for necessário
        contCed += 1
    else: # Quando não tiver mais como tirar o valor atual
        if contCed > 0: # Só vai aparecer caso tenha quantidade de pelo menos 1 cédula
            print(f'Total de cédulas de R${ced}: {contCed}')# Vai pegar o valor da cédula e quantas Cédulas antes de entrar no loop com o valor nome e assim sucessivamente
        if ced == 50: # Quando não for mais divível por 50
            ced = 20 # Agora o novo valor é 20
        elif ced == 20: # Quando não for mais divível por 20
            ced = 10 # Agora o novo valor é 10
        elif ced == 10: # Quando não for mais divível por 10
            ced = 1 # Agora o novo valor é 1
        contCed = 0 # Pois o próximo loop será com um novo valor de cédula
        if total == 0: # Encerar o programa
            break