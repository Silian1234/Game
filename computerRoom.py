import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.computerRoom_scaled
NowLocationRect = imports.computerRoom_scaled_rect

walls = [
    Block.Block(params.WIDTH / (1920 / 1700), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 170), params.HEIGHT / (1080 / 242)),
    Block.Block(params.WIDTH / (1920 / 1700), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 160), params.HEIGHT / (1080 / 950)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 700), params.WIDTH / (1920 / 180), params.HEIGHT / (1080 / 250)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 650), params.WIDTH / (1920 / 1730), params.HEIGHT / (1080 / 300)),
    Block.Block(params.WIDTH / (1920 / 145), params.HEIGHT / (1080 / 500), params.WIDTH / (1920 / 190), params.HEIGHT / (1080 / 531)),
    Block.Block(params.WIDTH / (1920 / 100), params.HEIGHT / (1080 / 159), params.WIDTH / (1920 / 170), params.HEIGHT / (1080 / 242)),
    Block.Block(params.WIDTH / (1920 / 544), params.HEIGHT / (1080 / 100), params.WIDTH / (1920 / 170), params.HEIGHT / (1080 / 860)),
    Block.Block(params.WIDTH / (1920 / 210), params.HEIGHT / (1080 / 350), params.WIDTH / (1920 / 1350), params.HEIGHT / (1080 / 603))
]

activator = [
    Activator.Activator(params.WIDTH / (1920 / 395), params.HEIGHT / (1080 / 387), params.WIDTH / (1920 / 725), params.HEIGHT / (1080 / 563)),
    Activator.Activator(params.WIDTH / (1920 / 200), params.HEIGHT / (1080 / 200), params.WIDTH / (1920 / 1250), params.HEIGHT / (1080 / 700))
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(params.WIDTH / (1920 / 1300), params.HEIGHT / (1080 / 300), params.WIDTH / (1920 / 450), params.HEIGHT / (1080 / 650), imports.secondDialog)
]

newXPos = params.WIDTH / (1920 / 1610)
newYPos = params.HEIGHT / (1080 / 365)