import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.underground_scaled
NowLocationRect = imports.underground_scaled_rect

walls = [
    Block.Block(params.WIDTH / (1920 / 1920), params.HEIGHT / (1080 / 10), 0, params.HEIGHT / (1080 / 300)),
    Block.Block(params.WIDTH / (1920 / 960), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 960), params.HEIGHT / (1080 / 800)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 500), params.WIDTH / (1920 / 1615), params.HEIGHT / (1080 / 300)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 800), params.WIDTH / (1920 / 430), params.HEIGHT / (1080 / 300))
]

activator = [
    Activator.Activator(params.WIDTH / (1920 / 383), params.HEIGHT / (1080 / 163), params.WIDTH / (1920 / 846), params.HEIGHT / (1080 / 262))
]

NPSSS = [

]

dialog_window = [

]

newXPos = params.WIDTH / (1920 / 1777)
newYPos = params.HEIGHT / (1080 / 870)