#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
#Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
n = int(input('Quantos termos de fibonacci você quer mostrar? '))
n1 = 0 # antecessor f(n-1)
n2 = 1 # antecessor do antecessor f(n-2)
count = 0
while count != n + 1:# quando o contador tiver chegado na posição que foi pedida no n para/ n + 1 pois quando tiver na posição 5 por exemplo e n = 5, ele tem que mostrar a posição 5, caso contrário ele ia para e não ai mostrar a posição 5
    if count == 1:
        print(f'{n1} ', end ='') # primeiro termo é 0
    if count >= 2:
        fn = n1 + n2 # fórmula de fibonacci
        print(f'-> {fn} ', end='')
        # Assumindo as novas posições
        n2 = n1
        n1 = fn
    count += 1
print(' -> Acabou!')