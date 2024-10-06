#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar.(US$1.00 = R$4,91)
real = float(input('Você tem quanto dinheiro na carteira? '))
dolar = real / 4.91
print(f'Você tem R${real:.2f} e em doláres é US${dolar:.2f}')