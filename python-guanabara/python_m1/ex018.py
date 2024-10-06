#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangentes desse ângulo.
from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo)) # Vai converter o valor para o seno só que tá em radiano, então converto valor angulo para rad
cosseno = cos(radians(angulo))# Vai converter o valor para o cosseno só que tá em radiano, então converto valor angulo para rad
tangente = tan(radians(angulo))# Vai converter o valor para o cosseno só que tá em radiano, então converto valor angulo para rad
print(f'A seno é {seno:.4f}, cosseno é {cosseno:.4f} e a tangente é {tangente:.4f} do ângulo de {angulo:.0f}°')