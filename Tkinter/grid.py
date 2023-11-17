from tkinter import *
root = Tk()
meu_texto = Label(root,text="jujubinha")
meu_texto2 = Label(root,text="jujubinha2")
#o grid faz que possamos escolher o lugar inde aparece a mensagem
meu_texto.grid(row=0, column=0)
meu_texto2.grid(row=1, column=0)
root.mainloop()