#!/bin/bash

#Shell öffnet Python2 Programm von Atlas Scientif und fragt pH-Wert ab"
#Wird vom Python Programm Raspy-Pool aufgerufen"
#Safe = /home/pi/Desktop/RaspyPool"

PID="$(pidof python)"

if [  "$PID" != ""  ]; then

  echo "#SH pH-Sensor -- Prozess bereits aktiv"

else
  cd /home/pi/RaspyPool/pH-Sensor || exit
  sudo python ftdi.py &
fi
