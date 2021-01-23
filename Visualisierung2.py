# imports
from tkinter import *
from PIL import ImageTk, Image
import time

"=== Initialisierung ========================================================================="
root = Tk()

# Farben
colBg = "#adc9c5"
colBtn = "#7e8282"
colBtnAktiv = "#ebae2d"
colBtnEin = "#08c43a"
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
hmStart = BooleanVar(root)
hmStart.set(True)

# Sollwerte
tsollInterval = Entry(root)
tsollVerzFilter = Entry(root)
tsollDauer = Entry(root)

tInterval = str("hh:mm")
tVerzFilter = str("min")
tDauer = str("min")

# Istwerte
tistInterval = Label()
tistVerzFilter = Label()
tistDauer = Label()

# Zeiten
current = time.strftime("%H:%M")

# Befehle
befPumpHand = BooleanVar(root)
befFilterHand = BooleanVar(root)
befHeatHand = BooleanVar(root)
befPumpAuto = BooleanVar(root)
befFilterAuto = BooleanVar(root)
befHeatAuto = BooleanVar(root)
befTime = BooleanVar(root)
befTimeVerzFilter = BooleanVar(root)

"=== Funktionen =========================================================================="


# Mainschlaufe des Ablaufs
# wird mit Start() gestartet und mit Stopp() abgebrochen
def Ablauf():
    # Abbruchbedingung
    if hmStart.get() is False:
        return

    root.after(1000, Ablauf)


def Time():
    global tDauer
    global tInterval
    global tVerzFilter


    # wandle Zeiten in Floats zum Rechnen
    actual = float(time.strftime("%H%M"))
    ConvInterval = float(tInterval.replace(":", ""))
    ConvtDauer = float(tDauer)
    ConvFilter = float(tVerzFilter)

    # Berechne Endzeit
    if ConvtDauer > 60:
        tEnd = ConvInterval + (ConvtDauer * 100/60)
    else:
        tEnd = ConvInterval + ConvtDauer

    if ConvFilter > 60:
        tFgFilter = ConvInterval + (ConvFilter * 100/60)
    else:
        tFgFilter = ConvInterval + ConvFilter

    print("Ende =" + str(tEnd))
    print("Filter =" + str(tFgFilter))


    # Vergleich
    if ConvInterval< actual < tEnd:
        print("FgTime")

    if tFgFilter < actual < tEnd:
        print("Filter Ein")

    root.after(1000, Time)


# Funktionen welche durch Buttons ausgeführt werden
# Betriebsmodus (Standard = Hand)
def setMode(arg="dummy"):
    # Modus wird von Button über Argument mit (hand / auto oder service) beschrieben
    Mode.set(arg)
    Visualisierung(arg)
    return Mode.get()


# Start / Stopp Funktion, startet die LoopFuntkion Ablauf()
def start(val):
    hmStart.set(val)
    Ablauf()


# Tastenfeld unten
def pumpe():
    if BtnPumpe.config("bg")[-1] == str(colBtn):
        BtnPumpe.config(bg=str(colBtnEin))
        befPumpHand.set(True)
    else:
        BtnPumpe.config(bg=str(colBtn))
        befPumpHand.set(False)


def filtr():
    if BtnFilter.config("bg")[-1] == str(colBtn):
        BtnFilter.config(bg=str(colBtnEin))
        befFilterHand.set(True)
    else:
        BtnFilter.config(bg=str(colBtn))
        befFilterHand.set(False)


def heat():
    if BtnHeat.config("bg")[-1] == str(colBtn):
        BtnHeat.config(bg=str(colBtnEin))
        befHeatHand.set(True)
    else:
        BtnHeat.config(bg=str(colBtn))
        befHeatHand.set(False)


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
    global tInterval
    global tDauer
    global tVerzFilter

    # Labelfeld
    # Definition
    labPicHome.grid_forget()
    labPicHome = LabelFrame(root, bg=str(colBg), width=(800 - 101), height=400)

    # Platzierung
    labPicHome.grid(row=1, column=0, rowspan=4, columnspan=4)
    labPicHome.grid_propagate(0)

    # Labels und Texte
    # Definition der Labels für Texte
    TxtIstwert = Label(labPicHome, text="Sollwert", width=15, font=font)
    TxtSollwert = Label(labPicHome, text="Istwert", width=15, font=font)
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

    # Definiere Istwerte
    tistInterval = Label(labPicHome, text=" ", width=15, font=str(font))
    tistVerzFilter = Label(labPicHome, text="Time", width=15, font=str(font))
    tistDauer = Label(labPicHome, text="Time", width=15, font=str(font))

    # Platziere Istwert
    tistInterval.grid(row=1, column=2)
    tistVerzFilter.grid(row=2, column=2)
    tistDauer.grid(row=3, column=2)

    # Platziere Sollwert
    tsollInterval.grid(row=1, column=1)
    tsollVerzFilter.grid(row=2, column=1)
    tsollDauer.grid(row=3, column=1)

    # setze Sollwert
    tsollInterval.insert(0, str(tInterval))
    tsollDauer.insert(0, str(tDauer))
    tsollVerzFilter.insert(0, str(tVerzFilter))

    clock()


