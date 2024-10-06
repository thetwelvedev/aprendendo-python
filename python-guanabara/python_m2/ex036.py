#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valorCasa = float(input('Valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
ano = int(input('Em quantos anos pretende pagar? '))
prestacao = valorCasa / (ano * 12) # ano * 12 porque as prestações são mensais
print(f'Para pagar um casa de R${valorCasa:.2f} em {ano} ano(s) a prestação ficará R${prestacao:.2f}')
if prestacao > (salario * 0.30): # prestação maior que 30% do salário 
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')