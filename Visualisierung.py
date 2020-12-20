# f5df1b orange
# 545451 grau

from tkinter import *

root = Tk()
root.geometry("800x480")


def toggle(tog=[0]):

    tog[0] = not tog[0]
    if tog[0]:

    else:



def toggle2(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:

    else:


btn = Button(root, text="Hallo", command=toggle, bg="#545451")
btn2 = Button(root, text="Holla", command=toggle2, bg="#545451")
btn2.pack()
btn.pack()

root.mainloop()
