"""Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais."""
nome = str(input())
salario_fixo = float(input())
total_de_vendas = float(input())
salario_final = salario_fixo + (0.15*total_de_vendas)
print(f"TOTAL = R$ {salario_final:.2f}")