#Módulos e Pacotes

#Módulos
'''Modularização é o ato de criar módulos no código
-Como criando módulos para diminuir o código, como por exemplo um código para ter as funções e outro para rodarr elas

Esse aqui ficaria um arquivo python exemplo:
uteis.py
def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

import uteis
num = int(input('Digite um valor: '))
fatNum= uteis.fatorial(num)
print(f'O fatorial de {num} é {fatNum}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O dobro de {num} é {uteis.triplo(num)}')

-Vantagens
Organização de código
Facilidade na manutenção
Ocultação de código detalhado
Reutilização em outros projetos
'''
#Pacotes
'''Pacotes em outras linguagens chamam de biblioteca
Básimente é ter dentro de pacotes vários módulos para importação
Normalmente usado em projetos bem grandes

Nessa pasta tem o
pacote: uteis
módulos: datas, numeros, strings
'''