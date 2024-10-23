from tkinter import *
from tkinter.ttk import * #Precisa disso para o combobox funcionar

janela = Tk()
janela.title("Combobox")
janela.geometry("500x500")

combo = Combobox(janela)
combo["values"] = (1, 2, 3, 4, "Par") #Valores a serem selecionados na combobox
combo.current(0) #O parâmetro é o index da lista feita com os valores
combo.grid(row=0, column=0)

def obter(eventObject): #Esse parametro da função vai ser valor selecionado dentro da combobox
    v = combo.get() #Vai sempre puxar o valor do .current
    label = Label(janela, text=v)
    label.grid(row=1, column=0)

combo.bind("<<ComboboxSelected>>", obter) #vai ler o evento e passar para a função, onde lá vai ter o parametro para receber o evento

janela.mainloop()
""".bind() é usado para associar eventos de interação do usuário (como cliques, teclas pressionadas, movimentos do mouse, etc.)
 a funções ou métodos específicos, permitindo que você reaja a essas ações.
widget.bind(evento, função)"""