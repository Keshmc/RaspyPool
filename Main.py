# imports
from tkinter import *
from PIL import ImageTk, Image
from subprocess import call
from gpiozero import DigitalOutputDevice
import time

"=== Initialisierung ========================================================================="
root = Tk()

# Farben
colBg = "#ffffff"
colBtn = "#7e8282"
colBtnAktiv = "#ebae2d"
colBtnEin = "#11cd55"
colBtnStart = "#6ceb2d"
colBtnStop = "#f02805"
colMeldung = "#000000"
colAlarm = "#fd2a00"

# Parameter
imgPath = StringVar(root)

try:
    imgPath.set("/home/pi/RaspyPool/HomeBild.png")
    Image.open(imgPath.get())
except FileNotFoundError:
    imgPath.set("HomeBild.png")
    Image.open(imgPath.get())

# Parameter für Buttons
height = 1
width = 10
justify = CENTER
font = "Arial"
padx = 5
pady = 5

# Definiere Output Pins
try:
    OutFilter = DigitalOutputDevice(6)
    OutPumpe = DigitalOutputDevice(13)
    OutHeizung = DigitalOutputDevice(19)
    OutReserve = DigitalOutputDevice(26)
except ModuleNotFoundError:
    pass

"=== Bilder / Labels ========================================================================="
# Grundbild (Root)
root.title("Raspy Pool")
root.geometry("800x480")
root.configure(bg=str(colBg))

# Label für Projekttitel
labTitel = Label(root, text="RaspyPool; IDPA Projekt 2020", anchor=W, padx=50, pady=5, relief=RAISED, font=str(font))
labTitel.grid(row=0, column=0, columnspan=6, sticky=W + E)

# Label für Meldungen
LabelMeldung = Label(root, text="Meldefenster", anchor=W, padx=50, pady=5, bg="#f2fcf5", font=str(font),
                     fg=str(colMeldung), relief=SUNKEN, bd=5)
LabelMeldung.grid(row=1, column=0, columnspan=6, sticky=W + E + N)
LabelMeldung.grid_propagate(0)

# Label für Hauptanzeige

imgHome = ImageTk.PhotoImage(Image.open(imgPath.get()))
labPicHome = Label(root, image=imgHome, bg=str(colBg), width=(800 - 120), height=330)
labPicHome.grid(row=2, column=0, rowspan=4, columnspan=5)
labPicHome.grid_propagate(0)

# Label für pH-Sensor
labPHSensor = Label(root, text="pH-Wert:  " + str(1), font=(str(font), 16))
labPHSensor.grid(row=5, column=0)

# Label für Tastenfeld rechts
labFeldRechts = LabelFrame(root, width=120, height=380, bg=str(colBg))
labFeldRechts.grid(row=1, column=5, rowspan=5, sticky=E + N)
labFeldRechts.grid_propagate(0)

# Label für Tastenfeld unten
labFeldUnten = LabelFrame(root, width=800, height=80, bg=str(colBg))
labFeldUnten.grid(row=6, column=0, columnspan=6, sticky=W + E)
labFeldUnten.grid_propagate(0)

"=== Variabeln =========================================================================="
# Globale Varialbeln
Mode = StringVar(root)
hmStart = BooleanVar(root)
hmStart.set(True)
hmSafe = BooleanVar(root)
hmKeyboard = BooleanVar(root).set(0)

# Sollwerte
tsollInterval = Entry(root)
tsollVerzFilter = Entry(root)
tsollDauer = Entry(root)

tInterval = str("#Wert")
tVerzFilter = str("#Wert")
tDauer = str("#Wert")

# Istwerte
istLabelTime = Label()
istLabelVerzFilter = Label()
istLabelDauer = Label()

tistVerzFilter = float()
tistDauer = float()
actual = float()
ConvInterval = float()
ConvtDauer = float()
ConvFilter = float()

# Zeiten
current = time.strftime("%H:%M")

