import pygame
import params, Block, imports, Activator

NowLocation = imports.room5_scaled
NowLocationRect = imports.room5_scaled_rect

walls = [
    Block.Block(1920, 10, 0, 520)
]

activator = [
    Activator.Activator(120, 50, 620, 635)
]

newXPos = 960
newYPos = 830