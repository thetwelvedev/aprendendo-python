#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.
lista = []
for i in range (0, 5):
    num = int(input('Digite um número: '))
    if i == 0 or num > lista[-1]:#Vai adicionar o primeiro elemento na lista
        lista.append(num) #Vai colocar o maior número no final
    else:
        pos = 0
        while pos < len(lista):# Vai pecorrer a lista
            if num <= lista[pos]: # Vai verificar se o número é menor que outro número numa posição específica
                lista.insert(pos, num) #Vai inserir o número na posição do antigo e o antigo é empurado para frente
                break
            pos += 1 #Para fazer a comparação com todas as posições da lista
print(lista)