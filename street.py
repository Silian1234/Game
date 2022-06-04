import pygame
import params, Block, imports, Activator

NowLocation = imports.street_scaled
NowLocationRect = imports.start_room_scaled_rect

walls = [
       Block.Block(10, 900, 870, 500),
       Block.Block(10, 900, 1045, 500),
]

activator = [
    Activator.Activator(400, 100, 750, 550)
]

newXPos = 1000
newYPos = 1900
