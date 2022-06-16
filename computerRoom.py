import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.computerRoom_scaled
NowLocationRect = imports.computerRoom_scaled_rect

walls = [
    Block.Block(1700, 10, 170, 242),
    Block.Block(1700, 10, 160, 950),
    Block.Block(10, 700, 180, 250),
    Block.Block(10, 650, 1730, 400),
    Block.Block(145, 500, 190, 531),
    Block.Block(100, 159, 170, 242),
    Block.Block(544, 100, 170, 860),
    Block.Block(210, 350, 1350, 603)
]

activator = [
    Activator.Activator(200, 200, 1050, 250),
    Activator.Activator(200, 200, 1250, 700)
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(1300, 300, 450, 650, imports.secondDialog)
]

newXPos = params.WIDTH / (params.WIDTH / 1610)
newYPos = params.HEIGHT / (params.HEIGHT / 365)