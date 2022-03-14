import pygame
from pygame.sprite import Sprite

class LeftBullet(Sprite):
	"""A class to manage bullets fired from the ship."""

	def __init__(self, ai_game):
		"""Create a bullet object at the ship's current position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Create a bullet rect at (0, 0) and then set the correct position.
		self.image = pygame.image.load('images/bullets.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.midtop = ai_game.ship.rect.midtop

		# Store the bullet's position as a decimal value.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal positon of the bullet.
		self.x -= self.settings.bullet_speed
		self.y -= self.settings.bullet_speed
		# Update the rect position.
		self.rect.x = self.x
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		self.screen.blit(self.image, self.rect)

class RightBullet(Sprite):
	"""A class to manage bullets fired from the ship."""

	def __init__(self, ai_game):
		"""Create a bullet object at the ship's current position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Create a bullet rect at (0, 0) and then set the correct position.
		self.image = pygame.image.load('images/bullets.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.midtop = ai_game.ship.rect.midtop

		# Store the bullet's position as a decimal value.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal positon of the bullet.
		self.x += self.settings.bullet_speed
		self.y -= self.settings.bullet_speed
		# Update the rect position.
		self.rect.x = self.x
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		self.screen.blit(self.image, self.rect)