# Befehle
befPumpHand = BooleanVar(root)
befFilterHand = BooleanVar(root)
befHeatHand = BooleanVar(root)
befOutAuto = BooleanVar(root)
befOutAutoFilter = BooleanVar(root)
befOutService = BooleanVar(root)

"=== Funktionen =========================================================================="


def Time():
    global tDauer
    global tInterval
    global tVerzFilter
    global ConvInterval
    global ConvtDauer
    global ConvFilter

    # wandle Zeiten in Floats zum Rechnen
    try:
        ConvInterval = float(tInterval.replace(":", ""))
        ConvtDauer = float(tDauer)
        ConvFilter = float(tVerzFilter)

        # Meldung
        LabelMeldung.configure(text="Meldung: Sollwerte gespeichert", fg=str(colMeldung))
        hmSafe.set(True)

    except ValueError:
        # Meldung
        LabelMeldung.configure(text="Alarm: Sollwerte konnten nicht gespeichert werden!", fg=str(colAlarm))
        hmSafe.set(False)
        return


def compTime():
    global befOutAuto
    global befOutAutoFilter
    global tistDauer
    global tistVerzFilter
    global actual
    global ConvInterval
    global ConvtDauer
    global ConvFilter

    # Vergleiche aktuelle Zeit
    actual = float(time.strftime("%H%M"))

    # Meldung wenn tVerzFilter grösser ist als Dauer
    if ConvFilter > ConvtDauer:
        LabelMeldung.configure(text="Alarm: Verzögerung Filter grösser als Einschaltdauer!", fg=str(colAlarm))

    # Berechne Endzeit
    if ConvtDauer > 60:
        tEnd = ConvInterval + (ConvtDauer * 100 / 60)
    else:
        tEnd = ConvInterval + ConvtDauer

    if ConvFilter > 60:
        tFgFilter = ConvInterval + (ConvFilter * 100 / 60)
    else:
        tFgFilter = ConvInterval + ConvFilter

    # Setzte befAuto
    if ConvInterval <= actual < tEnd and Mode.get() == "auto" and hmSafe.get():
        befOutAuto.set(True)
        tistDauer = tEnd - actual

    else:
        befOutAuto.set(False)
        tistDauer = ConvtDauer

    if tFgFilter <= actual <= tEnd and Mode.get() == "auto" and hmSafe.get():
        befOutAutoFilter.set(True)
    else:
        befOutAutoFilter.set(False)

    # Berechnung Istwert Einschaltverzögerung Filter
    if ConvInterval < actual < tFgFilter:
        tistVerzFilter = tFgFilter - actual
    else:
        tistVerzFilter = ConvFilter


