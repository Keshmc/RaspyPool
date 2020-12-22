# Pythons IDPA Projekt Raspy Pool Main Cycle
from tkinter import *

root = Tk()
root.geometry("800x480")

mode = StringVar()



def Hand():
    mode.set("hand")
    while "hand" in mode.get():
        print("Juhhhuuuu")
    pass

def Test():
    print("hi")


btn = Button(root, text="Test", command=Hand).pack()




root.mainloop()
