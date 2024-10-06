#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
lista = []
countEsquerda = countDireita = 0
frase = str(input('Digite uma expressão: ')) 
for letra in frase: #Aqui ele vai pegar cada elemento no string frase
    lista.append(letra) #Vai colocar cada elemento char e colocar n alista
for i in range(0, len(lista)): #Vai verificar se tem '(' ou ')' na lista
    if lista[i] == '(':
        countEsquerda += 1 #Quantas vezes aparece '('
    if lista[i] == ')':
        countDireita += 1 #Quantas vezes aparece ')'
if countDireita == countEsquerda:
    print('Sua expressão está certa!')
else:
    print('Sua expressão está errada!')