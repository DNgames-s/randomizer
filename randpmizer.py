from tkinter import *
from tkinter import ttk
from random import *

a = 0


def random():
    global a
    a = randint(0, 100)
    label.config(text=a)
    return a 





root = Tk()
root.title('Рандомайзер')
root.geometry('280x120')
root.resizable(width=False, height=False)

label2 = ttk.Label(root, font='Arial 10', text='нажмите, чтобы сгенерировать(0-100)')
label2.pack()


label = ttk.Label(root, font='Arial 10', text=a)
label.pack(pady=10)

btt = ttk.Button(root, text='сгенерировать', command=random)
btt.pack(pady=16)






root.mainloop()
