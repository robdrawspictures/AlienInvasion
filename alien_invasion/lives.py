import pygame
from pygame.sprite import Sprite

class Lives(Sprite):
	"""A class to manage the ship."""

	def __init__(self, ai_game):
		"""Initialise the ship and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship_sprite.png').convert_alpha()
		self.rect = self.image.get_rect()

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
