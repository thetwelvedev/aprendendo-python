from tkinter import *

janela = Tk()
janela.title('Place')
janela.geometry('500x500')

btn =  Button(janela, text="Usando place")
btn.place(x=100,y=100)

janela.mainloop()

#Place() - Esse gerenciador de geometria organiza os widgets colocandos em uma posição específica no widget pai.