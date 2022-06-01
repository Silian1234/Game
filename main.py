import pygame, random, importlib
import dialogs
import menu, imports, player, Block, NPS, Level_01, params

importlib.reload(menu)

# Создаем игру и окноф
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
pygame.display.set_caption("Devil Eye")
clock = pygame.time.Clock()

WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h

dialog_window = [dialogs.dialog(1000, 300, 450, 650)]

all_sprites = pygame.sprite.Group()
sprites_for_dialog = pygame.sprite.Group()

"""NPSS = [
    NPS.NPS(params.WIDTH/20, params.HEIGHT/13, 870, 600),
]"""

#walls = []

"""for i in range(0, len(NPSS)):
    all_sprites.add(NPSS[i])"""

#for i in range(0, len(walls)):
#    all_sprites.add(walls[i])

for i in range(0, len(dialog_window)):
    sprites_for_dialog.add(dialog_window[i])

player = player.Player()
#player.setWalls(walls)
#player.setNPSS(NPSS)
player.setDialog(dialog_window)
all_sprites.add(player)

menu.start()

pygame.quit()