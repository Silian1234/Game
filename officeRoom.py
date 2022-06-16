import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.officeRoom_scaled
NowLocationRect = imports.officeRoom_scaled_rect

walls = [

]

activator = [
    Activator.Activator(367, 270, 670, 520)
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(1300, 300, 450, 650, imports.officeRoomDialog)
]

newXPos = params.WIDTH / (params.WIDTH / 733)
newYPos = params.HEIGHT / (params.HEIGHT / 900)