from tkinter import *
root = Tk()
#Entry é como um input
e = Entry(root, width=50, bg="#65d9db", fg="black", borderwidth=5)
e.pack()
def myClick():
    texto = e.get()
    mylabel = Label(root, text="seu texto: " + texto)
    mylabel.pack()
botao = Button(root,text="me clica", fg="#65d9db", bg="black", command=myClick)
botao.pack()

root.mainloop()