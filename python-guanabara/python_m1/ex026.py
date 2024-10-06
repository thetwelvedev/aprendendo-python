##Faça um programa que leia uma frase pelo teclado e mostre:
''' -Quantas vezes aparece a letra “a”
-Em que posição aparece a primeira vez.
-Em que posição ela aparece a última vez.'''
frase = str(input('Digite uma frase: ')).strip().lower()
contadorDea = frase.count('a')
encontrarPrimeiroA = frase.find('a') + 1 # A posição começa do 0
encontrarUltimoA = frase.rfind('a') + 1 # .rfind() começa a procurar pelo lado direito
print(f'''A letra A aparece: {contadorDea} vezes
A letra A apareceu na primeira vez na posição {encontrarPrimeiroA}
A letra A aparceu na ultima vez na posição {encontrarUltimoA}''')