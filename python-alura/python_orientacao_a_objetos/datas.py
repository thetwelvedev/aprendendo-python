#desafio opcional
'''Lançamos o seguinte desafio: para ajudar na formatação de datas você deve criar uma nova classe auxiliar.
Essa classe deve representar uma Data (sem hora) que sabe imprimir uma data formatada. Ela deve funcionar dessa forma:'''
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')