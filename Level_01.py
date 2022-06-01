import pygame
import params, Block, imports, Activator
from config import cur, con

NowLocation = imports.start_room_scaled
NowLocationRect = imports.start_room_scaled_rect

walls = [
    Block.Block(10, params.HEIGHT/1.2, params.WIDTH/1.828571428571429, params.HEIGHT/1.35),
    Block.Block(10, 900, 660, 800),
    Block.Block(400, 10, 660, 800),
    Block.Block(2000, 10, 0, 950),
    Block.Block(10, 1500, 150, 100),
    Block.Block(10, 1500, 1730, 100),
    Block.Block(400, 10, 150, 250),
    Block.Block(1000, 10, 770, 250),
    Block.Block(10, 270, 550, 0),
    Block.Block(10, 270, 770, 0)
]

activator = [
    Activator.Activator(100, 100, 400, 250)
]

newXPos = 1500
newYPos = 400