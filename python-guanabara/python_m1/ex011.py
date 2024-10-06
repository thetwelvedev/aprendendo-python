#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
a = float(input('Qual a largura? '))
h = float(input('Qual a altura? '))
area = a * h
litroTinta = area / 2
print(f'A área da parede é {area:.2f}m² e precisa de {litroTinta:.2f} litros')