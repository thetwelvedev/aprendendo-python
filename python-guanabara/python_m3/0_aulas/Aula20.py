#Funções 1
#ex01
def linha():
    print('-'*30) 
#ex02
def mensagem(msg):
    print('-'*30) 
    print(msg)
    print('-'*30) 

mensagem(' CURSO EM VÍDEO')

#Prática
def soma(a, b):
    soma = a + b
    print(soma)

soma(3, 5)
linha()
#Empacotamento
def contador(*num):
    print(num)

contador(1,2,3,4)
contador(1,2)
contador(1,2,3,4,5,6)
linha()
#Outro exemplo
def contador2(*num):
    for valor in num:
        valor += 1
        print(f'{valor}', end= ' ')
    print()#Quebrar linha

contador2(1,2,3,4)
contador2(1,2)
contador2(1,2,3,4,5,6)
linha()

#Outro exemplo
def contador3(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador3(1,2,3,4)
contador3(1,2)
contador3(1,2,3,4,5,6)
linha()

valores =  [1, 2, 3, 5]

def dobrar(lista):
    listaDobrada = []
    for i in lista: # Vai pecorrer cada elemento na lista
        i *= 2 #Dobra o elemento
        listaDobrada.append(i) #Armazena o elemento na nova lista
    print(listaDobrada)

dobrar(valores)
linha()

def dobrar2(lista):
    pos = 0
    while pos < len(linha):
        lista[pos] *= 2
        pos += 1

dobrar(valores)

linha()
def somaFinal(*num):
    soma = 0
    for i in num:
        soma += i
    print(soma)

somaFinal(1,2,3)