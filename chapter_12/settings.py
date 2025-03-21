# settings.py
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 255)  # Blue background color
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)  # Red bullets
        self.bullet_speed = 1.5          # Speed of bullets
        self.bullets_allowed = 3         # Maximum number of bullets on screen
