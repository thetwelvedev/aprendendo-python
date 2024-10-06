#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:   
    escolha = int(input('Digite um número entre 0 a 20: '))
    if 0 <= escolha <= 20:
        print(f'O número por escrito fica {numeros[escolha]}!') #Vai printar exatamente o correspondente
        break
    else:
        print('Tente novamente. ', end = '')