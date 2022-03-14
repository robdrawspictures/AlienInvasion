class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialise the game's settings."""
		# Screen Settings
		self.screen_width = 1920
		self.screen_height = 1080
		self.bg_colour = (0, 0, 0)
		
		# Ship settings
		self.ship_speed = 3.0	
		self.ship_limit = 3

		# Bullet settings
		self.bullet_speed = 2.0		
		self.bullets_allowed = 10
		self.extra_bullets_allowed = 10

		# Alien settings		
		self.fleet_drop_speed = 10

		# How quickly the game speeds up
		self.speedup_scale = 1.2

		# How quickly the alien point values increase
		self.score_scale = 1.5

		self.initialise_dynamic_settings()

	def initialise_dynamic_settings(self):
		"""Initialise settings that change throughout the game."""
		self.alien_speed = 1.0

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50
		self.stage_clear_points = 1000

	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		# self.ship_speed *= self.speedup_scale
		# self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
