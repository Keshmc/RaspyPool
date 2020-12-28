# imports
from tkinter import *
from PIL import ImageTk, Image

"=== Initialisierung ========================================================================="
root = Tk()

# Farben
colBg = "#adc9c5"
colBtn = "#7e8282"
colBtnAktiv = "#ebae2d"
colBtnStart = "#6ceb2d"
colBtnStop = "#f02805"

# Parameter
imgPath = StringVar(root)
imgPath.set("HomeBild.png")

# Parameter für Buttons
height = 1
width = 10
justify = CENTER
font = "Arial"
padx = 5
pady = 5

"=== Bilder / Labels ========================================================================="
# Grundbild (Root)
root.title("Raspy Pool")
root.geometry("800x480")
root.configure(bg=str(colBg))

# Label für Projekttitel
labTitel = Label(root, text="RaspyPool; IDPA Projekt 2020", relief=RAISED)
labTitel.grid(row=0, column=0, columnspan=6, sticky=W + E)

# Label für Tastenfeld rechts
labFeldRechts = LabelFrame(root, width=105, height=400, bg=str(colBg))
labFeldRechts.grid(row=1, column=5, sticky=E)
labFeldRechts.grid_propagate(0)

# Label für Tastenfeld unten
labFeldUnten = LabelFrame(root, width=800, height=80, bg=str(colBg))
labFeldUnten.grid(row=5, column=0, columnspan=6, sticky=W + E)
labFeldUnten.grid_propagate(0)

# Label für Hauptanzeige
imgHome = ImageTk.PhotoImage(Image.open(imgPath.get()))
labPicHome = Label(root, image=imgHome, width=(800 - 105), height=400)
labPicHome.grid(row=1, column=0, rowspan=4, columnspan=4)
labPicHome.grid_propagate(0)

"=== Variabeln =========================================================================="
# Globale Varialbeln
Mode = StringVar(root)
befPump = BooleanVar(root)
befFilter = BooleanVar(root)
befHeat = BooleanVar(root)

# Sollwerte
tsollInterval = Entry()
tsollVerzFilter = Entry()
tsollDauer = Entry()

# Istwerte
tistInterval = Label()
tistVerzFilter = Label()
tistDauer = Label()

"=== Funktionen =========================================================================="


# Funktionen welche durch Buttons ausgeführt werden

# Betriebsmodus (Standard = Hand)
def setMode(arg="hand"):
    Mode.set(arg)
    return Mode.get()


def start():
    pass


# Tastenfeld unten
def home():
    global labPicHome
    global imgHome

    labPicHome.grid_forget()
    imgHome = ImageTk.PhotoImage(Image.open(str(imgPath.get())))
    labPicHome = Label(root, image=imgHome, width=(800 - 105), height=400)
    labPicHome.grid(row=1, column=0, rowspan=4, columnspan=4)
    labPicHome.grid_propagate(0)


def parameter():
    global labPicHome
    global tsollVerzFilter
    global tsollInterval
    global tsollDauer
    global tistVerzFilter
    global tistInterval
    global tistDauer

    # Labelfeld
    # Definition
    labPicHome.grid_forget()
    labPicHome = LabelFrame(root, bg=str(colBg), width=(800 - 101), height=400)

    # Platzierung
    labPicHome.grid(row=1, column=0, rowspan=4, columnspan=4)
    labPicHome.grid_propagate(0)

    # Labels und Texte
    # Definition der Labels für Texte
    TxtIstwert = Label(labPicHome, text="Istwert", width=15, font=font)
    TxtSollwert = Label(labPicHome, text="Sollwert", width=15, font=font)
    TxtInterval = Label(labPicHome, text="Interval: ", width=25, anchor=W, font=font)
    TxtVerzFilter = Label(labPicHome, text="Einschaltverzögerung Filter: ", width=25, anchor=W, font=font)
    TxtDauer = Label(labPicHome, text="Einschaltdauer: ", width=25, anchor=W, font=font)

    # Platziere die Texte
    TxtIstwert.grid(row=0, column=1, padx=5, pady=5)
    TxtSollwert.grid(row=0, column=2, padx=5, pady=5)
    TxtInterval.grid(row=1, column=0, padx=5, pady=10)
    TxtVerzFilter.grid(row=2, column=0, padx=5, pady=10)
    TxtDauer.grid(row=3, column=0, padx=5, pady=10)

    # Eingabe / Ausgabefenster
    # Definiere Sollwerte
    tsollInterval = Entry(labPicHome, width=15, font=str(font))
    tsollVerzFilter = Entry(labPicHome, width=15, font=str(font))
    tsollDauer = Entry(labPicHome, width=15, font=str(font))

    # Definmiere Istwerte
    tistInterval = Label(labPicHome, width=15, font=str(font))
    tistVerzFilter = Label(labPicHome, width=15, font=str(font))
    tistDauer = Label(labPicHome, width=15, font=str(font))

    # Platziere Sollwert
    tsollInterval.grid(row=1, column=1)
    tsollVerzFilter.grid(row=2, column=1)
    tsollDauer.grid(row=3, column=1)

    # Platziere Istwert
    tistInterval.grid(row=1, column=2)
    tistVerzFilter.grid(row=2, column=2)
    tistDauer.grid(row=3, column=2)


