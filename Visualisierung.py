# imports
from tkinter import *

# Parameter für Buttons
BgColor = "#fffefa"
Color = "#6e6d68"
ColorActive = "#ffd814"
ColorStart = "#2cf23f"
ColorStopp = "#eb3528"
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
StatFilter = IntVar(root)
StatPump = IntVar(root)
StatHeat = IntVar(root)
Mode = StringVar(root).set("platzhalter")


def blink():
    root.after(500, BtnStart.configure(bg=str(ColorStart)))
    root.update()
    root.after(500, BtnStart.configure(bg=str(Color)))
    root.update()
    root.after(500, blink)


def start():
    global hmStart
    if BtnStart.config("bg")[-1] == str(Color):
        hmStart = True
    else:
        BtnStart.config(bg=str(Color))
        hmStart = False


def stopp():
    global hmStopp
    if BtnStopp.config("bg")[-1] == str(Color):
        hmStopp = True
    else:
        BtnStart.config(bg=str(Color))
        hmStopp = False


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

"==========================================================================================================="
"Parameterfeld"
# Label für PicParameter
PicParameter = LabelFrame(bg=str("#427bf5"), width=(800 - 105), height=400)
PicParameter.grid_propagate(0)


def Parameter():
    global PicParameter
    # Bild Parameter
    PicParameter.grid(row=1, column=0, rowspan=4, columnspan=4)


# Labels Eingabefelder
TxtIst = Label(PicParameter, text="Istwert", width=30)
TxtSoll = Label(PicParameter, text="Sollwert", width=30)
TxtInterval = Label(PicParameter, text="Interval: ", width=30, anchor= W)
TxtVerzFilter = Label(PicParameter, text="Einschaltverzögerung Filter: ", width=30, anchor= W)
TxtDauer = Label(PicParameter, text="Einschaltdauer: ", width=30, anchor= W)

# Eingabe Felder
tsollInterval = Entry(PicParameter, width=35)
tverzFilter = Entry(PicParameter, width=35)
tsollDauer = Entry(PicParameter, width=35)

# Labels Istwert
tistInterval = Label(PicParameter, width=30)
tistverzFilter = Label(PicParameter, width=30)
tistDauer = Label(PicParameter, width=30)

# Packe Labels
tistInterval.grid(row=1, column=2)
tistverzFilter.grid(row=2, column=2)
tistDauer.grid(row=3, column=2)
# packe Labels ins Parameterfenster
TxtIst.grid(row=0, column=1, padx= 5, pady=5)
TxtSoll.grid(row=0, column=2, padx=5, pady=5)

TxtInterval.grid(row=1, column=0, padx=5, pady=10)
TxtVerzFilter.grid(row=2, column=0, padx=5, pady=10)
TxtDauer.grid(row=3, column=0, padx=5, pady=10)

# packe Eingabefelder ins Paramteterfenster
tsollInterval.grid(row=1, column=1)
tverzFilter.grid(row=2, column=1)
tsollDauer.grid(row=3, column=1)




def Auto():
    pass


def Hand():
    pass


def Service():
    pass


# Tastenleiste rechts
# Definiere Buttons
BtnAuto = Button(FeldRechts, text="Auto", command=Auto, width=width, height=height, justify=justify, font=font,
                 bg=str(Color))

BtnHand = Button(FeldRechts, text="Hand", command=Hand, width=width, height=height, justify=justify, font=font,
                 bg=str(Color))

BtnService = Button(FeldRechts, text="Service", command=Service, width=width, height=height, justify=justify, font=font,
                    bg=str(Color))

BtnStart = Button(FeldRechts, text="Start", command=start, width=width, height=height, justify=justify, font=font,
                  bg=str(Color))

BtnStopp = Button(FeldRechts, text="Stopp", command=stopp, width=width, height=height, justify=justify, font=font,
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
root.after(1000, blink)
root.mainloop()
