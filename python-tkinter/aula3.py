from tkinter import *

janela = Tk()
janela.title("Botão")
janela.geometry('200x200')

label = Label(janela, text="Primeiro botão")
label.grid(column=0, row=0)

def mensagem():
    print("Você apertou o botão!") #vai aparecer no terminal/ não necessário para janela
    label.configure(text="Você apertou o botão!") #Vai alterar a propriedade label nesse caso

btn = Button(janela, text="Clique aqui", bg="green", fg="white", width="9", height="2", command=mensagem) #Adiciona um botão
#text="mensagem no  botão", bg="cor do fundo", fg="cor da fonte", width="largura", height="altura", command=mensagem)
btn.grid(column=1, row=0) #Posiciona o botão

janela.mainloop()