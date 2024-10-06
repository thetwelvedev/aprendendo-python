#Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
lista = []
i = count = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    i += 1 # vai servir para pecorrer a lista
    # A) Quantos números foram digitados.
    count += 1
    # B) A lista de valores, ordenada de forma decrescente.
    lista.sort(reverse= True) #Deixa na ordem decrescente
    # C) Se o valor 5 foi digitado e está ou não na lista.
    if 5 in lista:
        resultado = 'Faz parte da lista'
    else:
        resultado  = 'Não faz parte da lista'
    escolha = str(input('Deseja continuar[S/N]? ')).upper()
    if escolha == 'N':
        break
print(f'''Quantidade de número digitado: {count}
Lista de decrescente: {lista}
O número 5: {resultado}''')