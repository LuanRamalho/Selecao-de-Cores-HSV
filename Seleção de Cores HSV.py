from tkinter import*
from tkinter.colorchooser import*
import tkinter.messagebox
window = Tk()
window.title("Seleção de Cores")
window.geometry("300x50")
window.config(background='#c0c0c0')

def escolha_cor():
    color = askcolor()
    window.configure(bg=color[1])
    print(color)

Button(text='Selecione a cor.', command=escolha_cor).pack()
mainloop()
