#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
'''– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''
valor = float(input('Digite o valor do produto: '))
pagamento = int(input('''Escolha sua opção de pagamento:
[1]À vista/cheque- 10% de desconto
[2]À vista no cartão: 5% de desconto
[3]Em até 2x no cartão: preço formal 
[4]3x ou mais no cartão: 20% de juros
Sua opção: '''))
if pagamento == 1:
    novoValor = valor - (valor * 0.1) # novo valor com 10% de desconto
    print(f'Seu pagamento fica R${novoValor:.2f}!')
elif pagamento == 2:
    novoValor = valor - (valor * 0.05) # novo valor com 5% de desconto
    print(f'Seu pagamento fica R${novoValor:.2f}!')
elif pagamento == 3:
    print(f'Seu pagamento fica 2x de R${valor / 2}!')
if pagamento == 4:
    parcelas = int(input('Qual a quantidade de parcelas[3 ou +]? '))
    novoValorComJuros = valor + (valor * 0.20) # novo valor com 20% de juros
    valorParcelado = novoValorComJuros / parcelas # valor parcelado
    print(f'Seu pagamento fica {parcelas}x de R${valorParcelado:.2f}!')