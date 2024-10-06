#Crie um programa que leia o nome completo de uma pessoa e mostre:
'''Nome com todas letras maiúsculas, todas letras minúsculas, todas letras ao todo sem contar espaços, quantas letras tem o primeiro nome'''
nomeCompleto = str(input('Digite seu nome completo: '))
nomeMinusculo = nomeCompleto.lower() # Deixa todas as letras minúsculas
nomeMaiusculo = nomeCompleto.upper() # Deixa todas as letras maiúsculas
tamanhoTotal = len(nomeCompleto) # Tamanho de todos os elementos incluindo os espaços internos
totalDeEspacos = nomeCompleto.count(' ') # Quantos espaços internos tem
TamanhoDoNomeSemEspaco = tamanhoTotal - totalDeEspacos # Sabe só a quantidade de letras
NomeLista = nomeCompleto.split() #Separa a os nomes em lista 
TamanhoDoPrimeiroNome = len(NomeLista[0]) # tamanho do primeiro elemento da lista
print(f'''Nome minúsculo: {nomeMinusculo}
Nome maiúsculo: {nomeMaiusculo}
Total de letras: {TamanhoDoNomeSemEspaco}
O primeiro nome tem {TamanhoDoPrimeiroNome} letras ''')
