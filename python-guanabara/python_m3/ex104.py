#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
#Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(msg):
    valorInt = 0
    while True: #Foi pedido que continuasse o código até receber um valor inteiro
        scan = str(input(msg)) #Vai ler a mensagem, que nem o scanf em C/o input pode apararecer abaixo da mensagem de print
        if scan.isnumeric(): #Vai verificar se na string tem número
            valorInt = int(scan) #Transformando string em inteiro
            break #fecha o loop quando tiver um valor inteiro
        else:
            print('\033[0;31mERRO! Não é um do tipo inteiro\033[m') #onde pego as cores: https://www.dio.me/articles/colocando-cores-no-seu-programa-em-python
    return valorInt
#Program principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

#teste
# def leiaInt(msg):
#     scan = str(input(msg)) #vai ser com um scanf em c
#     if scan.isnumeric():
#         n = int(scan)
#         return n
#     else:
#         return '\033[0;31mERRO! Não é um do tipo inteiro\033[m'

# #Program principal
# n = leiaInt('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')