import pygame
from settings import Settings
from game import Game

def run_game():
    # Initialize Pygame
    pygame.init()

    # Set up game settings
    settings = Settings()

    # Create a game instance
    game = Game(settings)

    # Start the game loop
    game.run()

if __name__ == '__main__':
    run_game()
