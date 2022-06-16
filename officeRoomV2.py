import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.officeRoomV2_scaled
NowLocationRect = imports.officeRoomV2_scaled_rect

walls = [

]

activator = [
    Activator.Activator(517, 295, 570, 500)
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(1300, 300, 450, 650, imports.officeRoomDialogV2)
]

newXPos = params.WIDTH / (params.WIDTH / 487)
newYPos = params.HEIGHT / (params.HEIGHT / 400)