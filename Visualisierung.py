# imports
from tkinter import *

# Parameter für Buttons
BgColor = "#fffefa"
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

# Projekt Titel
Titel = Label(root, text="RaspyPool; IDPA Projekt 2020", relief=RAISED)
Titel.grid(row=0, column=0, columnspan=6, sticky=W + E)

# Tastenfeld rechts
FeldRechts = LabelFrame(width=105, height=400, bg=str(BgColor))
FeldRechts.grid(row=1, column=5, sticky=E)
FeldRechts.grid_propagate(0)

# Tastenfeld unten
FeldUnten = LabelFrame(width=800, height=80, bg=str(BgColor))
FeldUnten.grid(row=5, column=0, columnspan=6, sticky=W + E)
FeldUnten.grid_propagate(0)

# Variabeln
Mode = StringVar(root)


# Commands
# Tastenfeld rechts
def Auto():
    if BtnAuto.config("bg")[-1] == str(Color):
        BtnAuto.config(bg=str(ColorActive))

        BtnService.config(bg=str(Color))
        BtnHand.config(bg=str(Color))

    else:
        BtnAuto.config(bg=str(Color))


def Hand():
    if BtnHand.config("bg")[-1] == str(Color):
        BtnHand.config(bg=str(ColorActive))

        BtnAuto.config(bg=str(Color))
        BtnService.config(bg=str(Color))

    else:
        BtnHand.config(bg=str(Color))


def Service():
    if BtnService.config("bg")[-1] == str(Color):
        BtnService.config(bg=str(ColorActive))

        BtnAuto.config(bg=str(Color))
        BtnHand.config(bg=str(Color))

    else:
        BtnService.config(bg=str(Color))
    pass


def Start():
    pass


def Stopp():
    pass


# Tastenfeld unten
def Home():
    PicHome = LabelFrame(bg=str(BgColor), width=(800 - 105), height=400)
    PicHome.grid(row=1, column=0, rowspan=4, columnspan=4)
    PicHome.grid_propagate(0)


def Pump():
    PicPump = LabelFrame(bg=str("#84ab8d"), width=(800 - 105), height=400)
    PicPump.grid(row=1, column=0, rowspan=4, columnspan=4)
    PicPump.grid_propagate(0)


def Filter():
    PicFilter = LabelFrame(bg=str("#cb34d9"), width=(800 - 105), height=400)
    PicFilter.grid(row=1, column=0, rowspan=4, columnspan=4)
    PicFilter.grid_propagate(0)


def Heat():
    PicHeat = LabelFrame(bg=str("#d95d34"), width=(800 - 105), height=400)
    PicHeat.grid(row=1, column=0, rowspan=4, columnspan=4)
    PicHeat.grid_propagate(0)


def Parameter():
    # Bild Parameter
    PicParameter = LabelFrame(bg=str("#427bf5"), width=(800 - 105), height=400)
    PicParameter.grid(row=1, column=0, rowspan=4, columnspan=4)
    PicParameter.grid_propagate(0)


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
                  bg=Color)

# Ordne Buttons ins Tastenfeld rechts
BtnAuto.grid(row=0, column=0, pady=5)
BtnHand.grid(row=1, column=0, pady=5)
BtnService.grid(row=2, column=0, pady=5)
BtnStart.grid(row=3, column=0, pady=5)
BtnStopp.grid(row=4, column=0, pady=5)

# Tastenfeld unten
BtnHome = Button(FeldUnten, text="Home", command=Home, width=width, height=height, justify=justify, font=font,
                 bg=str(Color))
BtnPump = Button(FeldUnten, text="Pumpe", command=Pump, width=width, height=height, justify=justify, font=font,
                 bg=str(Color))

BtnFilter = Button(FeldUnten, text="Filter", command=Filter, width=width, height=height, justify=justify, font=font,
                   bg=str(Color))

BtnHeat = Button(FeldUnten, text="Heizung", command=Heat, width=width, height=height, justify=justify, font=font,
                 bg=str(Color))

BtnParameters = Button(FeldUnten, text="Parameter", command=Parameter, width=width, height=height, justify=justify,
                       font=str(font),
                       bg=str(Color))

# Ordne Buttons ins Tastenfeld unten
BtnHome.grid(row=0, column=0, padx=10, pady=10)
BtnPump.grid(row=0, column=1, padx=10, pady=10)
BtnFilter.grid(row=0, column=2, padx=10, pady=10)
BtnHeat.grid(row=0, column=3, padx=10, pady=10)
BtnParameters.grid(row=0, column=4, padx=10, pady=10)

# Mainloop
root.mainloop()
