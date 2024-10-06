#Aprimore o desafio anterior, mostrando no final:  
#No final, mostre a matriz na tela, com a formatação correta.
matriz = []
#Colocando os valores na matriz
for i in range(0, 3): #vai fazer ter 3 linhas
    linha = []
    for j in range(0, 3): # vai fazer ter 3 valores para cada linha(no caso 3 colunas)
        valor = int(input(f'Digite o valor de [{i},{j}]: '))
        linha.append(valor) #cada posição vai pegar um valor
    matriz.append(linha) #Cada loop do for principal eu pego uma linha
print('-='*20)
#Printando os valores
soma = somaTerceiraColuna = maior = 0
for i in range(0, 3):
    #B) A soma dos valores da terceira coluna./Pois só a linha varia e a coluna é fixa então coloquei no loop só da linha, e como esse é o for só de printar valores, os valores já estão armazenados nas suas posições, logo não tem problema não tá no escopo do for da coluna
    somaTerceiraColuna += matriz[i][2]
    for j in range(0, 3): 
        print(f'[{matriz[i][j]:^5}]', end='') #Como os 3 valores printado por loop são da mesma linha uso o end='' para juntar
        #A) A soma de todos os valores pares digitados.
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
        #C) O maior valor da segunda linha.
        if matriz[1][j] > maior or maior == 0:
            maior = matriz[1][j]
    print() #Quebra linha a cada loop do primeiro for, e o segundo for coloca 3 valores a cada loop do primeiro for                                                 
print('-='*20)
print(f'A soma dos valores pares da matriz deu: {soma}.')
print(f'A soma dos valores da terceira coluna deu: {somaTerceiraColuna}.')
print(f'O maior valor da segunda linha é {maior}.')