import pygame
import params, imports

class NPS(pygame.sprite.Sprite):
	def __init__(self, width, height, x, y):
		# Конструктор платформ
		super().__init__()
		# Также указываем фото платформы
		self.image = pygame.transform.scale(imports.player_image_right1, (width, height))
		self.rect = pygame.Rect(width, height, x, y)
		self.rect.x = x
		self.rect.y = y
		self.rect.width = width
		self.rect.height = height

	def get_NPS_X(self):
		return self.rect.x

	def get_NPS_Y(self):
		return self.rect.y

	def get_NPS_Height(self):
		return self.rect.height

	def get_NPS_Width(self):
		return self.rect.width

