#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salary = float(input('Digite o seu salário: '))
newSalary = salary + (salary * 0.15) # 0.05 é 5/100 ou 5%
print(f'O salário era R${salary:.2f} e com aumento ficou R${newSalary:.2f}')