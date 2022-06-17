import pygame
import params, Block, imports, Activator
from config import cur, con

NowLocation = imports.start_room_scaled
NowLocationRect = imports.start_room_scaled_rect

walls = [
    Block.Block(10, params.HEIGHT/1.2, params.WIDTH/1.828571428571429, params.HEIGHT/1.35),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 900), params.WIDTH / (1920 / 660), params.HEIGHT / (1080 / 800)),
    Block.Block(params.WIDTH / (1920 / 400), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 660), params.HEIGHT / (1080 / 800)),
    Block.Block(params.WIDTH / (1920 / 2000), params.HEIGHT / (1080 / 10), 0, params.HEIGHT / (1080 / 950)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 1500), params.WIDTH / (1920 / 150), params.HEIGHT / (1080 / 100)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 1500), params.WIDTH / (1920 / 1730), params.HEIGHT / (1080 / 100)),
    Block.Block(params.WIDTH / (1920 / 400), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 150), params.HEIGHT / (1080 / 250)),
    Block.Block(params.WIDTH / (1920 / 1000), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 770), params.HEIGHT / (1080 / 250)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 270), params.WIDTH / (1920 / 550), 0),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 270), params.WIDTH / (1920 / 770), 0),
    Block.Block(params.WIDTH / (1920 / 125), params.HEIGHT / (1080 / 120), params.WIDTH / (1920 / 1050), params.HEIGHT / (1080 / 820)),
    Block.Block(params.WIDTH / (1920 / 400), params.HEIGHT / (1080 / 130), params.WIDTH / (1920 / 1345), params.HEIGHT / (1080 / 283)),
    Block.Block(params.WIDTH / (1920 / 240), params.HEIGHT / (1080 / 200), params.WIDTH / (1920 / 240), params.HEIGHT / (1080 / 170)),
    Block.Block(params.WIDTH / (1920 / 96), params.HEIGHT / (1080 / 90), params.WIDTH / (1920 / 911), params.HEIGHT / (1080 / 270)),
    Block.Block(params.WIDTH / (1920 / 260), params.HEIGHT / (1080 / 400), params.WIDTH / (1920 / 171), params.HEIGHT / (1080 / 600)),
    Block.Block(params.WIDTH / (1920 / 96), params.HEIGHT / (1080 / 90), params.WIDTH / (1920 / 1567), params.HEIGHT / (1080 / 820)),
    Block.Block(params.WIDTH / (1920 / 170), params.HEIGHT / (1080 / 81), params.WIDTH / (1920 / 780), params.HEIGHT / (1080 / 639)),
]

activator = [

]

newXPos = params.WIDTH / 1.2
newYPos = params.HEIGHT / 2
