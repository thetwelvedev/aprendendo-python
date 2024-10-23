from tkinter import *

janela = Tk()
janela.title('Pack')
janela.geometry('500x500')

red =  Button(janela, text="Vermelho", bg="red", fg="white")
red.pack(side='left') #or red.pack(side=LEFT)
green =  Button(janela, text="Verde", bg="green", fg="white")
green.pack(side='top')
blue =  Button(janela, text="Azul", bg="blue", fg="white")
blue.pack(side='right')
orange =  Button(janela, text="Laranja", bg="orange", fg="white")
orange.pack(side='bottom')

janela.mainloop()

#Pack() - Esse gerenciador de geometria organiza os widgets em blocos antes de colocá-los no widget pai.