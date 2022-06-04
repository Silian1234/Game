import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.workRoom_scaled
NowLocationRect = imports.workRoom_scaled_rect

walls = [
    Block.Block(10, 1000, 385, 100),
    Block.Block(10, 467, 1667, 100),
    Block.Block(10, 467, 1667, 801),
    Block.Block(1500, 10, 385, 995),
    Block.Block(1200, 10, 588, 260),
]

activator = [
    Activator.Activator(200, 200, 1050, 250)
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(1300, 300, 450, 650, imports.firstDialog)
]

newXPos = 1700
newYPos = 600