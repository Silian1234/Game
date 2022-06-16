import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.bossRoom_scaled
NowLocationRect = imports.bossRoom_scaled_rect

walls = [

]

activator = [
    Activator.Activator(470, 300, 1160, 390)
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(1300, 300, 450, 650, imports.bossDialog)
]

newXPos = params.WIDTH / (params.WIDTH / 730)
newYPos = params.HEIGHT / (params.HEIGHT / 730)