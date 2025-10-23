#Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
a, b, c = map(float, input("").split())
maiorAB = (a + b + abs(a - b)) // 2
maior = (maiorAB + c + abs(maiorAB - c)) // 2
print(f"{maior:.0f} eh o maior")