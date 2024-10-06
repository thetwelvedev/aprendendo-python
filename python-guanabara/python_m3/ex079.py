#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.  
#Caso o número já exista lá dentro, ele não será adicionado.No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
count = 0
while True:
    num = int(input('Digite um número: '))
    #Para adicionar o elemento a primeira vez que aparecer
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    #Caso não exista o valor só vai informar a que já existe 
    else:
        print('Esse número está duplicado e não vou adicionar!')
    escolha = str(input('Deseja continuar[S/N]? ')).upper()
    if escolha == 'N':
        lista.sort() #Deixa na ordem crescente
        print(lista)
        break
    
