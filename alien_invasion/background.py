import pygame

class Background:
	"""A class to manage the background surface."""

	def __init__(self, ai_game):
		"""Initialise the background and its attributes."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygame.image.load('images/spacebg1.png').convert_alpha()
		self.rect = self.image.get_rect()


	def blitme(self):
		"""Draw the background."""
		self.screen.blit(self.image, self.rect)