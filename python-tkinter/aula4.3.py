from tkinter import *

janela = Tk()
janela.title('Grid')
janela.geometry('500x500')

red =  Button(janela, text="Vermelho", bg="red", fg="white")
red.grid(row=0,column=0)
green =  Button(janela, text="Verde", bg="green", fg="white")
green.grid(row=1,column=1)
blue =  Button(janela, text="Azul", bg="blue", fg="white")
blue.grid(row=2,column=2)
orange =  Button(janela, text="Laranja", bg="orange", fg="white")
orange.grid(row=3,column=3)

janela.mainloop()

#Grid() - Esse gerenciador de geometria organiza widgets em uma estrutura semelhante a uma tabela no widget pai.