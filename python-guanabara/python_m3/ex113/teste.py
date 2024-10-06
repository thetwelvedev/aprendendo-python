from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado

n = dado.leiaDinheiro('Digite o preço: R$') #Essa função vai substituir o int(input() pois ela vai ter umas particularidades
taxa = float(input('Digite a porcentagem que deseja[apenas o valor]: '))
moeda.resumo(n,taxa)