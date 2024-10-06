#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um número: '))
escolha = int(input('''Escolha uma das bases para conversão: 
[1] Para binário
[2] Para Octal
[3] para Hexadecimal
Sua opção: '''))

if escolha == 1:
    print(f'O número {n} em binário é {bin(n)[2:]}') #bin() conversor de binário
elif escolha == 2:
    print(f'O número {n} em binário é {oct(n)[2:]}') #oct() conversor de octal
elif escolha == 3:
    print(f'O número {n} em binário é {hex(n)[2:]}') #hex() conversor de hexadecimal
    #[2:] serve para retirar a posição 0 e 1 pois ele começa da posição  2
else:
    print('Não tem essa opção')