#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
frase = str(input('Digite uma frase: ')).upper()
fraseSemEspaço = frase.replace(' ', '')# Vai criar a frase em espaços
tamanho = len(fraseSemEspaço) #Ver o tamanho da frase
fraseInvertida = ''
#fraseInversa = fraseSemEspaço[::-1] #Vem mostrando o elementos na ordem decrescente//inverte de forma simples

#Invertendo com o for
for c in range(tamanho - 1 , -1, -1): #Faz um for decrescente pois começa do último elemento(tamanho - 1 pois o len começa de 1 mas as posições de cada letra começa do 0) até o primeiro(-1 pois ele para um antes que seria o zero)
    char = fraseSemEspaço[c] # Pega cada elemento ao contrário
    fraseInvertida += char # Em cada loop a letra que vem de trás para frente vai somando ao final da palavra originalmente estava vazia(pois soma de string só junta ex.: 'a' + 'a' = 'aa')
print(F'O inverso de {fraseSemEspaço} é {fraseInvertida}')
if fraseSemEspaço == fraseInvertida: # Se a palavra normal for igual palavra ao contrário é palíndromo
    print('É palíndromo!')
else:
    print('Não é palíndromo!')