# Mainschlaufe des Ablaufs
# wird mit Start() gestartet und mit Stopp() abgebrochen
def Ablauf():
    global befOutAuto
    global befOutAutoFilter
    global befFilterHand
    global befHeatHand
    global befPumpHand
    global hmSafe

    # Abbruchbedingung
    if hmStart.get() is False:
        # setzte alle Befehle zurück
        # Auto
        befOutAuto.set(False)
        befOutAutoFilter.set(False)

        # Hand
        befPumpHand.set(False)
        befHeatHand.set(False)
        befFilterHand.set(False)

        # Service
        befOutService.set(False)

        # setze alle Ausgänge und Statusanzeigen zurück
        try:
            # setzte Status der Buttons zurück
            BtnFilter.configure(bg=colBtn)
            BtnPumpe.configure(bg=colBtn)
            BtnHeat.configure(bg=colBtn)

            # setzte alle Ausgänge zurück
            OutFilter.off()
            OutPumpe.off()
            OutHeizung.off()
            OutReserve.off()
        except NameError:
            pass

        # Meldung
        LabelMeldung.configure(text="Meldung: Anlage stoppt.", fg=str(colMeldung))
        return

    # Frage Fkt Zeitvergleich auto ab
    compTime()

    # frage Service Betrieb ab
    # setzte bef Service
    if Mode.get() == "service":
        befOutService.set(True)
    else:
        befOutService.set(False)

    # Out Pumpe
    if befOutAuto.get() or befPumpHand.get() or befOutService.get():
        # OutPumpe.on()
        BtnPumpe.configure(bg=colBtnEin)
    else:
        # OutPumpe.off()
        BtnPumpe.configure(bg=colBtn)

    # Out Heizung
    if befOutAuto.get() or befHeatHand.get() or befOutService.get():
        # OutHeizung.on()
        BtnHeat.configure(bg=colBtnEin)
    else:
        # OutHeizung.off()
        BtnHeat.configure(bg=colBtn)

    # Out Filter
    if befFilterHand.get() or befOutAutoFilter.get() and not befOutService.get():
        # OutFilter.on()
        BtnFilter.configure(bg=colBtnEin)
    else:
        # OutFilter.off()
        BtnFilter.configure(bg=colBtn)

    root.after(1000, Ablauf)


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

    if val:
        BtnStart.configure(bg=colBtnStart)
        BtnStopp.configure(bg=colBtn)
    else:
        BtnStart.configure(bg=colBtn)
        BtnStopp.configure(bg=colBtnStop)

    # Meldungen
    if Mode.get() == "auto":
        if hmSafe.get():
            LabelMeldung.configure(text="Meldung: Modus Auto aktiv! (Zeitsteuerung)", fg=str(colMeldung))
        else:
            LabelMeldung.configure(text="Alarm: Auto kann nicht gestartet werden. Sollwerte eingeben!",
                                   fg=str(colAlarm))
            # Configuriere StartButtons
            BtnStart.configure(bg=colBtn)
            BtnStopp.configure(bg=colBtnStop)

    if Mode.get() == "hand":
        LabelMeldung.configure(text="Meldung: Modus Hand aktiv! Aktoren können manuell gesteuert werden.",
                               fg=str(colMeldung))

    if Mode.get() == "service":
        LabelMeldung.configure(text="Meldung: Modus Service aktiv! UV-C Filter bleibt ausgeschalten.",
                               fg=str(colMeldung))
    Ablauf()


# Tastenfeld unten
def pumpe():
    if BtnPumpe.config("bg")[-1] == str(colBtn):
        BtnPumpe.config(bg=str(colBtnAktiv))
        if Mode.get() == "hand":
            befPumpHand.set(True)
    else:
        BtnPumpe.config(bg=str(colBtn))
        befPumpHand.set(False)


def filtr():
    if BtnFilter.config("bg")[-1] == str(colBtn):
        BtnFilter.config(bg=str(colBtnAktiv))
        if Mode.get() == "hand":
            befFilterHand.set(True)
    else:
        BtnFilter.config(bg=str(colBtn))
        befFilterHand.set(False)


def heat():
    if BtnHeat.config("bg")[-1] == str(colBtn):
        BtnHeat.config(bg=str(colBtnAktiv))
        if Mode.get() == "hand":
            befHeatHand.set(True)
    else:
        BtnHeat.config(bg=str(colBtn))
        befHeatHand.set(False)


def callpHSensor():
    # führe Bash-Script für pH-Wert Aufnahme aus
    try:
        call("bash /home/pi/RaspyPool/pH-Sensor.sh", shell=True)
    except FileNotFoundError:
        LabelMeldung.configure(text="Alarm: pH-Sensor konnte nicht gepingt werden", fg=colAlarm)
        pass


