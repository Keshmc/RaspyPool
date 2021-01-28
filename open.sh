#!/bin/bash

#Shell öffnet matchbox-keyboard"
#Wird vom Python-Programm Raspy-Pool aufgerufen"
#Safe = /home/pi/Desktop/RaspyPool"

PID="$(pidof matchbox-keyboard)"
if [  "$PID" != ""  ]; then
  :
else
  matchbox-keyboard &
  fi


