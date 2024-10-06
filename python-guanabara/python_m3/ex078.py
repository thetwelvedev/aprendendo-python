# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
num = []
for c in range(0, 5):
    num.append(int(input('Digite um número: ')))
print(f'''O menor valor foi {min(num)} e sua posição é {num.index(min(num))}
O maior valor foi {max(num)} e sua posição é {num.index(max(num))}''')#min pega menor valor da lista/max pega o maior valor da lista/index mostra posição do elemento na lista
#Versão na raça
num2 = []
menor =  maior = 0
for c in range(0, 5):
    num2.append(int(input('Digite um número: ')))
    #Código de menor e maior que
    if num2[c] < menor or menor == 0:
        menor = num2[c]
        posiçãoMenor = c # pois esse contador vai tá pecorrendo junto com os elementos da lista no caso cada valor de c é posição do elemento no loop
    if num2[c] > maior or maior == 0:
        maior = num2[c] 
        posiçãoMaior = c # pois esse contador vai tá pecorrendo junto com os elementos da lista
print(f'''O menor valor foi {menor} e sua posição é {posiçãoMenor}
O maior valor foi {maior} e sua posição é {posiçãoMaior}''')