def phSensor():
    global labPHSensor

    # Oeffne .txt Datei mit dem pH-Wert aus dem ftdi.py File
    # Hier muss variabel für pH-Wert gesetzt werden
    try:
        f = open("/home/pi/RaspyPool/pH-Sensor/ph.txt", "r")
        val = float(f.read(5))
        f.close()
    except FileNotFoundError:
        val = 0

    # pH-Wert von 0 bis 3 = rot
    if 0 <= val <= 3:
        labPHSensor.configure(text="pH-Wert:  " + str(val), bg="#ff0000")

    # pH-Wert von 3 bis 6 = orange
    if 3 < val <= 6:
        labPHSensor.configure(text="pH-Wert:  " + str(val), bg="#fe9a00")

    # pH-Wert von 6 bis 8 = grün
    if 6 < val <= 8:
        labPHSensor.configure(text="pH-Wert:  " + str(val), bg="#20fe06")

    # pH-Wert von 8 bis 11 = hellblau
    if 8 < val <= 11:
        labPHSensor.configure(text="pH-Wert:  " + str(val), bg="#00cbf0")

    # pH-Wert von 11 bis 14 = dunkelblau
    if 11 < val <= 14:
        labPHSensor.configure(text="pH-Wert:  " + str(val), bg="#6b65ec")

    root.after(1000, phSensor)


def home():
    global labPHSensor
    global labPicHome
    global imgHome

    # platziere Homebild
    labPicHome.grid_forget()
    imgHome = ImageTk.PhotoImage(Image.open(str(imgPath.get())))
    labPicHome = Label(root, image=imgHome, bg=str(colBg), width=(800 - 120), height=330)
    labPicHome.grid(row=2, column=0, rowspan=4, columnspan=5)
    labPicHome.grid_propagate(0)

    # platziere pH-Wert
    labPHSensor = Label(root, text="pH-Wert:  ", font=(str(font), 16))
    labPHSensor.grid(row=5, column=0)

    # führe Bash-Script für pH-Wert Aufnahem aus
    callpHSensor()
    phSensor()


# Call Funktionen für Tastatur

def callback():
    global hmKeyboard
    hmKeyboard = BooleanVar(root)
    try:
        # Shell Script verhindert Fehler mit infinte Loop
        if hmKeyboard.get() == 0:
            call("bash /home/pi/RaspyPool/open.sh", shell=True)
            hmKeyboard.set(True)
    except FileNotFoundError:
        hmKeyboard.set(False)
        pass


def callout():
    global hmKeyboard
    hmKeyboard = BooleanVar(root)
    try:
        # Shell Script nimmt PID und schliesst Tastatur
        call("bash /home/pi/RaspyPool/close.sh", shell=True)
        hmKeyboard.set(0)
    except FileNotFoundError:
        pass


def parameter():
    global labPicHome
    global tsollVerzFilter
    global tsollInterval
    global tsollDauer
    global istLabelVerzFilter
    global istLabelTime
    global istLabelDauer
    global tInterval
    global tDauer
    global tVerzFilter

    # Entferne Label für pH-Sensor
    labPHSensor.grid_forget()

    # Labelfeld
    # Definition
    labPicHome.grid_forget()
    labPicHome = LabelFrame(root, bg=str(colBg), width=(800 - 116), height=335)

    # schliesse Bildschirmtastatur beim rauscklicken
    labPicHome.bind("<Button-1>", callout)

    # Platzierung
    labPicHome.grid(row=2, column=0, rowspan=4, columnspan=5)
    labPicHome.grid_propagate(0)

    # Labels und Texte
    # Definition der Labels für Texte
    TxtIstwert = Label(labPicHome, text="Sollwert", width=15, font=font)
    TxtSollwert = Label(labPicHome, text="Istwert", width=15, font=font)
    TxtInterval = Label(labPicHome, text="Einschaltzeit: ", width=25, anchor=W, font=font)
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
    tsollInterval = Entry(labPicHome, width=15, font=str(font), bd=3)
    tsollVerzFilter = Entry(labPicHome, width=15, font=str(font), bd=3)
    tsollDauer = Entry(labPicHome, width=15, font=str(font), bd=3)

    # bef Oeffne Bildschirmtastatur
    tsollInterval.bind("<FocusIn>", callback)
    tsollVerzFilter.bind("<FocusIn>", callback)
    tsollVerzFilter.bind("<FocusIn>", callback)

    # Definiere Istwerte
    istLabelTime = Label(labPicHome, text=" ", width=15, font=str(font))
    istLabelVerzFilter = Label(labPicHome, text=" ", width=15, font=str(font))
    istLabelDauer = Label(labPicHome, text=" ", width=15, font=str(font))

    # Platziere Istwert
    istLabelTime.grid(row=1, column=2)
    istLabelVerzFilter.grid(row=2, column=2)
    istLabelDauer.grid(row=3, column=2)

    # Platziere Sollwert
    tsollInterval.grid(row=1, column=1)
    tsollVerzFilter.grid(row=2, column=1)
    tsollDauer.grid(row=3, column=1)

    # setze Sollwert
    tsollInterval.insert(0, str(tInterval) + " Uhr")
    tsollDauer.insert(0, str(tDauer) + " min")
    tsollVerzFilter.insert(0, str(tVerzFilter) + " min")

    clock()


