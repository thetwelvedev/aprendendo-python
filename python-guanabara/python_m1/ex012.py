#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
price = float(input('Digite o preço do produto: '))
discountPrice = price - (price * 0.05) # 0.05 é 5/100 ou 5%
print(f'O valor era R${price:.2f} e com desconto ficou R${discountPrice:.2f}')