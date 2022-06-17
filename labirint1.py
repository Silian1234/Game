import pygame
import params, Block, imports, Activator

NowLocation = imports.labirint1_scaled
NowLocationRect = imports.labirint1_scaled_rect

walls = [

]

activator = [
    Activator.Activator(517, 295, 570, 500)
]

newXPos = params.WIDTH / (params.WIDTH / 940)
newYPos = params.HEIGHT / (params.HEIGHT / 30)