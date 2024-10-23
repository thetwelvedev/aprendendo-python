from tkinter import *

janela = Tk()
janela.title("Frame")
janela.geometry("300x300")

frame_1 = Frame(janela, width=150, height=200, bg="red")
frame_1.grid(row=0, column=0)
label = Label(frame_1, width=20, text="1", fg="black")
label.grid(row=0, column=0) 

frame_2 = Frame(janela, width=150, height=200, bg="green")
frame_2.grid(row=0, column=1)
 
frame_3 = Frame(janela, width=300, height=200, bg="blue")
frame_3.grid(row=1, column=0, columnspan=2) # o columnspan defne o número de de coluna que o frame vai preencher

janela.mainloop()