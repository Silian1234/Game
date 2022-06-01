import pygame

import NPS
import player

pygame.init()

check_position = [NPS.NPS.rect.x, NPS.NPS.rect.y]

def s_kem_govorim():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                for i in range(len(check_position)):
                    if player.Player.rect.colliderect(check_position[i]):
                        return i
