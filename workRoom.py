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
    Block.Block(300, 10, 1667, 801),
    Block.Block(300, 10, 1667, 557),
    Block.Block(638, 200, 775, 847),
    Block.Block(110, 170, 375, 654),
    Block.Block(500, 145, 588, 260),
    Block.Block(482, 366, 850, 260),
    Block.Block(10, 10, 610, 430),
    Block.Block(10, 10, 623, 467),
    Block.Block(10, 10, 642, 504),
    Block.Block(10, 10, 665, 530),
    Block.Block(10, 10, 690, 553),
    Block.Block(10, 10, 714, 571),
    Block.Block(10, 10, 738, 580),
    Block.Block(10, 10, 762, 589),
    Block.Block(10, 10, 800, 607),
    Block.Block(100, 200, 1332, 260),
]

activator = [
    Activator.Activator(200, 350, 1332, 260)
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(1300, 300, 450, 650, imports.firstDialog)
]

newXPos = 1920
newYPos = 730