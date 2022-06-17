import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.computerRoomV4_scaled
NowLocationRect = imports.computerRoomV4_scaled_rect

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
    Activator.Activator(params.WIDTH / (1920 / 230), params.HEIGHT / (1080 / 245), params.WIDTH / (1920 / 1658), params.HEIGHT / (1080 / 215))
]

NPSSS = [

]

dialog_window = [

]

newXPos = params.WIDTH / (1920 / 583)
newYPos = params.HEIGHT / (1080 / 355)