#!/bin/bash

#Shell schliesst matchbox-keyboard wenn dieses offen ist
#Wird vom Python-Programm Raspy-Pool aufgerufen
#Safe = /home/pi/Desktop/RaspyPool

PID="$(pidof matchbox-keyboard)"
if [  "$PID" != ""  ]; then
  kill $PID
  fi
  
