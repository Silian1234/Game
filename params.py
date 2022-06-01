import pygame

pygame.display.init()
infoObject = pygame.display.Info()

WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

for_spawn_dialog_window = False
switch = 1

