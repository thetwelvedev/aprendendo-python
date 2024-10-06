#Crie um programa que leia o nome de uma pessoa e diga se ela tem “Silva” no nome
nome = str(input('Digite seu nome completo: ')).strip() # Deixa tudo minúsculo para facilitar a comparação e sem espaço aos lados
comparacao = 'Silva' in nome
print(f"Tem Silva no nome? {comparacao} ")