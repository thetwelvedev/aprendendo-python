# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def linha():
    print('-='*15)

def maior(*num):
    from time import sleep
    #Nesse empacotamento ele cria uma tupla, então vou converter para lista
    lista = list(num)
    if num == []: #Quando não colocarem parâmetro
        lista = []
    linha()
    print('Analisando os valores passados...')
    if lista != []:
        #Esse for vai pecorrer a lista para printar cada elemento dela
        for i in range(0, len(lista)):
            print(f'{lista[i]}', end=' ', flush=True)#flush para funcionar o sleep corretamente
            sleep(0.5)
        print(f'Foram informados {len(lista)} valores ao todo.')
        #Usar a função sorted para deixar em ordem crescente
        lista.sort()
        print(f'O maior número dessa sequência é {lista[-1]}.') #vai pegar o último elemento
    else: #Caso sem parâmetro
        print('Foram informados 0 valores ao todo.')
        print('O maior número dessa sequência é 0.')
maior(1,7,8,4,5)
maior()