def pumpe(val):
    befPump.set(val)


def filtr(val):
    befFilter.set(val)


def heat(val):
    befHeat.set(val)

"=== Buttons =========================================================================="
# Buttons fürs Tastenfeld rechts
# Definition
BtnAuto = Button(labFeldRechts, command=lambda: setMode("auto"), text="Auto", width=width, height=height,
                 justify=justify, bg=str(colBtn),
                 font=str(font))
BtnHand = Button(labFeldRechts, text="Hand", command=lambda: setMode("hand"), width=width, height=height,
                 justify=justify, bg=str(colBtn),
                 font=str(font))
BtnService = Button(labFeldRechts, command=lambda: setMode("service"), text="Service", width=width, height=height,
                    justify=justify, bg=str(colBtn),
                    font=str(font))
BtnStart = Button(labFeldRechts, text="Start", width=width, height=height, justify=justify,
                  bg=str(colBtnStart),
                  font=str(font))
BtnStopp = Button(labFeldRechts, text="Stop", width=width, height=height, justify=justify, bg=str(colBtnStop),
                  font=str(font))
BtnSafe = Button(labFeldRechts, text="Speichern", width=width, height=height, justify=justify, bg=str(colBtn),
                 font=str(font))

# Platzierung
BtnAuto.grid(row=0, column=0, pady=5)
BtnHand.grid(row=1, column=0, pady=5)
BtnService.grid(row=2, column=0, pady=5)
BtnStart.grid(row=3, column=0, pady=(30, 5))
BtnStopp.grid(row=4, column=0, pady=(5, 30))
BtnSafe.grid(row=5, column=0, pady=10)

# Buttons fürs Tastenfeld unten
# Definition
BtnHome = Button(labFeldUnten, command=home, text="Home", width=width, height=height, justify=justify, bg=str(colBtn),
                 font=str(font))
BtnPump = Button(labFeldUnten, command=pumpe(True), text="Pumpe", width=width, height=height, justify=justify,
                 bg=str(colBtn),
                 font=str(font))
BtnFilter = Button(labFeldUnten, command=filtr(True), text="Filter", width=width, height=height, justify=justify,
                   bg=str(colBtn),
                   font=str(font))
BtnHeat = Button(labFeldUnten, command=heat(True), text="Heizung", width=width, height=height, justify=justify,
                 bg=str(colBtn),
                 font=str(font))
BtnParameters = Button(labFeldUnten, command=parameter, text="Parameters", width=width, height=height, justify=justify,
                       bg=str(colBtn),
                       font=str(font))
BtnExit = Button(labFeldUnten, command=root.quit, text="Exit", width=width, height=height, justify=justify,
                 bg=str(colBtn), font=str(font))

# Platzierung
BtnHome.grid(row=0, column=0, padx=10, pady=10)
BtnPump.grid(row=0, column=1, padx=10, pady=10)
BtnFilter.grid(row=0, column=2, padx=10, pady=10)
BtnHeat.grid(row=0, column=3, padx=10, pady=10)
BtnParameters.grid(row=0, column=4, padx=10, pady=10)
BtnExit.grid(row=0, column=5, padx=(95, 0), pady=10)

# Aufruf von Funktion
# setzte standard Modus auf Hand
setMode()

# Mainloop
root.mainloop()
