import pygame
import params, Block, imports, Activator, NPS, dialogs

NowLocation = imports.workRoom_scaled
NowLocationRect = imports.workRoom_scaled_rect

walls = [
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 1000), params.WIDTH / (1920 / 385),params.HEIGHT / (1080 / 100)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 467), params.WIDTH / (1920 / 1667),params.HEIGHT / (1080 / 100)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 467), params.WIDTH / (1920 / 1667),params.HEIGHT / (1080 / 801)),
    Block.Block(params.WIDTH / (1920 / 1500), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 385),params.HEIGHT / (1080 / 995)),
    Block.Block(params.WIDTH / (1920 / 1200), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 588),params.HEIGHT / (1080 / 260)),
    Block.Block(params.WIDTH / (1920 / 300), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 1667),params.HEIGHT / (1080 / 801)),
    Block.Block(params.WIDTH / (1920 / 300), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 1667),params.HEIGHT / (1080 / 557)),
    Block.Block(params.WIDTH / (1920 / 638), params.HEIGHT / (1080 / 200), params.WIDTH / (1920 / 775),params.HEIGHT / (1080 / 847)),
    Block.Block(params.WIDTH / (1920 / 110), params.HEIGHT / (1080 / 170), params.WIDTH / (1920 / 375),params.HEIGHT / (1080 / 654)),
    Block.Block(params.WIDTH / (1920 / 500), params.HEIGHT / (1080 / 145), params.WIDTH / (1920 / 588),params.HEIGHT / (1080 / 260)),
    Block.Block(params.WIDTH / (1920 / 482), params.HEIGHT / (1080 / 366), params.WIDTH / (1920 / 850),params.HEIGHT / (1080 / 260)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 610),params.HEIGHT / (1080 / 430)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 623),params.HEIGHT / (1080 / 467)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 642),params.HEIGHT / (1080 / 504)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 665),params.HEIGHT / (1080 / 530)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 690),params.HEIGHT / (1080 / 553)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 714),params.HEIGHT / (1080 / 571)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 738),params.HEIGHT / (1080 / 580)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 762),params.HEIGHT / (1080 / 589)),
    Block.Block(params.WIDTH / (1920 / 10), params.HEIGHT / (1080 / 10), params.WIDTH / (1920 / 800),params.HEIGHT / (1080 / 607)),
    Block.Block(params.WIDTH / (1920 / 100), params.HEIGHT / (1080 / 200), params.WIDTH / (1920 / 1332),params.HEIGHT / (1080 / 260)),
]

activator = [
    Activator.Activator(params.WIDTH / (1920 / 200), params.HEIGHT / (1080 / 350), params.WIDTH / (1920 / 1332),params.HEIGHT / (1080 / 260))
]

NPSSS = [

]

dialog_window = [
    dialogs.dialog(params.WIDTH / (1920 / 1300), params.HEIGHT / (1080 / 300), params.WIDTH / (1920 / 450),params.HEIGHT / (1080 / 650), imports.firstDialog)
]

newXPos = params.WIDTH / (1920 / 1920)
newYPos = params.HEIGHT / (1080 / 730)