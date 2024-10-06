from datetime import date
def dataDeHoje():
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
    print(f'{dia}/{mes}/{ano}')

def data():
    data = date.today()
    print(data)