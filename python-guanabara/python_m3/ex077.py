#Crie um programa que tenha uma tupla com várias palavras(não usar acentos)
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais
palavras_programacao = ('variavel', 'funcao', 'classe', 'metodo', 'condicional', 'loop', 'lista', 'dicionario', 'string', 'inteiro', 'flutuante', 'booleano', 'import', 'return', 'while', 'for', 'if', 'else', 'elif', 'def', 'True', 'False', 'None', 'lambda', 'global', 'local', 'try', 'except', 'finally', 'raise', 'assert', 'break', 'continue')
for palavra in palavras_programacao: # Cada palavra aqui vai ser um elemento da tupla
    print(f'\nNa palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
