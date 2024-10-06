#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
'''– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''
def linha():
    print('-='*40)

def notas(*num, situação=False):
    #Dicionário
    notas = dict()
    #Transformando em lista
    num = list(num)
    #Pecorrer a lista para informar a quantidade de notas e fazer a soma das notas
    contador = somaDasNotas = 0
    for elemento in num:
        somaDasNotas += elemento
        contador += 1
    notas['Total'] = contador
    #Encontrar o maior e o menor
    notas['Maior'] = notas['Menor'] = 0
    for i in range(0,len(num)):
        if notas['Maior'] == 0 and notas['Menor'] == 0:
            notas['Menor'] = num[i]
            notas['Maior'] = num[i]
        if notas['Maior'] < num[i]:
            notas['Maior'] = num[i]
        if notas['Menor'] > num[i]:
            notas['Menor'] = num[i]
    #Média das notas
    media = somaDasNotas/ contador
    notas['Média'] = media
    #Caso opcional
    if situação == True:
        if media < 7:
            notas['Situação'] = 'Ruim'
        elif 7 <= media <= 8:
            notas['Situação'] = 'Boa'
        else:
            notas['Situação'] = 'Excelente'
    return notas
linha()
print(notas(1,2,3,4,5))
print(notas(9.9,9.5,10,9,8, situação=True))

#Solução guanabas
def notas2(*num, situação=False):
    notas = dict()
    notas['Total'] = len(num)
    notas['Maior'] = max(num)
    notas['Menor'] = min(num)
    notas['Média'] = sum(num)/len(num)
    #Caso opcional
    if situação: # Aqui situção pode receber o valor booleando true, quando acontece if True, roda o código dentro do if
        if notas['Média'] < 7:
            notas['Situação'] = 'Ruim'
        elif 7 <= notas['Média'] <= 8:
            notas['Situação'] = 'Boa'
        else:
            notas['Situação'] = 'Excelente'
    return notas
linha()
print(notas2(1,2,3,4,5))
print(notas2(9.9,9.5,10,9,8, situação=True))