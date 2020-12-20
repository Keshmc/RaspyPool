from tkinter import *

# Main Root
root = Tk()
root.title("Raspy Pool IDPA")
root.geometry("800x480")

# Parameter Buttons
width = 20
padx = 5
pady = 5
widht = 20
height = 1
justify = CENTER
Color = str("#70706c")
ColorActive = str("#e8c010")

# Frame Tastenfeld links
FeldLinks = LabelFrame(root, padx=5, pady=5)
FeldLinks.grid(row=0, column=5)

# Betriebsarten
ModeHand = StringVar(root)
ModeHand.set("ModeHand")
Mode = StringVar(root)


# FlipFlops für Mode Tasten
def toggleHand(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        Mode.set("ModeHand")

    else:
        pass


# def toggleAuto(tog=[0]):
#     global Mode
#     tog[0] = not tog[0]
#     if tog[0]:
#         Mode = ModeAuto
#     else:
#         pass
#
#
# def toggleService(tog=[0]):
#     global Mode
#     tog[0] = not tog[0]
#     if tog[0]:
#         Mode = ModeService
#     else:
#         pass


# Betriebsarten
# Betriebsart Hand
if Mode.get() == "ModeHand":
    print("Juhuuuuu")

bgHand = Color
bgAuto = Color
bgService = Color

BtnHand = Button(FeldLinks, text="Hand", padx=padx, pady=5, width=widht, height=height, justify=str(justify), bg=bgHand,
                 command=toggleHand)
BtnAuto = Button(FeldLinks, text="Auto", padx=padx, pady=5, width=widht, height=height, justify=str(justify), bg=bgAuto)
BtnService = Button(FeldLinks, text="Service", padx=padx, pady=5, width=widht, height=height, justify=str(justify),
                    bg=bgService)

# Verschiebe die Buttons ins Tastenfeld links
BtnAuto.grid(row=0, column=0)
BtnHand.grid(row=1, column=0)
BtnService.grid(row=2, column=0)

# Main Loop
root.mainloop()
