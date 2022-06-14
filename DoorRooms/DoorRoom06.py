import pygame
import params, Block, imports, Activator

NowLocation = imports.room6_scaled
NowLocationRect = imports.room6_scaled_rect

walls = [
    Block.Block(1920, 10, 0, 520)
]

activator = [
    Activator.Activator(50, 50, 500, 500)
]

newXPos = 960
newYPos = 830