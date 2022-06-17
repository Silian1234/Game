import pygame
import params, Block, imports, Activator

NowLocation = imports.street_scaled
NowLocationRect = imports.start_room_scaled_rect

walls = [
       Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 900), params.WIDTH / (1920 / 870), params.HEIGHT / (1080 / 500)),
       Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 900), params.WIDTH / (1920 / 1045), params.HEIGHT / (1080 / 500)),
]

activator = [
    Activator.Activator(params.WIDTH / (1920 / 400), params.HEIGHT / (1080 / 100), params.WIDTH / (1920 / 750), params.HEIGHT / (1080 / 550))
]

newXPos = params.WIDTH / (1920 / 937)
newYPos = params.HEIGHT / (1080 / 987)
