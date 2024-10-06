#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.
from math import pow, sqrt #pow é de potência e sqrt é raiz quadrada
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hipotenusa = pow(co,2) + pow(ca,2) #pega o quadrado dos catetos
h = sqrt(hipotenusa) #como a hipotenusa estaria ao quadrado então passa como raiz, logo tiro a raiz quadrada do quadrado dos catetos
print(f'Os catetos {co} e {ca} tem a hipotenusa {h}.')
