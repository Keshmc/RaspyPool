# imports
from tkinter import *

# Parameter für Buttons
# Vorlage Button(root, text="", command=, width=width, height=height, justify=justify, padx=padx, pady=pady, font=font, bg=str(Color))
BgColor = "#bfbeba"
Color = "#6e6d68"
ColorActive = "#ffd814"
font = "Arial"
height = 1
width = 10
justify = CENTER
padx = 5
pady = 5

# Grundbild
root = Tk()
root.title("Raspy Pool")
root.geometry("800x480")
root.configure(bg=str(BgColor))

# Tastenfeld rechts
FeldRechts = LabelFrame(width=105, height=400, bg=str(BgColor))
FeldRechts.grid(row=0, column=5, sticky=E)
FeldRechts.grid_propagate(0)

# Tastenfeld unten
FeldUnten = LabelFrame(width=800, height=80, bg=str(BgColor))
FeldUnten.grid(row=5, column=0)

# Commands
def Auto():
    pass


def Hand():
    pass


def Service():
    pass


def Start():
    pass


def Stopp():
    pass


# Tastenleiste rechts
# Definiere Buttons
BtnAuto = Button(FeldRechts, text="Auto", command=Auto, width=width, height=height, justify=justify, font=font,
                 bg=str(Color))

BtnHand = Button(FeldRechts, text="Hand", command=Hand, width=width, height=height, justify=justify, font=font,
                 bg=str(Color))

BtnService = Button(FeldRechts, text="Service", command=Service, width=width, height=height, justify=justify, font=font,
                    bg=str(Color))

BtnStart = Button(FeldRechts, text="Start", command=Start, width=width, height=height, justify=justify, font=font,
                  bg=str(Color))

BtnStopp = Button(FeldRechts, text="Stopp", command=Stopp, width=width, height=height, justify=justify, font=font,
                  bg=str(Color))

# Ordne Buttons ins Tastenfeld rechts
BtnAuto.grid(row=0, column=0, pady=5)
BtnHand.grid(row=1, column=0, pady=5)
BtnService.grid(row=2, column=0, pady=5)
BtnStart.grid(row=3, column=0, pady=5)
BtnStopp.grid(row=4, column=0, pady=5)


# Mainloop
root.mainloop()
