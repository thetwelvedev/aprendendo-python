#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
cont = 0
soma = 0
maior = menor = 0
escolha = 'S'
while escolha == 'S':
    n = int(input('Digite um número inteiro: '))
    cont += 1 # Contador
    soma += n 
    #Maior e menor
    if n > maior:
        maior = n
    if menor > n or menor == 0: #Tirar o valor 0 do menor
        menor = n
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / cont
print(f'Foram digitados {cont} números e sua média deu {media}.')
print(f'O menor número foi {menor} e o maior foi {maior}.')