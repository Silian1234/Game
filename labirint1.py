import pygame
import params, Block, imports, Activator

NowLocation = imports.labirint1_scaled
NowLocationRect = imports.labirint1_scaled_rect

walls = [

]

activator = [
    Activator.Activator(params.WIDTH / (1980 / 107), params.HEIGHT / (1080 /60), params.WIDTH / (1920 /909), params.HEIGHT / (1080 /1015)),
    Activator.Activator(params.WIDTH / (1980 / 107), params.HEIGHT / (1080 /60), params.WIDTH / (1920 /1550), params.HEIGHT / (1080 /1014))
]

newXPos = params.WIDTH / (1920 / 940)
newYPos = params.HEIGHT / (1080 / 50)