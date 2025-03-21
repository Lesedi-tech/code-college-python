import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('code-college-python/chapter_12/images/ship.bmp')  # Adjust path as needed
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Move the ship right if moving_right is True and within screen bounds
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1

        # Move the ship left if moving_left is True and within screen bounds
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
