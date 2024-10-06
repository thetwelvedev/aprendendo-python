# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
#o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num, show=False):
    """
    >>Calcula o Fatorial de um número
    Parâmetro num: Número que será  cálculado
    Parâmetro show(opcional): MOstra o cálculo do Fatorial
    return: Retorna o resultado do Fatorial do número(num)
    """
    fat =  1
    for i in range(num, 0, -1): #For que vai decrescendo
        fat *= i
        if show == True: #Condição para mostrar a multiplicação
            if i > 1: #quando tem que aparecer o  x
                print(f'{i} x', end=' ')
            else: #  quando tem que aparecer o =
                print(f'{i} = ', end='')
    return fat
print(fatorial(6))
print(fatorial(5, True))
help(fatorial)