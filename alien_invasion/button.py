import pygame.font

class Button:

	def __init__(self, ai_game, msg):
		"""Initialise button attributes."""
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_colour = (0, 255, 0)
		self.text_colour = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.centerx = self.screen_rect.centerx
		self.rect.y = 750

		# The button message needs to be prepped only once.
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image and center the text on the button."""
		self.msg_image = self.font.render(msg, True, self.text_colour,
				self.button_colour)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.centerx = self.rect.centerx
		self.msg_image_rect.y = self.rect.y + 10 

	def draw_button(self):
		# Draw a blank button and then draw message.
		self.screen.fill(self.button_colour, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)