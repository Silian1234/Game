import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.workRoom_scaled
NowLocationRect = imports.workRoom_scaled_rect

walls = [

]

activator = [
    Activator.Activator(200, 200, 1050, 250)
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(1300, 300, 450, 650, imports.firstDialog)
]

newXPos = 1700
newYPos = 600