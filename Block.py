import pygame
import params, imports

class Block(pygame.sprite.Sprite):
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

	def getX(self):
		return self.rect.x

	def getY(self):
		return self.rect.y

	def getHeight(self):
		return self.rect.height

	def getWidth(self):
		return self.rect.width
