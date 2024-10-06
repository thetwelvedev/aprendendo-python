#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos km o carro percorreu:  '))
dia = int(input('Quantos dias que o carro ficou alugado: '))
pagar = km * 60 + dia * 0.15
print(f'Você rodou {km}km e {dia} dia(s) e o total a se pagar deu R${pagar:.2f}')
