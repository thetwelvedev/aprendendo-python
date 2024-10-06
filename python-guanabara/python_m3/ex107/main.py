#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

n = int(input('Digite o preço: R$'))
taxa = int(input('Digite a porcentagem que deseja[apenas o valor]: '))

print(f'A metade de R${n:.2f} é R${moeda.metade(n):.2f}')
print(f'A dobro de R${n:.2f} é R${moeda.dobro(n):.2f}')
print(f'Com o aumento de {taxa}% fica R${moeda.aumentar(n, taxa):.2f}')
print(f'Com a diminuição de {taxa}% fica R${moeda.diminuir(n, taxa):.2f}')