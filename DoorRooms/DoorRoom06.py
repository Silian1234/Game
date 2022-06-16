import pygame
import params, Block, imports, Activator

NowLocation = imports.room6_scaled
NowLocationRect = imports.room6_scaled_rect

walls = [
    Block.Block(1920, 10, 0, 520)
]

activator = [
    Activator.Activator(params.WIDTH / (params.WIDTH / 208), params.HEIGHT / (params.HEIGHT / 105),
                        params.WIDTH / (params.WIDTH / 100), params.HEIGHT / (params.HEIGHT / 622)),
    Activator.Activator(params.WIDTH / (params.WIDTH / 230), params.HEIGHT / (params.HEIGHT / 110),
                        params.WIDTH / (params.WIDTH / 566), params.HEIGHT / (params.HEIGHT / 608)),
    Activator.Activator(params.WIDTH / (params.WIDTH / 210), params.HEIGHT / (params.HEIGHT / 106),
                        params.WIDTH / (params.WIDTH / 1066), params.HEIGHT / (params.HEIGHT / 622)),
    Activator.Activator(params.WIDTH / (params.WIDTH / 208), params.HEIGHT / (params.HEIGHT / 105),
                        params.WIDTH / (params.WIDTH / 1566), params.HEIGHT / (params.HEIGHT / 622))
]

newXPos = params.WIDTH / (params.WIDTH / 888)
newYPos = params.HEIGHT / (params.HEIGHT / 814)