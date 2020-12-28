# Pythons IDPA Projekt Raspy Pool Main Cycle
from tkinter import *

import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


root = Tk()
root.geometry("800x480")

Mode = StringVar()

while Mode.get == "Auto":
    pass





root.mainloop()
while "hand":
    if GPIO.input(17) == 0:
        GPIO.output(18, GPIO.LOW)

    else:
        GPIO.output(18, GPIO.HIGH)

#Handbetrieb
#alles eigenständig ein und ausschalten

# Automatikbetrieb
# alles automatisch laufen und filter soll verspätet einschalten

# Servicebetrieb
# nur pumpe

# Variabeln
Mode = StringVar(root)
befPump = BooleanVar(root)
befFilter = BooleanVar(root)
befHeat = BooleanVar(root)

tsollInterval = Entry()
tsollverFilter = Entry()

Mode.get() #Wert aus Variabel

