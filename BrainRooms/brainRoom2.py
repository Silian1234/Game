import pygame
import params, Block, imports, Activator

NowLocation = imports.brainRoom2_scaled
NowLocationRect = imports.brainRoom2_scaled_rect

walls = [
    Block.Block(1920, 10, 0, 540)
]

activator = [
    Activator.Activator(200, 200, 1500, 780)
]

newXPos = 800
newYPos = 700