import moeda

n = int(input('Digite o preço: R$'))
taxa = int(input('Digite a porcentagem que deseja[apenas o valor]: '))

print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'A dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'Com o aumento de {taxa}% fica {moeda.moeda(moeda.aumentar(n, taxa))}')
print(f'Com a diminuição de {taxa}% fica {moeda.moeda(moeda.diminuir(n, taxa))}')