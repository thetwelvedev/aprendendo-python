"""Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais."""
numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora_trabalhada = float(input())

salario = horas_trabalhadas*valor_por_hora_trabalhada
print(f"NUMBER = {numero_funcionario}\nSALARY = U$ {salario:.2f}")