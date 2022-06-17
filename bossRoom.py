import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.bossRoom_scaled
NowLocationRect = imports.bossRoom_scaled_rect

walls = [
    Block.Block(params.WIDTH / (1920 / 1700), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 150), params.HEIGHT / (1080 / 180)),
    Block.Block(params.WIDTH / (1920 / 522), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 150), params.HEIGHT / (1080 / 855)),
    Block.Block(params.WIDTH / (1920 / 900), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 888), params.HEIGHT / (1080 / 855)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 700), params.WIDTH / (1920 / 182), params.HEIGHT / (1080 / 180)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 700), params.WIDTH / (1920 / 1644), params.HEIGHT / (1080 / 180)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 700), params.WIDTH / (1920 / 662), params.HEIGHT / (1080 / 855)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 700), params.WIDTH / (1920 / 888), params.HEIGHT / (1080 / 855)),
    Block.Block(params.WIDTH / (1920 / 648), params.HEIGHT / (1080 / 140), params.WIDTH / (1920 / 582), params.HEIGHT / (1080 / 180)),
    Block.Block(params.WIDTH / (1920 / 160), params.HEIGHT / (1080 / 200), params.WIDTH / (1920 / 182), params.HEIGHT / (1080 / 734)),
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