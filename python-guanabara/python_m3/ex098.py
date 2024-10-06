#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:   
def linha():
    print('-='*15)

def contador(inicio, fim, passo):
    from time import sleep
    linha()
    #Teste lógico
    if passo == 0:
        passo = 1 
    if passo < 0:
        passo *= -1
    
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)

    if inicio < fim :
        for i in range(inicio, fim + 1, passo):
            print(f'{i}', end=' ', flush=True) # Uso o flush para não ativar o buffer de tela
            sleep(0.5)
        print('FIM!')
    if inicio > fim :
        for i in range(inicio, fim - 1, -passo): # tem que ser com o passo negativo para o for rodar do maior para o menor
            print(f'{i}', end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
#A)de 1 até 10, de 1 em 1 
contador(1, 10, 1)
#B)de 10 até 0, de 2 em 2
contador(10, 0, 2)

linha()
print('Contagem Personalizada')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
linha()