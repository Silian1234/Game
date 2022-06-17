import pygame
import params, Block, imports, Activator, ActivatorV2

NowLocation = imports.brainRoom3_scaled
NowLocationRect = imports.brainRoom3_scaled_rect

walls = [
    Block.Block(params.WIDTH / (1920 / 1920), params.HEIGHT / (1080 / 10), 0, params.HEIGHT / (1080 / 540))
]

activator = [
    Activator.Activator(params.WIDTH / (1920 / 200), params.HEIGHT / (1080 / 200), params.WIDTH / (1920 / 200), params.HEIGHT / (1080 / 780))
]

activatorV2 = [
    Activator.Activator(params.WIDTH / (1920 / 200), params.HEIGHT / (1080 / 200), params.WIDTH / (1920 / 1500), params.HEIGHT / (1080 / 780))
]

newXPos = params.WIDTH / (1920 / 800)
newYPos = params.HEIGHT / (1080 / 700)