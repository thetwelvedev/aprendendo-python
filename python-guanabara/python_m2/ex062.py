# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerrará quando ele disser que quer mostrar 0 termos.
a1 = float(input('Digite o primeiro termo: '))
r = float(input('Qual a razão? '))
n = 1 #posição do número na sequência

total = 0
mais = 10 # Programa inicia com 10
while mais != 0: # quando digitar 0 acaba
    total += mais
    while n != total + 1:  #para ir até 10 inicialmente/ coloquei esse mais 1 para incluir o 10
        an = a1 + (n -1)*r # fórmula pa
        print(f'A termo {n}º da progressão é {an}')
        n += 1 # Vai aumentando 1 pois no próximo loop é a próxima posição
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Acabou!')