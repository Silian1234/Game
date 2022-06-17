import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.bossRoom_scaled
NowLocationRect = imports.bossRoom_scaled_rect

walls = [

]

activator = [
    Activator.Activator(params.WIDTH / (1920 / 470), params.HEIGHT / (1080 / 300), params.WIDTH / (1920 / 1160), params.HEIGHT / (1080 / 390))
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(params.WIDTH / (1920 / 1300), params.HEIGHT / (1080 / 300), params.WIDTH / (1920 / 450), params.HEIGHT / (1080 / 650), imports.bossDialog)
]

newXPos = params.WIDTH / (1920 / 730)
newYPos = params.HEIGHT / (1080 / 730)