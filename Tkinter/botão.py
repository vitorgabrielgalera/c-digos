from tkinter import *
root = Tk()
#define o que fazer ao clicar no botão
def myClick():
    mylabel = Label(root, text="clique no botão!")
    mylabel.pack()
botao = Button(root,text="me clica", fg="#65d9db", bg="#000000", command=myClick)
botao.pack()
root.mainloop()