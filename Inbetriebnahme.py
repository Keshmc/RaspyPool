# import
from tkinter import *
from gpiozero import DigitalOutputDevice

# Define Pins
Filter = DigitalOutputDevice(6)
Pumpe = DigitalOutputDevice(13)
Heizung = DigitalOutputDevice(19)
Reserve = DigitalOutputDevice(26)

# Farben
colBtn = "#7e8282"
colBtnEin = "#08c43a"

root = Tk()
root.title("Raspy Pool")
root.geometry("800x480")


def filtr():
    if BtnFilter.config("bg")[-1] == str(colBtn):
        BtnFilter.config(bg=str(colBtnEin))
        Filter.on()
    else:
        BtnFilter.config(bg=str(colBtn))
        Filter.off()


def pumpe():
    if BtnPumpe.config("bg")[-1] == str(colBtn):
        BtnPumpe.config(bg=str(colBtnEin))
        Pumpe.on()
    else:
        BtnPumpe.config(bg=str(colBtn))
        Pumpe.off()


def heizung():
    if BtnHeizung.config("bg")[-1] == str(colBtn):
        BtnHeizung.config(bg=str(colBtnEin))
        Heizung.on()
    else:
        BtnHeizung.config(bg=str(colBtn))
        Heizung.off()


def reserve():
    if BtnReserve.config("bg")[-1] == str(colBtn):
        BtnReserve.config(bg=str(colBtnEin))
        Reserve.on()
    else:
        BtnReserve.config(bg=str(colBtn))
        Reserve.off()

# definiere Buttons
BtnFilter = Button(root, text="Filter", command=filtr, width= 40, font= "Arial", bg= colBtn, height= 2)
BtnPumpe = Button(root, text="Pumpe", command=pumpe, width= 40, font= "Arial", bg= colBtn, height= 2)
BtnHeizung = Button(root, text="Heizung", command=heizung, width= 40, font= "Arial", bg= colBtn, height= 2)
BtnReserve = Button(root, text="Reserve", command=reserve, width= 40, font= "Arial", bg= colBtn, height= 2)

# platziere Buttons
BtnFilter.pack(pady=10)
BtnPumpe.pack(pady=10)
BtnHeizung.pack(pady=10)
BtnReserve.pack(pady=10)

root.mainloop()