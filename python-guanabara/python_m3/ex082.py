#Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.
lista = []
listaPar = []
listaImpar =[]
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
    escolha = str(input('Deseja continuar[S/N]? ')).upper()
    if escolha == 'N':
        break
print(f'''A lista completa é: {lista}
A lista com números pares: {listaPar}
A lista com números impares: {listaImpar}''')