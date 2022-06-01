import pygame
import params
import imports


class dialog(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        # Конструктор платформ
        super().__init__()
        # Также указываем фото платформы
        self.image = pygame.transform.scale(imports.blockImage, (width, height))
        self.rect = pygame.Rect(width, height, x, y)
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        self.for_text = pygame.font.SysFont('arial', 20)
        self.dialog_text = 0
        self.a = 0
        self.stroka = 0
        self.pos_stroki = 0

    def creat_text(self):
        self.dialog_text = open('test_dialog.txt')
        self.a = int(self.dialog_text.readline())
        for i in range(self.a):
            self.stroka = self.dialog_text.readline()
            self.stroka = self.for_text.render(self.stroka, True, params.WHITE)
            self.pos_stroki = self.stroka.get_rect(centre=(params.WIDTH // 2, params.HEIGHT // 2))
