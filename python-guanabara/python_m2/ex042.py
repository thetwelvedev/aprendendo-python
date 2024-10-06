#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
'''– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''
a = float(input('Digite o comprimento da reta: '))
b = float(input('Digite o comprimento da outra reta: '))
c = float(input('Digite o comprimento da outra reta: '))
# Para ser triângulo tem que todos os lados serem  menores que a soma dos outros dois lados.
if a >= b + c:
    print('Não é triângulo!')
if b >= a + c:
    print('Não é triângulo!')
if c >= a + b:
    print('Não é triângulo!')
else:
    print('É um triângulo ', end='') # end='' serve para juntar com a próxima linha
    if a == b == c:
        print('equilátero!')
    elif a == b or a == c or b == c:
        print('isósceles!')
    else:
        print('escaleno!')

    
    
    
     
    