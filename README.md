# RaspyPool
This RaspyPool project was implemented as an IDPA project of the Berufsmaturitätsschule St.Gallen. The Python program is designed for a Raspberry Pi 4 (8GB), 
but can be run on any System where Python is installed. The Poolsteering can control the following devices:
- a filter pump
- a UVC filter 
- a heater
- a pH-Sensor from Atlas Scientific (USB)

To ensure the function of the steering, the hardware has to be rebuilt according to the Wiring Diagram and Dispo. We used the pH-Sample from [Atlas Scientific.](https://atlas-scientific.com/carrier-boards/electrically-isolated-usb-ezo-carrier-board/)
For more Information and Details to the Hardware and Software see the [Dokumentation_DE.](../master/Dokumentation_DE/IDPA_Poolsteuerung_Dokumentation.pdf)

# Installation on Raspberry Pi
This is a provisional installation guide. A detailed version is still in work.

1. Make sure that you have installed match-box keyboard. This step is optional. <br/>
   Guide: [matchbox-keyboard](https://pimylifeup.com/raspberry-pi-on-screen-keyboard)

2. Download the RaspyPool Project to your Raspberry Pi. The folder structure must be saved under the following directory: 
> /home/pi/ "RaspyPool"

3. Move the Entry.desktop File from the autostart folder to the following directory:
> /etc/xdg/autostart

4. Move the MyApp.sh File from the autostart folder to the following directory:
> /usr/bin

The autostart should work now. The RaspyPool will run automatically after a reboot. 
``` bash 
$ sudo reboot 
```

For more Information see the [Dokumentation_DE.](../master/Dokumentation_DE/IDPA_Poolsteuerung_Dokumentation.pdf)


# Installation on your PC
This is a provisional installation guide. A detailed version is still in work

The project can be executed on the PC. The following functions cannot be guaranteed due to missing hardware:
- pH-Sensor
- GPIO Outputs
- Autostar

1. Make sure that you have Python3.9 installed to your PC.
   Guide: [Python3.9 YouTube Tutorial](https://www.youtube.com/watch?v=dyJdLalc7TA)
   
2. Download the RaspyPool Project.

3. Execute the Main.py. I show it for simplicity's sake using the standard Python IDLE as an example. The IDLE is automatically installed with Python.
   Any other IDE can be used. My favorite is [PyCharm by Jetbrains.](https://www.jetbrains.com/de-de/pycharm/)
   
   3.1 open IDLE (Python 3.9) <br/>
   3.2 got to `file > open > "Main.py" ` from the downloaded RaspyPool Folder <br/>
   3.3 the Main.py opens. Go to `run` and execute the File <br/>

For more Information see the [Dokumentation_DE.](../master/Dokumentation_DE/IDPA_Poolsteuerung_Dokumentation.pdf)









