from tkinter import *

janela = Tk()
janela.title("Label")
janela.geometry('200x200')

label = Label(janela, text="Primeiro label", font=("Arial Bold", 20), bg="green", fg="white") #adiciona o rótulo
label.grid(column=0, row=0) #fornece a localização ao rótulo

janela.mainloop()