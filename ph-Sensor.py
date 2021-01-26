import usb.core

# Anleitungsvideo
"https://www.youtube.com/watch?v=xfhzbw93rzw"

"============================================================================"
# Zuerst müssen die Variabeln fürs USB Gerät angepasst werden
# Linux Commands
"lsusb --> zeigt angeschlossene USB Geräte"
"lsusb -D /dev/bus/usb/#Num1/#Num2/"

# Configuration
idVendor = 0x045e
idProduct = 0x0040

"============================================================================="
# Definiere USB Gerät über ID
dev = usb.core.find(idVendor=idVendor, idProduct=idProduct)

# Endpoint
ep = dev[0].interfaces()[0].endpoints()[0]

# Interfacenummer
i = dev[0].interfaces()[0].bInterfaceNumber

# reset current Process
dev.reset()

# Falls gerade ein Prozess auf das USB Gerät zugreift, wird dieser ausgekoppelt damit Python darauf zugreifen kann.
if dev.is_kernel_driver_active(i):
    dev.detach_kernel_driver(i)

# Konfiguriere Device und setzte Endpointadresse
dev.set_configuration()
epaddr = ep.bEndpointAddress

# Lese Endpointadresse mit Anzahl Bytes
read = dev.read(epaddr, 1024)
print(len(read))
print(read)
