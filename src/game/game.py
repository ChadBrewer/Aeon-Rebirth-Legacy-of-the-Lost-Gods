
import pygame
from .player import Player
from .enemy import Enemy

class Game:
    def __init__(self, settings):
        self.settings = settings
        self.screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update game state here
            
            # Clear screen
            self.screen.fill(self.settings.bg_color)
            
            # Draw game objects here
            
            pygame.display.flip()
            self.clock.tick(self.settings.fps)

        pygame.quit()
