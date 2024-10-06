from uteis import numeros
print('Módulo-numeros')
num = int(input('Digite um valor: '))
fatNum= numeros.fatorial(num)
print(f'O fatorial de {num} é {fatNum}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O dobro de {num} é {numeros.triplo(num)}')

from uteis import datas
print('Módulo-datas')
datas.dataDeHoje()
datas.data()

from uteis import strings
print('Módulo-string')

frase = str(input('Digite uma palavra: ')).strip()
strings.criptogarfiaDeCesar(frase)