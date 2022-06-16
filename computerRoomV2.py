import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.computerRoomV2_scaled
NowLocationRect = imports.computerRoomV2_scaled_rect

walls = [

]

activator = [
    Activator.Activator(369, 363, 723, 587)
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(1300, 300, 450, 650, imports.thirdDialog)
]

newXPos = params.WIDTH / (params.WIDTH / 1210)
newYPos = params.HEIGHT / (params.HEIGHT / 690)