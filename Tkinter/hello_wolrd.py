#importa todas as funções
from tkinter import *

#cria a janela
root = Tk()

#coloca um texto dentro da janela
meu_texto = Label(root,text="Hello world!")

#coloca a frase na janela
meu_texto.pack()

#crio um loop para que a janela fique aberta
root.mainloop()