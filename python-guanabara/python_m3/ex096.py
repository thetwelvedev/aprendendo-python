# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno de {largura}m x{comprimento}m é {area:.2f}m²')

print('>>>>>> ÁREA DO TERRENO <<<<<<')
a = float(input('Largura[m]: '))
b = float(input('Comprimento[m]: '))

area(a,b)