from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("RadioButton")
janela.geometry("200x200")

def obter():
    print(f"O valor do botão selecionado é {selecionado.get()}.")

selecionado = BooleanVar()

rad1 = Radiobutton(janela, text="Primeiro", value=0, var=selecionado, command=obter)#Cada botão tem que ter um valor diferente, pois se tiver o mesmo valor quando um for ativado o outro de mesmo valor vai ser também
rad1.grid(row=0, column=0)
rad2 = Radiobutton(janela, text="Segundo", value=1, var=selecionado, command=obter)
rad2.grid(row=0, column=1)
rad3 = Radiobutton(janela, text="Terceiro", value=0, var=selecionado, command=obter)
rad3.grid(row=0, column=2)

janela.mainloop()