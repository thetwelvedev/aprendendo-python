from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Listbox")
janela.geometry("250x200")

listbox = Listbox(janela, height=8)
listbox.grid(row=0, column=0)

def test():
    print(listbox.get(ACTIVE))
    l = Label(janela, text=listbox.get(ACTIVE), width=20)
    l.grid(row=0, column=1)

def test2():
    listbox.delete(ANCHOR)

linguagens_programacao = ["Python", "Java", "C", "C++", "JavaScript", "Ruby", "Go", "Swift"]

for i in linguagens_programacao:
    listbox.insert(END, i)

b = Button(janela, text="Imprimir", command=test)
b.grid(row=1, column=0)
b2 = Button(janela, text="Deletar", command=test2)
b2.grid(row=2, column=0)


"""# Excluir elemento selecionado
listbox.delete(ANCHOR)
#Exclua o segundo item da posição delete (2)
listbox.delete(2)
#Excluir todos os itens 
listbox.delete(0, END)
#exclui linhas no intervalo especificado
listbox.delete(inicio, fim)
"""
janela.mainloop()