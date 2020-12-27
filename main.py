# Pythons IDPA Projekt Raspy Pool Main Cycle
from tkinter import *

import RPi.GPIO as GPIO

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