def clock():
    global current

    # Istwerte werden aktualisiert
    tistInterval.configure(text=str(current))
    tistDauer.configure(text=str("Time"))
    tistVerzFilter.configure(text=str("Time"))

    root.after(1000, clock)


def safe():
    global tInterval
    global tDauer
    global tVerzFilter

    # speichere Sollwerte
    # Sollwert Interval
    tInterval = tsollInterval.get()
    tsollInterval.delete(0, END)
    tsollInterval.insert(0, tInterval)

    # Sollwert Dauer
    tDauer = tsollDauer.get()
    tsollDauer.delete(0, END)
    tsollDauer.insert(0, str(tDauer))

    # Sollwert Verzögerung Filter
    tVerzFilter = tsollVerzFilter.get()
    tsollVerzFilter.delete(0, END)
    tsollVerzFilter.insert(0, str(tVerzFilter))

    Time()


"=== Visualisierung =========================================================================="


def Visualisierung(arg):
    # Visualisierung nach Modus

    # Automodus
    if arg == "auto":
        # Buttons Modus
        BtnAuto.config(bg=colBtnAktiv)
        BtnHand.config(bg=colBtn)
        BtnService.config(bg=colBtn)

        # Disable Handfunktionen
        BtnPumpe.config(stat=DISABLED)
        BtnFilter.config(stat=DISABLED)
        BtnHeat.config(stat=DISABLED)

    # Handmodus
    if arg == "hand":
        # Buttons Modus
        BtnAuto.config(bg=colBtn)
        BtnHand.config(bg=colBtnAktiv)
        BtnService.config(bg=colBtn)

        # Disable Handfunktionen
        BtnPumpe.config(stat=NORMAL)
        BtnFilter.config(stat=NORMAL)
        BtnHeat.config(stat=NORMAL)

    # Service Modus
    if arg == "service":
        # Buttons Modus
        BtnAuto.config(bg=colBtn)
        BtnHand.config(bg=colBtn)
        BtnService.config(bg=colBtnAktiv)

        # Disable Handfunktionen
        BtnPumpe.config(stat=DISABLED)
        BtnFilter.config(stat=DISABLED)
        BtnHeat.config(stat=DISABLED)

    # kein Modus (dummy)
    if arg == "dummy":
        # Buttons Modus
        BtnAuto.config(bg=colBtn)
        BtnHand.config(bg=colBtn)
        BtnService.config(bg=colBtn)

        # Disable Handfunktionen
        BtnPumpe.config(stat=DISABLED)
        BtnFilter.config(stat=DISABLED)
        BtnHeat.config(stat=DISABLED)

    root.update()


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
BtnStart = Button(labFeldRechts, command=lambda: start(True), text="Start", width=width, height=height, justify=justify,
                  bg=str(colBtn),
                  font=str(font))
BtnStopp = Button(labFeldRechts, command=lambda: start(False), text="Stop", width=width, height=height, justify=justify,
                  bg=str(colBtn),
                  font=str(font))
BtnSafe = Button(labFeldRechts, command=safe, text="Speichern", width=width, height=height, justify=justify,
                 bg=str(colBtn),
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
BtnPumpe = Button(labFeldUnten, command=pumpe, text="Pumpe", width=width, height=height, justify=justify,
                  bg=str(colBtn),
                  font=str(font))
BtnFilter = Button(labFeldUnten, command=filtr, text="Filter", width=width, height=height, justify=justify,
                   bg=str(colBtn),
                   font=str(font))
BtnHeat = Button(labFeldUnten, command=heat, text="Heizung", width=width, height=height, justify=justify,
                 bg=str(colBtn),
                 font=str(font))
BtnParameters = Button(labFeldUnten, command=parameter, text="Parameters", width=width, height=height, justify=justify,
                       bg=str(colBtn),
                       font=str(font))
BtnExit = Button(labFeldUnten, command=root.quit, text="Exit", width=width, height=height, justify=justify,
                 bg=str(colBtn), font=str(font))

# Platzierung
BtnHome.grid(row=0, column=0, padx=10, pady=10)
BtnPumpe.grid(row=0, column=1, padx=10, pady=10)
BtnFilter.grid(row=0, column=2, padx=10, pady=10)
BtnHeat.grid(row=0, column=3, padx=10, pady=10)
BtnParameters.grid(row=0, column=4, padx=10, pady=10)
BtnExit.grid(row=0, column=5, padx=(95, 0), pady=10)

# Aufruf von Funktion
# setzte standard Modus auf Hand
setMode()
clock()

# Mainloop
root.mainloop()
