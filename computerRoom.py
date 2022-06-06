import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.computerRoom_scaled
NowLocationRect = imports.computerRoom_scaled_rect

walls = [

]

activator = [
    Activator.Activator(200, 200, 1050, 250),
    Activator.Activator(200, 200, 1250, 700)
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(1300, 300, 450, 650, imports.secondDialog)
]

newXPos = 1700
newYPos = 600