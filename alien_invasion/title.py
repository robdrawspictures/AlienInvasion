import pygame
from pygame.sprite import Sprite

class Title(Sprite):
	"""A class to manage the ship."""

	def __init__(self, ai_game):
		"""Initialise the title and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the title image and get its rect.
		self.image = pygame.image.load('images/titlers.png').convert_alpha()
		self.rect = self.image.get_rect()

		# Position the title image.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.y = 50

	def blitme(self):
		"""Draw the title on the start screen."""
		self.screen.blit(self.image, self.rect)
