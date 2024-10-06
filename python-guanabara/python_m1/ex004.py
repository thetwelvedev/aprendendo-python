#Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
word = input("Digite algo: ")
print(f'O tipo primitivo desse valor é {type}')
print(f'Só tem espaços? {word.isspace()}')
print(f'Decimal: {word.isdecimal()}')
print(f'Alfabético: {word.isalpha()}')
print(f'alphanumérico: {word.isalnum()}')
print(f'Está em maiúscula? {word.isupper()}')
print(f'Está em minúscula? {word.islower()}')
print(f'Está capitalizada? {word.istitle()}')

