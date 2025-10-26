"""Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias."""
dinheiro = int(input())
cedulas = [100, 50, 20, 10, 5, 2, 1]
print(dinheiro)
for cedula in cedulas:
    qtd_cedulas = dinheiro//cedula  #vai pegar só parte inteira
    print(f"{qtd_cedulas} nota(s) de R$ {cedula},00")
    dinheiro = dinheiro % cedula #vai pegar o resto da divisão para o próximo loop