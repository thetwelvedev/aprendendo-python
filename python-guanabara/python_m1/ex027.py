#Faça um programa qua leia o nome completo da uma passoa. mostrando em seguida o primeiro e o último nome separadamenta.
'''Ex: Ana Maria de Souza
primeiro = Ana
último = Souza'''
nome = str(input('Digite seu nome completo: '))
listaNome = nome.split() # Faz uma lista com cada elemento
primeiroNome = listaNome[0] # Vai pegar o primeiro elemento da lista
ultimoNome = listaNome[-1] # Vai pegar o último elemento da lista
print(f'''Seu primeiro nome é {primeiroNome}
Seu último nome é {ultimoNome}''')