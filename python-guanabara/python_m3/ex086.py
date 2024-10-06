#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
matriz = []
#Colocando os valores na matriz
for i in range(0, 3): #vai fazer ter 3 linhas
    linha = []
    for j in range(0, 3): # vai fazer ter 3 valores para cada linha(no caso 3 colunas)
        valor = int(input(f'Digite o valor de [{i},{j}]: '))
        linha.append(valor) #cada posição vai pegar um valor
    matriz.append(linha) #Cada loop do for principal eu pego uma linha

#Printando os valores
for i in range(0, 3):
    for j in range(0, 3): 
        print(f'[{matriz[i][j]:^5}]', end='') #Como os 3 valores printado por loop são da mesma linha uso o end='' para juntar
    print() #Quebra linha a cada loop do primeiro for, e o segundo for coloca 3 valores a cada loop do primeiro for