def clock():
    global current
    global tistDauer
    global tistVerzFilter

    # Zeiten updaten
    current = time.strftime("%H:%M")

    # Istwerte werden aktualisiert

    istLabelTime.configure(text=str(current) + " Uhr")
    istLabelDauer.configure(text=str(tistDauer) + " min")
    istLabelVerzFilter.configure(text=str(tistVerzFilter) + " min")

    root.after(1000, clock)


def safe():
    global tInterval
    global tDauer
    global tVerzFilter

    # speichere Sollwerte
    # Sollwert Interval
    a = tsollInterval.get()
    tInterval = a.replace(" Uhr", "").replace("hh:mm", "")
    tsollInterval.delete(0, "end")
    tsollInterval.insert(0, str(tInterval) + " Uhr")

    # Sollwert Dauer
    b = tsollDauer.get()
    tDauer = b.replace(" min", "").replace("min", "")
    tsollDauer.delete(0, "end")
    tsollDauer.insert(0, str(tDauer) + " min")

    # Sollwert Verzögerung Filter
    c = tsollVerzFilter.get()
    tVerzFilter = c.replace(" min", "").replace("min", "")
    tsollVerzFilter.delete(0, "end")
    tsollVerzFilter.insert(0, str(tVerzFilter) + " min")

    Time()


"=== Visualisierung =========================================================================="


def Visualisierung(arg):
    m = StringVar(root)

    # Ausgänge werden nach Moduswechsel zurückgesetzt
    if m.get() != str(arg):
        m.set(arg)
        start(False)

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

        # Meldungen
        LabelMeldung.configure(text="Meldung: Modus Auto angewählt. Start betätigen.", fg=str(colMeldung))

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

        # Meldungen
        LabelMeldung.configure(text="Meldung: Modus Hand angewählt. Start betätigen.", fg=str(colMeldung))

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

        # Meldungen
        LabelMeldung.configure(text="Meldung: Modus Service angewählt. Start betätigen.", fg=str(colMeldung))

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

        # Meldungen
        LabelMeldung.configure(text="Alarm: kein Modus angewählt. Bitte Modus auswählen", fg=str(colAlarm))

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
BtnSafe = Button(labFeldRechts, command=safe, text="  speichern", width=width, height=height, justify=justify,
                 bg=str(colBtn), font=str(font), anchor=W)

# Platzierung
BtnAuto.grid(row=0, column=0, pady=(10, 5))
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

# Platzierung
BtnHome.grid(row=0, column=0, padx=5, pady=10)
BtnPumpe.grid(row=0, column=1, padx=10, pady=10)
BtnFilter.grid(row=0, column=2, padx=10, pady=10)
BtnHeat.grid(row=0, column=3, padx=10, pady=10)
BtnParameters.grid(row=0, column=4, padx=10, pady=10)

# Aufruf von Funktion
# setzte standard Modus auf Hand
setMode()
clock()
phSensor()

# Mainloop
root.mainloop()
