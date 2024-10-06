import moeda 

n = int(input('Digite o preço: R$'))
taxa = int(input('Digite a porcentagem que deseja[apenas o valor]: '))

print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n,formato=True)}')
print(f'A dobro de {moeda.moeda(n)} é {moeda.dobro(n,formato=True)}')
print(f'Com o aumento de {taxa}% fica {moeda.aumentar(n, taxa,formato=True)}')
print(f'Com a diminuição de {taxa}% fica {moeda.diminuir(n, taxa,formato=True)}')