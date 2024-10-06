#Escreva um programa que leia um  valor em metros e a exiba convertido em centímetros e milímetros.
m = float(input('Digite a dimensão em metros: '))
cm = m * 100
mm = m * 1000

print(f'{m}m é {cm}cm ou {mm}mm')
