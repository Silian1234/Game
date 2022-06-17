import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.officeRoom_scaled
NowLocationRect = imports.officeRoom_scaled_rect

walls = [
    Block.Block(params.WIDTH / (1920 / 700), params.HEIGHT / (1080 / 450), params.WIDTH / (1920 / 769), params.HEIGHT / (1080 / 100)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 700), params.WIDTH / (1920 / 880), params.HEIGHT / (1080 / 510)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 300), params.WIDTH / (1920 / 662),params.HEIGHT / (1080 / 792)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 700), params.WIDTH / (1920 / 182),params.HEIGHT / (1080 / 110)),
    Block.Block(params.WIDTH / (1920 / 700), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 182),params.HEIGHT / (1080 / 135)),
    Block.Block(params.WIDTH / (1920 / 480), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 182),params.HEIGHT / (1080 / 792)),
]

activator = [
    Activator.Activator(params.WIDTH / (1920 / 367), params.HEIGHT / (1080 / 270), params.WIDTH / (1920 / 670), params.HEIGHT / (1080 / 520))
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(params.WIDTH / (1920 / 1300), params.HEIGHT / (1080 / 300), params.WIDTH / (1920 / 450), params.HEIGHT / (1080 / 650), imports.officeRoomDialog)
]

newXPos = params.WIDTH / (1920 / 733)
newYPos = params.HEIGHT / (1080 / 900)