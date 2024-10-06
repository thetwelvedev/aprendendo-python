#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(num):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - num
    if idade < 16:
        return f'Com {idade} anos: Voto NEGADO!'
    elif  16 <= idade < 18:
        return f'Com {idade} anos: Voto OPCIONAL!'
    else:
        return f'Com {idade} anos: Voto OBRIGATÓRIO!'

n = int(input('Ano de nascimento: '))
print(voto(n))